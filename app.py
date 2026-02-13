from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import re

app = Flask(__name__)

# Emergency keywords that trigger alerts
EMERGENCY_KEYWORDS = [
    'chest pain', 'heart attack', 'stroke', 'breathing problem', 
    'difficulty breathing', 'can\'t breathe', 'suicide', 'kill myself',
    'severe bleeding', 'unconscious', 'seizure', 'choking',
    'severe headache', 'paralysis', 'severe pain'
]

def get_db_connection():
    """Create database connection"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def detect_emergency(message):
    """Check if message contains emergency keywords"""
    message_lower = message.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in message_lower:
            return True, keyword
    return False, None

def log_chat(user_message, bot_response):
    """Store chat conversation in database"""
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO chat_logs (user_message, bot_response) VALUES (?, ?)',
        (user_message, bot_response)
    )
    conn.commit()
    conn.close()

def log_emergency(message):
    """Store emergency alert in database"""
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO emergency_logs (message) VALUES (?)',
        (message,)
    )
    conn.commit()
    conn.close()

def get_disease_info(disease_name):
    """Fetch disease information from database"""
    conn = get_db_connection()
    disease = conn.execute(
        'SELECT * FROM diseases WHERE LOWER(name) = ?',
        (disease_name.lower(),)
    ).fetchone()
    conn.close()
    return disease

def search_disease_by_keyword(keyword):
    """Search diseases by keyword in name"""
    conn = get_db_connection()
    keyword = f'%{keyword.lower()}%'
    diseases = conn.execute(
        'SELECT * FROM diseases WHERE LOWER(name) LIKE ? LIMIT 5',
        (keyword,)
    ).fetchall()
    conn.close()
    return diseases

def generate_response(message):
    """Main chatbot engine - provides symptoms and prevention for diseases"""
    message_clean = message.lower().strip()
    
    # Check for emergency
    is_emergency, emergency_keyword = detect_emergency(message)
    if is_emergency:
        log_emergency(message)
        return {
            'type': 'emergency',
            'message': f'⚠️ EMERGENCY DETECTED: {emergency_keyword}\n\n'
                      '🚨 Please seek immediate medical attention!\n\n'
                      '📞 Emergency Numbers:\n'
                      '• India: 112 / 108\n'
                      '• US: 911\n'
                      '• UK: 999\n\n'
                      'If you are experiencing a medical emergency, please call emergency services or go to the nearest hospital immediately.'
        }
    
    # Greetings
    greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
    if any(greet in message_clean for greet in greetings):
        return {
            'type': 'greeting',
            'message': '👋 Hello! I\'m your Health Information Assistant.\n\n'
                      'Simply type any disease name to get information about its symptoms and prevention.\n\n'
                      'Examples:\n'
                      '• Type "diabetes" to learn about diabetes\n'
                      '• Type "covid" for COVID-19 information\n'
                      '• Type "malaria" for malaria details\n\n'
                      'What disease would you like to know about?'
        }
    
    # Help command
    if 'help' in message_clean or 'list' in message_clean:
        conn = get_db_connection()
        diseases = conn.execute('SELECT name FROM diseases ORDER BY name').fetchall()
        conn.close()
        
        disease_list = '\n'.join([f'• {d["name"]}' for d in diseases])
        return {
            'type': 'help',
            'message': f'📚 Available Diseases in Database:\n\n{disease_list}\n\n'
                      'Just type the disease name to get symptoms and prevention information!'
        }
    
    # Remove common words to get disease name
    words_to_remove = ['what', 'is', 'tell', 'me', 'about', 'information', 'on', 'explain', 
                       'describe', 'details', 'of', 'the', 'a', 'an', '?', 'prevention', 
                       'symptoms', 'for', 'give', 'show']
    
    disease_query = message_clean
    for word in words_to_remove:
        disease_query = disease_query.replace(word, ' ')
    disease_query = disease_query.strip()
    
    # If query is empty after removing common words, use original message
    if not disease_query:
        disease_query = message_clean
    
    # Try to find disease in database
    disease = get_disease_info(disease_query)
    
    # If no exact match, try keyword search
    if not disease:
        diseases = search_disease_by_keyword(disease_query)
        if diseases:
            disease = diseases[0]
    
    if disease:
        # Build simple response with symptoms and prevention
        response = f'📋 **{disease["name"]}**\n\n'
        response += f'🤒 **SYMPTOMS:**\n{disease["symptoms"]}\n\n'
        response += f'🛡️ **PREVENTION:**\n{disease["prevention"]}\n\n'
        response += '⚠️ **Disclaimer:** This information is for educational purposes only. Always consult a healthcare professional for medical advice and diagnosis.'
        
        return {
            'type': 'disease_info', 
            'message': response,
            'disease': dict(disease)
        }
    else:
        # Disease not found
        conn = get_db_connection()
        all_diseases = conn.execute('SELECT name FROM diseases ORDER BY name').fetchall()
        conn.close()
        
        # Show similar diseases if any
        similar_diseases = []
        for d in all_diseases:
            if any(word in d['name'].lower() for word in disease_query.split()):
                similar_diseases.append(d['name'])
        
        if similar_diseases:
            similar_list = '\n'.join([f'• {name}' for name in similar_diseases[:5]])
            return {
                'type': 'not_found',
                'message': f'❌ Disease "{message}" not found in database.\n\n'
                          f'Did you mean:\n{similar_list}\n\n'
                          'Type "help" or "list" to see all available diseases.'
            }
        else:
            return {
                'type': 'not_found',
                'message': f'❌ Disease "{message}" not found in database.\n\n'
                          'Type "help" or "list" to see all available diseases.\n\n'
                          'Available diseases include: COVID-19, Dengue, Diabetes, Malaria, Tuberculosis, and many more!'
            }

# Routes
@app.route('/')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    return render_template('dashboard.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    # Generate response
    response_data = generate_response(user_message)
    
    # Log conversation
    log_chat(user_message, response_data['message'])
    
    return jsonify(response_data)

@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    """Get all diseases"""
    conn = get_db_connection()
    diseases = conn.execute('SELECT * FROM diseases ORDER BY name').fetchall()
    conn.close()
    
    return jsonify([dict(d) for d in diseases])

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics"""
    conn = get_db_connection()
    
    # Total chats
    total_chats = conn.execute('SELECT COUNT(*) as count FROM chat_logs').fetchone()['count']
    
    # Total emergencies
    total_emergencies = conn.execute('SELECT COUNT(*) as count FROM emergency_logs').fetchone()['count']
    
    # Total diseases
    total_diseases = conn.execute('SELECT COUNT(*) as count FROM diseases').fetchone()['count']
    
    # Recent chats
    recent_chats = conn.execute(
        'SELECT * FROM chat_logs ORDER BY timestamp DESC LIMIT 10'
    ).fetchall()
    
    # Emergency logs
    emergency_logs = conn.execute(
        'SELECT * FROM emergency_logs ORDER BY timestamp DESC LIMIT 10'
    ).fetchall()
    
    # Count disease mentions in chats
    from collections import Counter
    all_messages = conn.execute('SELECT user_message FROM chat_logs').fetchall()
    diseases = conn.execute('SELECT name FROM diseases').fetchall()
    conn.close()
    
    disease_mentions = Counter()
    disease_names = [d['name'].lower() for d in diseases]
    for msg in all_messages:
        msg_lower = msg['user_message'].lower()
        for disease in disease_names:
            if disease in msg_lower:
                disease_mentions[disease.title()] += 1
    
    top_diseases = disease_mentions.most_common(5)
    
    return jsonify({
        'total_chats': total_chats,
        'total_emergencies': total_emergencies,
        'total_diseases': total_diseases,
        'recent_chats': [dict(c) for c in recent_chats],
        'emergency_logs': [dict(e) for e in emergency_logs],
        'top_diseases': top_diseases
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)