import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[^A-Za-z0-9]', password))
    
    strength = 0
    feedback = []
    
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
        
    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
        
    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    strength_feedback = {
        5: "Very strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very weak",
        0: "Extremely weak"
    }
    
    return {
        "strength": strength_feedback[strength],
        "feedback": feedback
    }

# Ask for user input
password = input("Enter your password: ")
result = assess_password_strength(password)
print(f"Password strength: {result['strength']}")
print("Feedback:")
for item in result['feedback']:
    print(f"- {item}")
