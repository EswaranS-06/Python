def passwordStrengthChecker(password):
    
    hasLetters = any( char.isalpha() for char in password)
    hasDigits = any( char.isdigit() for char in password )
    hasSpecial = any(not char.isalnum() for char in password)
    password_len = len(password)
    
    if ( password_len <= 6 or (hasLetters or hasDigits or hasSpecial)):
        return "Weak"
    
    elif ( password_len >6 and hasLetters and hasDigits and hasSpecial):
        return "Strong"
    
    elif( password_len <= 6 and hasLetters and hasDigits):
        return "Moderate"
    
    
while True:
    password = input("Enter Your password to check its Strength: ")

    print(f" Strength: {passwordStrengthChecker(password)}") 