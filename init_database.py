import sqlite3
from datetime import datetime

def init_database():
    """Initialize SQLite database with tables and comprehensive disease data"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Drop existing tables
    cursor.execute('DROP TABLE IF EXISTS diseases')
    cursor.execute('DROP TABLE IF EXISTS chat_logs')
    cursor.execute('DROP TABLE IF EXISTS emergency_logs')
    
    # Create Diseases Table
    cursor.execute('''
        CREATE TABLE diseases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            symptoms TEXT NOT NULL,
            prevention TEXT NOT NULL,
            causes TEXT,
            risk_factors TEXT,
            info TEXT
        )
    ''')
    
    # Create Chat Logs Table
    cursor.execute('''
        CREATE TABLE chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create Emergency Logs Table
    cursor.execute('''
        CREATE TABLE emergency_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Comprehensive Disease Data (60 Diseases)
    diseases = [
        {
            'name': 'COVID-19',
            'symptoms': 'Fever, dry cough, tiredness, difficulty breathing, loss of taste or smell, sore throat, headache, body aches, diarrhea, skin rash',
            'prevention': 'Get vaccinated, wear masks in crowded places, maintain 6 feet distance, wash hands frequently with soap for 20 seconds, use hand sanitizer, avoid touching face, stay home if sick, improve ventilation indoors',
            'causes': 'SARS-CoV-2 virus transmitted through respiratory droplets and aerosols',
            'risk_factors': 'Age over 60, diabetes, heart disease, obesity, lung disease, weakened immune system, pregnancy',
            'info': 'COVID-19 is a respiratory illness caused by the SARS-CoV-2 virus. It ranges from mild to severe and can be life-threatening.'
        },
        {
            'name': 'Dengue Fever',
            'symptoms': 'High fever (104°F), severe headache, pain behind eyes, joint and muscle pain, nausea, vomiting, skin rash, mild bleeding (nose/gums)',
            'prevention': 'Eliminate stagnant water, use mosquito repellent (DEET), wear long-sleeved clothes, install window screens, use mosquito nets while sleeping, empty water containers weekly',
            'causes': 'Dengue virus (DEN-1, DEN-2, DEN-3, DEN-4) transmitted by Aedes aegypti mosquitoes',
            'risk_factors': 'Living in tropical/subtropical areas, previous dengue infection, weakened immune system, outdoor activities during peak mosquito hours',
            'info': 'Dengue is a mosquito-borne viral infection common in tropical regions. Severe dengue can cause internal bleeding and death.'
        },
        {
            'name': 'Diabetes Type 2',
            'symptoms': 'Increased thirst, frequent urination, increased hunger, unexplained weight loss, fatigue, blurred vision, slow-healing sores, frequent infections, tingling in hands/feet, darkened skin areas',
            'prevention': 'Maintain healthy weight (BMI 18.5-24.9), exercise 150 minutes weekly, eat balanced diet (low sugar, high fiber), limit processed foods, avoid sugary drinks, quit smoking, manage stress, regular health checkups',
            'causes': 'Insulin resistance where body cells do not respond properly to insulin, leading to high blood sugar',
            'risk_factors': 'Obesity, family history, age over 45, sedentary lifestyle, high blood pressure, high cholesterol, PCOS, gestational diabetes history',
            'info': 'Type 2 diabetes is a chronic metabolic condition where the body cannot properly use insulin, leading to high blood sugar levels.'
        },
        {
            'name': 'Malaria',
            'symptoms': 'Fever with chills, sweating, headache, nausea, vomiting, muscle pain, fatigue, rapid breathing, enlarged spleen, jaundice, anemia',
            'prevention': 'Take antimalarial medications when traveling to endemic areas, use insecticide-treated bed nets, apply mosquito repellent, wear protective clothing (long sleeves/pants), use indoor insecticide spray, avoid outdoor activities at dusk/dawn',
            'causes': 'Plasmodium parasites (P. falciparum, P. vivax, P. ovale, P. malariae) transmitted by female Anopheles mosquitoes',
            'risk_factors': 'Living/traveling to endemic areas (sub-Saharan Africa, South Asia, Central/South America), lack of preventive measures, pregnancy, young children, people with HIV/AIDS',
            'info': 'Malaria is a life-threatening parasitic disease transmitted by mosquitoes. Early diagnosis and treatment are crucial.'
        },
        {
            'name': 'Tuberculosis',
            'symptoms': 'Persistent cough (3+ weeks), coughing up blood or mucus, chest pain, unintentional weight loss, fever, night sweats, chills, fatigue, loss of appetite',
            'prevention': 'Get BCG vaccine (in endemic areas), avoid close contact with TB patients, ensure good ventilation, cover mouth when coughing, complete full treatment course if infected, strengthen immune system, get tested if exposed',
            'causes': 'Mycobacterium tuberculosis bacteria spread through airborne droplets when infected person coughs or sneezes',
            'risk_factors': 'HIV infection, weakened immune system, malnutrition, diabetes, kidney disease, smoking, alcohol abuse, living in crowded conditions, healthcare workers',
            'info': 'TB is a bacterial infection primarily affecting lungs but can affect other organs. It is curable with proper treatment.'
        },
        {
            'name': 'Hypertension',
            'symptoms': 'Often no symptoms (silent killer), severe headache, chest pain, dizziness, difficulty breathing, nosebleeds, blood spots in eyes, irregular heartbeat',
            'prevention': 'Reduce salt intake (less than 5g daily), exercise regularly (30 min daily), maintain healthy weight, limit alcohol (1-2 drinks daily), quit smoking, manage stress (yoga, meditation), eat potassium-rich foods, reduce caffeine',
            'causes': 'Multiple factors including genetics, poor diet, lack of exercise, stress, kidney disease',
            'risk_factors': 'Age over 60, family history, obesity, high salt diet, lack of exercise, smoking, excessive alcohol, stress, chronic kidney disease, sleep apnea',
            'info': 'High blood pressure is a condition where blood force against artery walls is consistently too high, increasing heart disease and stroke risk.'
        },
        {
            'name': 'Asthma',
            'symptoms': 'Shortness of breath, chest tightness or pain, wheezing, coughing (especially at night), difficulty sleeping due to breathing problems, whistling sound when exhaling',
            'prevention': 'Avoid triggers (smoke, allergens, pollution, cold air), take prescribed medications regularly, use air purifiers, keep home clean and dust-free, avoid pets if allergic, get flu vaccine annually, maintain healthy weight, exercise moderately',
            'causes': 'Airway inflammation and narrowing triggered by allergens, irritants, exercise, cold air, stress',
            'risk_factors': 'Family history, allergies (hay fever, eczema), obesity, smoking, exposure to secondhand smoke, air pollution, occupational exposure to chemicals',
            'info': 'Asthma is a chronic respiratory condition causing inflamed and narrowed airways, making breathing difficult.'
        },
        {
            'name': 'Influenza',
            'symptoms': 'Fever (100-104°F), chills, cough, sore throat, runny/stuffy nose, muscle/body aches, headache, fatigue, vomiting and diarrhea (more common in children)',
            'prevention': 'Get annual flu vaccine, wash hands frequently, avoid touching face, stay away from sick people, clean and disinfect surfaces, cover coughs and sneezes, stay home when sick, boost immune system',
            'causes': 'Influenza A, B, C viruses transmitted through respiratory droplets and contaminated surfaces',
            'risk_factors': 'Age (children under 5, adults over 65), weakened immune system, chronic diseases (asthma, diabetes, heart disease), pregnancy, obesity, living in crowded places',
            'info': 'Flu is a contagious respiratory illness that can cause mild to severe symptoms and lead to serious complications.'
        },
        {
            'name': 'Heart Attack',
            'symptoms': 'Chest pain/discomfort (pressure, squeezing), pain in arms/back/neck/jaw/stomach, shortness of breath, cold sweat, nausea, lightheadedness, fatigue',
            'prevention': 'Exercise regularly (150 min weekly), eat heart-healthy diet (fruits, vegetables, whole grains), maintain healthy weight, manage stress, quit smoking, limit alcohol, control blood pressure/cholesterol/diabetes, get regular checkups',
            'causes': 'Blockage in coronary arteries (usually due to plaque buildup) restricting blood flow to heart muscle',
            'risk_factors': 'High blood pressure, high cholesterol, diabetes, smoking, obesity, family history, age (men 45+, women 55+), sedentary lifestyle, stress',
            'info': 'A heart attack occurs when blood flow to heart is severely reduced or blocked. Immediate medical attention is critical.'
        },
        {
            'name': 'Stroke',
            'symptoms': 'Sudden numbness/weakness (face, arm, leg - especially one side), confusion, trouble speaking/understanding, vision problems in one or both eyes, difficulty walking, dizziness, loss of balance, severe headache',
            'prevention': 'Control blood pressure, exercise regularly, eat healthy diet (low sodium, high potassium), maintain healthy weight, limit alcohol, quit smoking, manage diabetes/cholesterol, treat atrial fibrillation, reduce stress',
            'causes': 'Blood clot blocking artery to brain (ischemic stroke) or ruptured blood vessel in brain (hemorrhagic stroke)',
            'risk_factors': 'High blood pressure, diabetes, heart disease, smoking, obesity, age over 55, family history, previous stroke/TIA, atrial fibrillation, high cholesterol',
            'info': 'A stroke occurs when blood supply to brain is interrupted. Time is critical - seek immediate emergency help (remember F.A.S.T.).'
        },
        {
            'name': 'Pneumonia',
            'symptoms': 'Cough with phlegm/pus, fever, chills, difficulty breathing, chest pain when breathing/coughing, fatigue, nausea, vomiting, diarrhea, confusion (in elderly)',
            'prevention': 'Get vaccinated (pneumococcal, flu), wash hands frequently, quit smoking, maintain strong immune system, avoid sick people, practice good hygiene, treat respiratory infections promptly',
            'causes': 'Bacterial (Streptococcus pneumoniae), viral (influenza), or fungal infections causing lung inflammation',
            'risk_factors': 'Age (under 2, over 65), weakened immune system, chronic diseases, smoking, hospitalization, ventilator use',
            'info': 'Pneumonia is a lung infection causing air sacs to fill with fluid or pus, making breathing difficult.'
        },
        {
            'name': 'Cholera',
            'symptoms': 'Severe watery diarrhea (rice-water stools), nausea, vomiting, rapid dehydration, muscle cramps, low blood pressure, rapid heart rate, dry skin, extreme thirst',
            'prevention': 'Drink safe/boiled water, avoid raw/undercooked food, wash hands with soap, use proper sanitation, get vaccinated (if traveling to endemic areas), peel fruits/vegetables, avoid street food',
            'causes': 'Vibrio cholerae bacteria from contaminated water or food',
            'risk_factors': 'Poor sanitation, contaminated water sources, crowded living conditions, lack of stomach acid, type O blood, raw shellfish consumption',
            'info': 'Cholera is an acute diarrheal disease that can be fatal within hours if untreated. Rehydration is key treatment.'
        },
        {
            'name': 'Typhoid Fever',
            'symptoms': 'Prolonged fever (103-104°F), weakness, stomach pain, headache, loss of appetite, rash (rose spots), constipation or diarrhea, enlarged spleen/liver',
            'prevention': 'Get vaccinated before traveling to endemic areas, drink safe/boiled water, avoid raw foods, wash hands frequently, avoid street vendors, use proper sanitation, cook food thoroughly',
            'causes': 'Salmonella typhi bacteria from contaminated food or water',
            'risk_factors': 'Traveling to endemic areas (South Asia, Africa, Latin America), poor sanitation, contaminated water, lack of vaccination',
            'info': 'Typhoid is a bacterial infection causing high fever and gastrointestinal symptoms. Antibiotic treatment is essential.'
        },
        {
            'name': 'Hepatitis B',
            'symptoms': 'Fatigue, loss of appetite, nausea, vomiting, abdominal pain, dark urine, clay-colored stool, joint pain, jaundice (yellow skin/eyes), fever',
            'prevention': 'Get vaccinated (most effective), use condoms during sex, do not share needles/razors/toothbrushes, ensure sterile medical equipment, screen blood donations, practice safe injection practices',
            'causes': 'Hepatitis B virus (HBV) transmitted through blood, semen, or other body fluids',
            'risk_factors': 'Unprotected sex, sharing needles, healthcare workers, living with infected person, travel to endemic areas, dialysis patients, HIV infection',
            'info': 'Hepatitis B is a viral liver infection that can become chronic and lead to cirrhosis or liver cancer.'
        },
        {
            'name': 'Hepatitis C',
            'symptoms': 'Often no symptoms initially, fatigue, fever, nausea, vomiting, abdominal pain, dark urine, joint pain, jaundice, loss of appetite',
            'prevention': 'Do not share needles or drug equipment, avoid sharing personal items (razors, toothbrushes), ensure sterile medical/tattoo equipment, practice safe sex, get tested if at risk, screen blood donations',
            'causes': 'Hepatitis C virus (HCV) transmitted through blood contact',
            'risk_factors': 'Injection drug use, blood transfusion before 1992, long-term hemodialysis, tattoos/piercings with unsterile equipment, HIV infection, being born to HCV-positive mother',
            'info': 'Hepatitis C is a bloodborne viral infection affecting the liver. Chronic infection can lead to serious liver damage.'
        },
        {
            'name': 'HIV/AIDS',
            'symptoms': 'Flu-like symptoms initially (fever, fatigue, rash, sore throat, swollen lymph nodes), weight loss, chronic diarrhea, night sweats, recurring infections, oral thrush',
            'prevention': 'Use condoms during sex, take PrEP if high-risk, never share needles, get tested regularly, limit sexual partners, treat STIs promptly, use post-exposure prophylaxis (PEP) if exposed, ensure safe blood transfusions',
            'causes': 'Human Immunodeficiency Virus (HIV) transmitted through blood, semen, vaginal fluids, breast milk',
            'risk_factors': 'Unprotected sex, multiple sexual partners, injection drug use, STIs, blood transfusions in areas with poor screening, mother-to-child transmission',
            'info': 'HIV attacks the immune system. Without treatment, it progresses to AIDS. Modern antiretroviral therapy allows normal lifespan.'
        },
        {
            'name': 'Chickenpox',
            'symptoms': 'Itchy rash with fluid-filled blisters, fever, headache, fatigue, loss of appetite, rash progressing from red spots to blisters to scabs',
            'prevention': 'Get varicella vaccine (2 doses), avoid contact with infected persons, practice good hygiene, wash hands frequently, isolate infected individuals, do not scratch blisters',
            'causes': 'Varicella-zoster virus spread through direct contact or airborne droplets',
            'risk_factors': 'Not vaccinated, contact with infected person, weakened immune system, pregnancy, age (more severe in adults)',
            'info': 'Chickenpox is a highly contagious viral infection causing itchy rash and fever. Vaccine is highly effective.'
        },
        {
            'name': 'Measles',
            'symptoms': 'High fever, cough, runny nose, red/watery eyes, white spots in mouth (Koplik spots), red rash starting on face spreading to body',
            'prevention': 'Get MMR vaccine (2 doses), avoid contact with infected persons, practice good hygiene, boost immune system, isolate infected individuals, vitamin A supplementation',
            'causes': 'Measles virus (rubeola) spread through airborne droplets',
            'risk_factors': 'Not vaccinated, vitamin A deficiency, weakened immune system, travel to endemic areas, crowded living conditions',
            'info': 'Measles is a highly contagious viral disease that can cause serious complications including pneumonia and brain damage.'
        },
        {
            'name': 'Mumps',
            'symptoms': 'Swollen/painful salivary glands (especially parotid glands), fever, headache, muscle aches, fatigue, loss of appetite, pain while chewing/swallowing',
            'prevention': 'Get MMR vaccine (2 doses), avoid sharing utensils/drinks, practice good hygiene, avoid close contact with infected persons, wash hands frequently',
            'causes': 'Mumps virus spread through respiratory droplets and saliva',
            'risk_factors': 'Not vaccinated, crowded living conditions (dorms, barracks), weakened immune system, international travel',
            'info': 'Mumps is a contagious viral infection affecting salivary glands. Can cause complications like meningitis and infertility.'
        },
        {
            'name': 'Rubella',
            'symptoms': 'Mild fever, rash (starting on face, spreading to body), swollen lymph nodes, headache, pink eye, joint pain (especially in women)',
            'prevention': 'Get MMR vaccine (2 doses), avoid contact with infected persons during pregnancy, practice good hygiene, ensure vaccination before pregnancy',
            'causes': 'Rubella virus spread through respiratory droplets',
            'risk_factors': 'Not vaccinated, pregnancy (can cause birth defects), international travel, crowded environments',
            'info': 'Rubella (German measles) is usually mild but can cause severe birth defects if contracted during pregnancy.'
        },
        {
            'name': 'Whooping Cough',
            'symptoms': 'Severe coughing fits followed by whooping sound, runny nose, nasal congestion, red/watery eyes, fever, vomiting after coughing, extreme fatigue',
            'prevention': 'Get DTaP/Tdap vaccine (children and adults), avoid contact with infected persons, practice good hygiene, cover coughs, boost immune system, pregnant women should get Tdap',
            'causes': 'Bordetella pertussis bacteria spread through respiratory droplets',
            'risk_factors': 'Infants under 6 months, pregnant women, not fully vaccinated, close contact with infected person, weakened immune system',
            'info': 'Whooping cough (pertussis) is a highly contagious bacterial infection causing severe coughing. Dangerous for infants.'
        },
        {
            'name': 'Diphtheria',
            'symptoms': 'Thick gray coating in throat/nose, sore throat, fever, swollen lymph nodes, difficulty breathing/swallowing, bluish skin, drooling, hoarse voice',
            'prevention': 'Get DTaP/Tdap vaccine, avoid close contact with infected persons, practice good hygiene, ensure proper vaccination schedule, get booster shots',
            'causes': 'Corynebacterium diphtheriae bacteria spread through respiratory droplets',
            'risk_factors': 'Not vaccinated, crowded/unsanitary conditions, travel to endemic areas, weakened immune system',
            'info': 'Diphtheria is a serious bacterial infection affecting throat and airways. Vaccination has made it rare in developed countries.'
        },
        {
            'name': 'Tetanus',
            'symptoms': 'Jaw cramping (lockjaw), muscle stiffness (neck, abdomen, back), difficulty swallowing, painful muscle spasms, fever, sweating, rapid heart rate, high blood pressure',
            'prevention': 'Get DTaP/Tdap vaccine and boosters every 10 years, clean wounds thoroughly, seek medical care for deep/dirty wounds, avoid rusty objects, wear protective gear when working outdoors',
            'causes': 'Clostridium tetani bacteria entering through wounds, cuts, or punctures',
            'risk_factors': 'Not vaccinated, deep/contaminated wounds, diabetes, injection drug use, agricultural work, inadequate wound care',
            'info': 'Tetanus is a serious bacterial infection causing severe muscle spasms. Preventable through vaccination.'
        },
        {
            'name': 'Polio',
            'symptoms': 'Most cases asymptomatic, flu-like symptoms (fever, sore throat, headache, fatigue), stiff neck/back, muscle weakness, paralysis (in severe cases)',
            'prevention': 'Get polio vaccine (IPV - 4 doses), practice good hygiene, wash hands frequently, avoid contaminated water/food, ensure proper sanitation',
            'causes': 'Poliovirus spread through fecal-oral route (contaminated water/food)',
            'risk_factors': 'Not vaccinated, travel to endemic areas (Afghanistan, Pakistan), young children, weakened immune system, poor sanitation',
            'info': 'Polio is a viral infection that can cause paralysis. Nearly eradicated globally due to vaccination campaigns.'
        },
        {
            'name': 'Rabies',
            'symptoms': 'Fever, headache, nausea, vomiting, agitation, anxiety, confusion, hyperactivity, difficulty swallowing, excessive salivation, fear of water (hydrophobia), hallucinations, paralysis',
            'prevention': 'Vaccinate pets, avoid wild animals, do not approach stray animals, wash animal bites immediately, get post-exposure prophylaxis after animal bite, avoid areas with bat colonies',
            'causes': 'Rabies virus transmitted through saliva of infected animals (dogs, bats, raccoons) via bites or scratches',
            'risk_factors': 'Animal bite/scratch, travel to endemic areas, outdoor activities in wildlife areas, veterinarians, animal handlers, not vaccinating pets',
            'info': 'Rabies is a fatal viral disease affecting the nervous system. Post-exposure vaccination must start immediately after exposure.'
        },
        {
            'name': 'Zika Virus',
            'symptoms': 'Fever, rash, joint pain, red eyes, headache, muscle pain (most people have no symptoms or mild symptoms)',
            'prevention': 'Avoid mosquito bites (use repellent, wear long clothing, use mosquito nets), eliminate standing water, use condoms (virus in semen), delay travel to affected areas if pregnant, treat mosquito breeding sites',
            'causes': 'Zika virus transmitted by Aedes mosquitoes, sexual contact, or mother to child during pregnancy',
            'risk_factors': 'Pregnancy (can cause birth defects - microcephaly), travel to affected areas, unprotected sex with infected partner, living in tropical areas',
            'info': 'Zika is a mosquito-borne virus usually causing mild illness but can cause severe birth defects if contracted during pregnancy.'
        },
        {
            'name': 'Ebola',
            'symptoms': 'Fever, severe headache, muscle pain, weakness, fatigue, diarrhea, vomiting, abdominal pain, unexplained bleeding/bruising',
            'prevention': 'Avoid contact with infected persons/animals, practice proper hygiene, use protective equipment when caring for patients, avoid bush meat, follow safe burial practices, get vaccinated if high-risk',
            'causes': 'Ebola virus spread through direct contact with blood/body fluids of infected person or animal',
            'risk_factors': 'Healthcare workers, family members of infected persons, handling infected animals, travel to outbreak areas, unsafe burial practices',
            'info': 'Ebola is a severe, often fatal viral hemorrhagic fever. Early treatment improves survival rates.'
        },
        {
            'name': 'Lyme Disease',
            'symptoms': 'Bull\'s-eye rash (erythema migrans), fever, chills, fatigue, muscle/joint aches, swollen lymph nodes, later: severe joint pain, neurological problems, heart palpitations',
            'prevention': 'Use insect repellent (DEET), wear long clothing in wooded areas, check for ticks after outdoor activities, shower after being outdoors, landscape to reduce tick habitats, treat pets for ticks',
            'causes': 'Borrelia burgdorferi bacteria transmitted through blacklegged tick (deer tick) bites',
            'risk_factors': 'Outdoor activities in wooded/grassy areas, living in endemic areas (Northeast/Upper Midwest US), not using tick prevention',
            'info': 'Lyme disease is a tick-borne bacterial infection. Early antibiotic treatment prevents serious complications.'
        },
        {
            'name': 'West Nile Virus',
            'symptoms': 'Most cases asymptomatic, fever, headache, body aches, nausea, vomiting, rash, swollen lymph nodes, severe cases: high fever, neck stiffness, confusion, seizures, paralysis',
            'prevention': 'Use mosquito repellent, wear protective clothing, eliminate standing water, use screens on windows/doors, avoid outdoor activities at dusk/dawn, use mosquito nets',
            'causes': 'West Nile virus transmitted by infected mosquitoes (primarily Culex species)',
            'risk_factors': 'Age over 60, weakened immune system, chronic diseases, outdoor activities, living in areas with WNV activity',
            'info': 'West Nile virus is a mosquito-borne infection. Most people have mild symptoms, but elderly are at risk for severe disease.'
        },
        {
            'name': 'Yellow Fever',
            'symptoms': 'Fever, chills, headache, back/body pain, nausea, vomiting, fatigue, jaundice (yellow skin/eyes), bleeding, organ failure in severe cases',
            'prevention': 'Get yellow fever vaccine (required for travel to some countries), use mosquito repellent, wear protective clothing, eliminate breeding sites, avoid mosquito bites, use mosquito nets',
            'causes': 'Yellow fever virus transmitted by Aedes and Haemagogus mosquitoes',
            'risk_factors': 'Travel to endemic areas (tropical Africa, Central/South America), not vaccinated, outdoor activities in endemic areas',
            'info': 'Yellow fever is a serious viral disease transmitted by mosquitoes. Vaccination is highly effective and required for travel to many countries.'
        },
        {
            'name': 'Chikungunya',
            'symptoms': 'High fever, severe joint pain, muscle pain, headache, nausea, fatigue, rash, joint swelling (can last months)',
            'prevention': 'Avoid mosquito bites (repellent, protective clothing, nets), eliminate standing water, use air conditioning/window screens, treat water containers with larvicides',
            'causes': 'Chikungunya virus transmitted by Aedes aegypti and Aedes albopictus mosquitoes',
            'risk_factors': 'Travel to affected areas (Africa, Asia, Americas), outdoor activities, living in tropical areas, weakened immune system',
            'info': 'Chikungunya is a mosquito-borne viral disease causing severe joint pain that can persist for months or years.'
        },
        {
            'name': 'Meningitis',
            'symptoms': 'Sudden high fever, severe headache, stiff neck, nausea, vomiting, confusion, sensitivity to light, skin rash, seizures, drowsiness',
            'prevention': 'Get vaccinated (meningococcal, pneumococcal, Hib), avoid close contact with infected persons, practice good hygiene, do not share drinks/utensils, treat respiratory infections promptly',
            'causes': 'Bacterial (Neisseria meningitidis, Streptococcus pneumoniae), viral, or fungal infection of brain/spinal cord membranes',
            'risk_factors': 'Age (infants, teens, young adults), not vaccinated, crowded living (dorms, military), weakened immune system, travel to meningitis belt (sub-Saharan Africa)',
            'info': 'Meningitis is inflammation of brain and spinal cord membranes. Bacterial meningitis is life-threatening and requires immediate treatment.'
        },
        {
            'name': 'Encephalitis',
            'symptoms': 'Fever, headache, confusion, seizures, personality changes, weakness, difficulty speaking, hearing/vision problems, loss of consciousness',
            'prevention': 'Get vaccinated (Japanese encephalitis if traveling), avoid mosquito bites, practice good hygiene, get early treatment for infections, avoid tick bites',
            'causes': 'Viral infections (herpes simplex, West Nile, Japanese encephalitis), bacterial/fungal infections, autoimmune reactions',
            'risk_factors': 'Weakened immune system, age (very young, elderly), outdoor activities in endemic areas, not vaccinated, travel to affected regions',
            'info': 'Encephalitis is brain inflammation usually caused by viral infection. Can be life-threatening and requires immediate medical care.'
        },
        {
            'name': 'Sepsis',
            'symptoms': 'Fever or low temperature, rapid heart rate, rapid breathing, confusion, extreme pain/discomfort, clammy/sweaty skin, low blood pressure, decreased urination',
            'prevention': 'Prevent infections (vaccines, good hygiene), practice proper wound care, manage chronic conditions, seek early treatment for infections, maintain strong immune system',
            'causes': 'Body\'s overwhelming response to bacterial, viral, or fungal infection causing tissue damage and organ failure',
            'risk_factors': 'Very young or elderly, weakened immune system, chronic diseases, recent surgery/hospitalization, invasive devices (catheters), severe wounds/burns',
            'info': 'Sepsis is a life-threatening condition from body\'s response to infection. Requires immediate emergency treatment.'
        },
        {
            'name': 'COPD',
            'symptoms': 'Chronic cough, shortness of breath (especially during activities), wheezing, chest tightness, frequent respiratory infections, fatigue, unintended weight loss, swelling in ankles/feet/legs',
            'prevention': 'Do not smoke (or quit smoking), avoid secondhand smoke, avoid air pollution/chemical fumes, use protective equipment at work, prevent respiratory infections (vaccines, hygiene)',
            'causes': 'Long-term exposure to irritants (cigarette smoke, air pollution, chemical fumes, dust) causing lung damage',
            'risk_factors': 'Smoking (biggest risk), long-term exposure to air pollution, occupational exposure to dust/chemicals, age over 40, genetic factor (alpha-1 antitrypsin deficiency), asthma',
            'info': 'COPD (Chronic Obstructive Pulmonary Disease) is a progressive lung disease including emphysema and chronic bronchitis. Quitting smoking is crucial.'
        },
        {
            'name': 'Bronchitis',
            'symptoms': 'Persistent cough with mucus (clear, white, yellow, or green), chest discomfort, fatigue, shortness of breath, slight fever, chills, body aches',
            'prevention': 'Avoid smoking and secondhand smoke, practice good hygiene (wash hands), get vaccinated (flu, pneumonia), avoid air pollution, use humidifier, wear mask in dusty environments',
            'causes': 'Viral infections (same viruses causing colds/flu), bacterial infections, exposure to irritants (smoke, pollution, dust)',
            'risk_factors': 'Smoking, weakened immune system, exposure to irritants, gastric reflux, frequent exposure to colds/flu',
            'info': 'Bronchitis is inflammation of bronchial tubes. Acute bronchitis is common and resolves in weeks; chronic bronchitis is serious and part of COPD.'
        },
        {
            'name': 'Kidney Stones',
            'symptoms': 'Severe pain in side/back (below ribs), pain radiating to lower abdomen/groin, pain during urination, pink/red/brown urine, cloudy/foul-smelling urine, nausea, vomiting, frequent urination, fever if infected',
            'prevention': 'Drink plenty of water (8-12 cups daily), limit sodium (less than 2,300mg/day), reduce animal protein, limit oxalate-rich foods (spinach, nuts, tea), maintain healthy weight, get adequate calcium from food',
            'causes': 'Crystals forming in urine from high concentration of minerals (calcium, oxalate, uric acid)',
            'risk_factors': 'Dehydration, family/personal history, age 30-60, men more common, diet high in protein/sodium/sugar, obesity, digestive diseases, certain medications',
            'info': 'Kidney stones are hard mineral deposits forming in kidneys. Small stones may pass naturally; large stones may need medical intervention.'
        },
        {
            'name': 'Urinary Tract Infection',
            'symptoms': 'Strong, persistent urge to urinate, burning sensation during urination, frequent small amounts of urine, cloudy urine, strong-smelling urine, pelvic pain (women), rectal pain (men), blood in urine',
            'prevention': 'Drink plenty of water, urinate after intercourse, wipe front to back (women), avoid irritating feminine products, do not hold urine for long, take showers instead of baths, wear cotton underwear, avoid tight pants',
            'causes': 'Bacteria (usually E. coli) entering urinary tract through urethra',
            'risk_factors': 'Women (shorter urethra), sexual activity, certain birth control, menopause, urinary tract abnormalities, catheter use, weakened immune system, kidney stones',
            'info': 'UTI is a bacterial infection of urinary system. Common and usually responds well to antibiotics.'
        },
        {
            'name': 'Gastritis',
            'symptoms': 'Upper abdominal pain/discomfort, nausea, vomiting, feeling of fullness after eating, loss of appetite, bloating, heartburn, hiccups, black/tarry stools (if bleeding)',
            'prevention': 'Avoid NSAIDs or take with food, limit alcohol, quit smoking, manage stress, eat smaller meals, avoid spicy/acidic foods, treat H. pylori infection',
            'causes': 'H. pylori bacterial infection, excessive alcohol, chronic vomiting, stress, NSAIDs (aspirin, ibuprofen), autoimmune disorders',
            'risk_factors': 'H. pylori infection, regular NSAID use, excessive alcohol, smoking, stress, autoimmune diseases, age over 60, other infections',
            'info': 'Gastritis is stomach lining inflammation. Can be acute or chronic. Treatment depends on cause.'
        },
        {
            'name': 'Peptic Ulcer',
            'symptoms': 'Burning stomach pain, feeling of fullness/bloating, heartburn, nausea, fatty food intolerance, dark/black stools, vomiting blood, unexplained weight loss',
            'prevention': 'Avoid NSAIDs or take with food, limit alcohol, quit smoking, manage stress, treat H. pylori infection, eat regular meals, avoid spicy foods',
            'causes': 'H. pylori bacterial infection, long-term NSAID use damaging stomach/intestinal lining',
            'risk_factors': 'H. pylori infection, regular NSAID use, smoking, excessive alcohol, stress, spicy foods, family history, age over 50',
            'info': 'Peptic ulcers are open sores in stomach or upper small intestine lining. Treatable with medication.'
        },
        {
            'name': 'IBS',
            'symptoms': 'Abdominal pain/cramping, bloating, gas, diarrhea or constipation (or both), mucus in stool, symptoms triggered by certain foods/stress',
            'prevention': 'Identify and avoid trigger foods, eat high-fiber foods, drink plenty of water, exercise regularly, manage stress (yoga, meditation), get adequate sleep, eat smaller meals, keep food diary',
            'causes': 'Unknown exact cause; involves gut-brain interaction, intestinal muscle contractions, nervous system abnormalities, inflammation, infections, gut bacteria changes',
            'risk_factors': 'Age under 50, women, family history, anxiety/depression, history of abuse, stress',
            'info': 'IBS (Irritable Bowel Syndrome) is a chronic condition affecting large intestine. Managed through diet, lifestyle, and stress management.'
        },
        {
            'name': 'Crohn\'s Disease',
            'symptoms': 'Diarrhea, abdominal pain/cramping, blood in stool, fatigue, weight loss, reduced appetite, mouth sores, feeling that bowels are not empty, fever, perianal disease',
            'prevention': 'No known prevention, but manage symptoms by avoiding trigger foods, quit smoking, manage stress, take medications as prescribed, eat balanced diet, stay hydrated',
            'causes': 'Autoimmune disorder where immune system attacks digestive tract (exact cause unknown)',
            'risk_factors': 'Age under 30, family history, smoking, ethnicity (Ashkenazi Jewish descent), living in developed countries/urban areas, NSAID use',
            'info': 'Crohn\'s disease is a chronic inflammatory bowel disease affecting any part of digestive tract. Requires ongoing management.'
        },
        {
            'name': 'Ulcerative Colitis',
            'symptoms': 'Diarrhea with blood/pus, abdominal pain/cramping, rectal pain/bleeding, urgency to defecate, inability to defecate despite urgency, weight loss, fatigue, fever, failure to grow (children)',
            'prevention': 'No known prevention, but manage symptoms by avoiding trigger foods, manage stress, stay hydrated, take medications as prescribed, limit dairy, eat small meals',
            'causes': 'Autoimmune disorder causing chronic inflammation of colon and rectum (exact cause unknown)',
            'risk_factors': 'Age under 30, family history, ethnicity (Ashkenazi Jewish descent), isotretinoin (Accutane) use',
            'info': 'Ulcerative colitis is chronic inflammatory bowel disease causing inflammation and ulcers in colon and rectum. Increases colon cancer risk.'
        },
        {
            'name': 'Celiac Disease',
            'symptoms': 'Diarrhea, bloating, gas, fatigue, weight loss, anemia, bone/joint pain, skin rash (dermatitis herpetiformis), headaches, nausea, vomiting, constipation, failure to thrive (children)',
            'prevention': 'Strict gluten-free diet (avoid wheat, barley, rye), read food labels carefully, avoid cross-contamination, take vitamin/mineral supplements as needed, join support groups',
            'causes': 'Autoimmune disorder where gluten triggers immune system to attack small intestine',
            'risk_factors': 'Family history, Type 1 diabetes, autoimmune thyroid disease, Down syndrome, Turner syndrome, microscopic colitis',
            'info': 'Celiac disease is an autoimmune disorder triggered by gluten. Only treatment is strict lifelong gluten-free diet.'
        },
        {
            'name': 'Gallstones',
            'symptoms': 'Sudden severe pain in upper right abdomen, sudden pain in center of abdomen (below breastbone), back pain between shoulder blades, right shoulder pain, nausea, vomiting',
            'prevention': 'Maintain healthy weight, avoid rapid weight loss, eat regular meals, exercise regularly, eat high-fiber diet, limit high-fat/high-cholesterol foods, maintain healthy diet during weight loss',
            'causes': 'Hardened deposits of bile (too much cholesterol, bilirubin, or bile salts in gallbladder)',
            'risk_factors': 'Women, age over 40, obesity, rapid weight loss, high-fat diet, pregnancy, family history, diabetes, liver disease, certain medications',
            'info': 'Gallstones are hardened bile deposits in gallbladder. May cause no symptoms or severe pain requiring removal.'
        },
        {
            'name': 'Pancreatitis',
            'symptoms': 'Upper abdominal pain radiating to back, abdominal tenderness, nausea, vomiting, fever, rapid pulse, weight loss, oily stools (chronic)',
            'prevention': 'Limit alcohol or abstain, quit smoking, maintain healthy weight, eat low-fat diet, drink plenty of fluids, avoid medications that can trigger pancreatitis, treat gallstones',
            'causes': 'Gallstones, chronic alcohol use, certain medications, high triglycerides, abdominal surgery, infections',
            'risk_factors': 'Excessive alcohol, smoking, obesity, diabetes, family history, high triglycerides, abdominal injury, pancreatic cancer',
            'info': 'Pancreatitis is pancreas inflammation. Acute pancreatitis is sudden; chronic pancreatitis causes permanent damage.'
        },
        {
            'name': 'Liver Cirrhosis',
            'symptoms': 'Fatigue, easy bruising/bleeding, loss of appetite, nausea, swelling in legs/feet/abdomen, weight loss, itchy skin, yellow skin/eyes (jaundice), confusion, drowsiness, spider-like blood vessels',
            'prevention': 'Limit alcohol or abstain, maintain healthy weight, eat balanced diet, protect from hepatitis (vaccines, safe sex), avoid sharing needles, limit exposure to chemicals, manage underlying conditions',
            'causes': 'Chronic alcohol abuse, chronic viral hepatitis (B, C), fatty liver disease, iron/copper buildup, autoimmune diseases, bile duct damage',
            'risk_factors': 'Excessive alcohol, chronic hepatitis, obesity, diabetes, shared needles, unprotected sex, exposure to toxic chemicals',
            'info': 'Cirrhosis is late-stage liver scarring from various liver diseases. Damage is permanent but progression can be slowed.'
        },
        {
            'name': 'Rheumatoid Arthritis',
            'symptoms': 'Joint pain/swelling/stiffness (especially hands, feet), morning stiffness lasting hours, fatigue, fever, weight loss, symmetrical joint involvement, rheumatoid nodules',
            'prevention': 'No known prevention, but reduce risk by not smoking, maintain healthy weight, limit alcohol, manage stress, exercise regularly, eat anti-inflammatory diet',
            'causes': 'Autoimmune disorder where immune system attacks joint linings (exact cause unknown)',
            'risk_factors': 'Women, age 40-60, family history, smoking, obesity, environmental exposures',
            'info': 'Rheumatoid arthritis is chronic autoimmune disease causing joint inflammation. Can affect other organs. Early treatment prevents joint damage.'
        },
        {
            'name': 'Osteoarthritis',
            'symptoms': 'Joint pain during/after movement, stiffness after inactivity, tenderness, loss of flexibility, grating sensation, bone spurs, swelling',
            'prevention': 'Maintain healthy weight, exercise regularly, avoid joint injuries, use proper posture, avoid repetitive stress, strengthen muscles around joints, eat balanced diet rich in vitamin D and calcium',
            'causes': 'Cartilage breakdown in joints from aging, wear and tear, injury',
            'risk_factors': 'Age, obesity, joint injuries, repetitive stress, genetics, bone deformities, certain metabolic diseases',
            'info': 'Osteoarthritis is most common arthritis from joint cartilage breakdown. Managed with lifestyle changes, medications, and sometimes surgery.'
        },
        {
            'name': 'Gout',
            'symptoms': 'Severe joint pain (often big toe), lingering discomfort after attack, inflammation/redness, limited range of motion in affected joints',
            'prevention': 'Limit alcohol, limit high-purine foods (red meat, organ meat, seafood), drink plenty of water, maintain healthy weight, eat low-fat dairy, eat complex carbs, limit sugary foods/drinks',
            'causes': 'High uric acid levels forming sharp crystals in joints',
            'risk_factors': 'High-purine diet, alcohol, obesity, medical conditions (hypertension, diabetes, kidney disease), family history, age/sex (men, postmenopausal women), certain medications',
            'info': 'Gout is inflammatory arthritis from uric acid crystals in joints. Managed with diet, medication, and lifestyle changes.'
        },
        {
            'name': 'Lupus',
            'symptoms': 'Fatigue, fever, joint pain/stiffness/swelling, butterfly-shaped rash on face, skin lesions, fingers/toes turning white/blue in cold, shortness of breath, chest pain, dry eyes, headaches, confusion, memory loss',
            'prevention': 'No known prevention, but manage symptoms by avoiding sun exposure, taking medications as prescribed, getting adequate rest, exercising regularly, not smoking, eating healthy diet, managing stress',
            'causes': 'Autoimmune disorder where immune system attacks own tissues (exact cause unknown - likely genetic and environmental factors)',
            'risk_factors': 'Women, age 15-45, ethnicity (African American, Hispanic, Asian), family history, certain medications',
            'info': 'Lupus (SLE) is chronic autoimmune disease affecting multiple organs. Symptoms vary greatly. Managed with medications and lifestyle.'
        },
        {
            'name': 'Psoriasis',
            'symptoms': 'Red patches covered with thick silvery scales, dry/cracked skin that may bleed, itching/burning/soreness, thickened/pitted nails, swollen/stiff joints',
            'prevention': 'No known prevention, but manage symptoms by moisturizing skin, avoiding triggers (stress, infections, skin injuries), not smoking, limiting alcohol, maintaining healthy weight, managing stress',
            'causes': 'Immune system problem causing skin cell production to speed up (exact cause unknown - genetic and environmental triggers)',
            'risk_factors': 'Family history, viral/bacterial infections, stress, smoking, obesity, vitamin D deficiency',
            'info': 'Psoriasis is chronic autoimmune condition causing rapid skin cell buildup. Can affect joints (psoriatic arthritis). Managed with topical treatments, medications, and light therapy.'
        },
        {
            'name': 'Eczema',
            'symptoms': 'Dry/sensitive skin, red/inflamed skin, intense itching, dark patches, rough/leathery/scaly patches, oozing/crusting, swelling',
            'prevention': 'Moisturize regularly (especially after bathing), avoid harsh soaps/detergents, take warm (not hot) showers, avoid triggers (stress, certain fabrics, fragrances), use humidifier, avoid scratching, wear soft breathable fabrics',
            'causes': 'Combination of genetic and environmental factors affecting skin\'s ability to retain moisture and protect from bacteria/allergens/irritants',
            'risk_factors': 'Family history of eczema/allergies/asthma, living in developed countries/cold climates/urban areas',
            'info': 'Eczema (atopic dermatitis) is chronic condition causing inflamed, itchy skin. Often starts in childhood. Managed with moisturizers, medications, and avoiding triggers.'
        },
        {
            'name': 'Hypothyroidism',
            'symptoms': 'Fatigue, weight gain, cold intolerance, constipation, dry skin, thinning hair, slow heart rate, depression, impaired memory, muscle weakness, elevated cholesterol, puffy face',
            'prevention': 'No known prevention, but ensure adequate iodine intake, manage selenium levels, treat autoimmune conditions, avoid excess soy products, get regular thyroid screening if at risk',
            'causes': 'Autoimmune disease (Hashimoto\'s thyroiditis), thyroid surgery, radiation therapy, certain medications, iodine deficiency',
            'risk_factors': 'Women, age over 60, family history, autoimmune disease, radiation therapy to neck, pregnancy, certain medications',
            'info': 'Hypothyroidism is underactive thyroid gland producing insufficient hormones. Managed with daily hormone replacement medication.'
        },
        {
            'name': 'Hyperthyroidism',
            'symptoms': 'Weight loss despite good appetite, rapid/irregular heartbeat, nervousness/anxiety/irritability, tremor, sweating, heat intolerance, frequent bowel movements, enlarged thyroid (goiter), fatigue, muscle weakness, difficulty sleeping',
            'prevention': 'No known prevention, but manage risk by ensuring adequate but not excessive iodine, avoid smoking, manage stress, get regular checkups if at risk',
            'causes': 'Graves\' disease (autoimmune), thyroid nodules, thyroiditis, excessive iodine, too much thyroid medication',
            'risk_factors': 'Family history, women, age 20-40, other autoimmune conditions, smoking, recent pregnancy, excessive iodine intake',
            'info': 'Hyperthyroidism is overactive thyroid producing too much hormone. Treated with medications, radioactive iodine, or surgery.'
        },
        {
            'name': 'Anemia',
            'symptoms': 'Fatigue, weakness, pale/yellowish skin, irregular heartbeat, shortness of breath, dizziness/lightheadedness, chest pain, cold hands/feet, headaches, brittle nails',
            'prevention': 'Eat iron-rich foods (red meat, beans, dark leafy greens), eat vitamin C-rich foods (enhances iron absorption), ensure adequate vitamin B12 and folate, treat underlying conditions, avoid excessive tea/coffee with meals',
            'causes': 'Iron deficiency, vitamin B12/folate deficiency, chronic diseases, blood loss, bone marrow problems, hemolysis',
            'risk_factors': 'Poor diet, intestinal disorders, menstruation, pregnancy, chronic conditions, family history, certain medications',
            'info': 'Anemia is condition with insufficient healthy red blood cells to carry adequate oxygen. Treatment depends on cause.'
        },
        {
            'name': 'Osteoporosis',
            'symptoms': 'Often no symptoms until fracture occurs, back pain from fractured vertebra, loss of height, stooped posture, bone fractures occurring more easily than expected',
            'prevention': 'Get adequate calcium (1,000-1,200mg daily), ensure sufficient vitamin D (600-800 IU daily), exercise regularly (weight-bearing, strength training), avoid smoking, limit alcohol, maintain healthy weight, prevent falls',
            'causes': 'Decreased bone density and strength from aging, hormonal changes, nutritional deficiencies',
            'risk_factors': 'Age, women (especially post-menopause), family history, small body frame, low calcium/vitamin D, sedentary lifestyle, smoking, excessive alcohol, certain medications',
            'info': 'Osteoporosis causes bones to become weak and brittle. Often called "silent disease" as it progresses without symptoms until fracture occurs.'
        }
    ]
    
    # Insert disease data
    for disease in diseases:
        cursor.execute('''
            INSERT INTO diseases (name, symptoms, prevention, causes, risk_factors, info)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (disease['name'], disease['symptoms'], disease['prevention'], 
              disease['causes'], disease['risk_factors'], disease['info']))
    
    conn.commit()
    conn.close()
    print(f"✅ Database initialized successfully with {len(diseases)} diseases!")
    print("\nDisease list:")
    for i, disease in enumerate(diseases, 1):
        print(f"{i}. {disease['name']}")

if __name__ == '__main__':
    init_database()