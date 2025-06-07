password = "E$w@r@n$27"
lst = [True, False, True]
hasLetters = any( lst)
hasDigits = any( char.isdigit() for char in password )
hasSpecial = any(not char.isalnum() for char in password)
password_len = len(password)