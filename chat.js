// Chat functionality
const chatBox = document.getElementById('chatBox');
const userInput = document.getElementById('userInput');
const typingIndicator = document.getElementById('typing-indicator');

// Initialize chat
function initChat() {
    // Remove welcome message on first interaction
    userInput.addEventListener('focus', () => {
        const welcomeMsg = document.querySelector('.welcome-message');
        if (welcomeMsg) {
            welcomeMsg.style.display = 'none';
        }
    }, { once: true });
}

// Send message on Enter key
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

// Send example query
function sendExample(text) {
    userInput.value = text;
    sendMessage();
}

// Send message function
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message) {
        return;
    }
    
    // Remove welcome message if present
    const welcomeMsg = document.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.remove();
    }
    
    // Add user message to chat
    addMessage(message, 'user');
    
    // Clear input
    userInput.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    try {
        // Send to backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        // Hide typing indicator
        hideTypingIndicator();
        
        // Add bot response
        addMessage(data.message, 'bot', data.type);
        
    } catch (error) {
        console.error('Error:', error);
        hideTypingIndicator();
        addMessage('Sorry, I encountered an error. Please try again.', 'bot', 'error');
    }
}

// Add message to chat box
function addMessage(text, sender, type = 'default') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${sender}`;
    
    const time = new Date().toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit' 
    });
    
    let iconHtml = '';
    let contentClass = 'message-content';
    
    if (sender === 'user') {
        iconHtml = '<div class="message-icon"><i class="fas fa-user"></i></div>';
    } else {
        iconHtml = '<div class="message-icon"><i class="fas fa-robot"></i></div>';
        
        // Add special styling for emergency messages
        if (type === 'emergency') {
            contentClass += ' emergency-message';
        }
    }
    
    // Format message text (convert markdown-style formatting)
    let formattedText = formatMessage(text);
    
    if (sender === 'user') {
        messageDiv.innerHTML = `
            <div class="${contentClass}">
                ${formattedText}
                <div class="message-time">${time}</div>
            </div>
            ${iconHtml}
        `;
    } else {
        messageDiv.innerHTML = `
            ${iconHtml}
            <div class="${contentClass}">
                ${formattedText}
                <div class="message-time">${time}</div>
            </div>
        `;
    }
    
    chatBox.appendChild(messageDiv);
    
    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Format message text
function formatMessage(text) {
    // Convert **bold** to <strong>
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert bullet points
    text = text.replace(/^[•·]\s/gm, '• ');
    
    // Convert numbered lists
    text = text.replace(/^(\d+)[.)]\s/gm, '$1. ');
    
    // Convert line breaks to <br>
    text = text.replace(/\n/g, '<br>');
    
    // Convert emoji shortcuts
    text = text.replace(/:\)/g, '😊');
    text = text.replace(/:\(/g, '😞');
    
    return text;
}

// Show typing indicator
function showTypingIndicator() {
    typingIndicator.style.display = 'flex';
}

// Hide typing indicator
function hideTypingIndicator() {
    typingIndicator.style.display = 'none';
}

// Clear chat
function clearChat() {
    if (confirm('Are you sure you want to clear the chat?')) {
        chatBox.innerHTML = `
            <div class="welcome-message">
                <div class="text-center">
                    <i class="fas fa-heartbeat fa-4x text-primary mb-3"></i>
                    <h3>Welcome to AI Public Health Chatbot! 👋</h3>
                    <p class="lead">Your intelligent health awareness companion</p>
                    <p>I can help you with disease information, symptom checking, and preventive healthcare guidance.</p>
                    <p class="text-muted">Type a message to get started...</p>
                </div>
            </div>
        `;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', initChat);

// Voice input support (optional enhancement)
if ('webkitSpeechRecognition' in window) {
    const recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        sendMessage();
    };
    
    // Add voice button (if you want to enable this)
    // const voiceBtn = document.createElement('button');
    // voiceBtn.innerHTML = '<i class="fas fa-microphone"></i>';
    // voiceBtn.onclick = () => recognition.start();
}

// Auto-focus input on page load
window.addEventListener('load', () => {
    userInput.focus();
});

// Prevent form submission if wrapped in form
document.addEventListener('submit', (e) => {
    e.preventDefault();
});