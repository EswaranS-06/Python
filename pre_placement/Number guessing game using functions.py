#Number guessing game using functions
import random
import time

def guessing(player, guess_list, p1g, p2g, score, player_guess):
    while True:
        pg = int(input(f"\n______________________________________\n\nEnter your Guess(1-10)\n\n Player --> [{player}]  :"))
        if pg in p1g or pg in  p2g:
            print(f"This number is Already guessed: [{pg}] ")
            continue
        else:
            if pg in guess_list:
                print(f'\tYes, [{player}] as guessed "[{pg}]" is "Right"')
                player_guess.append(pg)
                score+=1
                return player_guess, score
                
            else:
                print(f'\tNo,  [{player}] as guessed "[{pg}]" is "Wrong"')
                player_guess.append(pg)
                return player_guess, score


def main():
    p1 = input("Enter the Player 1 Name: ")
    p2 = input("Enter the Player 2 Name: ")

    print(f"Hello {p1} and {p2} wait for computer to choose number between [1-10]")
    time.sleep(2)
    print("Wait for some times")
    time.sleep(2)

    score1 = 0
    score2 = 0
    guess_lst = []
    p1g = []
    p2g = []

    while len(guess_lst)<5:
        d = random.randint(1,10)
        if d in guess_lst:
            continue
        else:
            guess_lst.append(d)

    #print(guess_lst)

    for i in range(3):
        p1g, score1 = guessing(p1, guess_lst, p1g, p2g, score1, p1g)
        time.sleep(1)
        p2g, score2 = guessing(p2, guess_lst, p1g, p2g, score2, p1g)
        time.sleep(1)
        
    print("______________________________________")
    print(f'''
        
    Computer guessings are {guess_lst}
    -----------------------------------\n
    {p1}:
        Number guess {p1g},
        Score {score1}/3
    ------------------------------- \n  
    {p2}:
        Number guess {p2g},
        Score {score2}/3
    ------------------------------- \n
    Game Result:
        [{"Draw" if score1 == score2 else p2 if score2 > score1 else p1}] <----- Won the Game 
        
    ''')
    
    print("Next game begin:- \n\n\n")
    
if __name__ == "__main__":
    main()