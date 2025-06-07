from random import randint
"""def number_guessing():
    try:
        int_to_guess = randint(1,100)
        count = 0
        guess = int(input("Guess the number between 1 and 100:"))

        while guess != int_to_guess :
            if guess == 0:
                exit() # for testing
            elif not 0 < guess <101 :
                count += 1
                guess = int(input("Invalid Input must be between 1 to 100!!!\n\nGuess the number: "))
                
            elif guess > int_to_guess:
                count += 1
                guess = int(input("\n\tToo High! 🔺\n\nGuess the number: "))
                
            elif guess < int_to_guess:
                count += 1
                guess = int(input("\n\tToo Low! 🔻\n\nGuess the number: "))
            
        else:
            print(f"Correct! You guessed it in {count} tries.")
                
    except ValueError:
        print("Invalid Input must be between 1 to 100 \n\n!!!   ONLY NUMBER   !!!\n")
        number_guessing()
        
number_guessing()
"""
try :
    def guess_input():
        global count, guess
        count += 1
        guess = int(input("\nGuess the number: "))
    count, int_to_guess, guess = 0, randint(1,100), int(input("Guess the number between 1 and 100:"))
    
    while True:
        if not 0 <guess<100 :
            print("Invalid Input must be between 1 to 100!!!")
            guess_input()
        elif guess > int_to_guess:
            print("\n\tToo High! 🔺")
            guess_input()
        elif guess < int_to_guess:
            print("\n\tToo Low! 🔻")
            guess_input()
        else :
            count += 1
            print(f"Correct! You guessed it in {count} tries.")
            exit()
        
except ValueError:
    print("Invaid Input \n!!!    ONLYY NUMBERS   !!!")