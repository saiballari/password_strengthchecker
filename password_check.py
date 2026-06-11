import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Very Strong Password"
    elif score == 4:
        return "Strong Password"
    elif score == 3:
        return "Medium Password"
    elif score == 2:
        return "Weak Password"
    else:
        return "Very Weak Password"

password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)