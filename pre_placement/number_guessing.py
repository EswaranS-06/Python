import time
import random

p1 = input("Enter the Player 1 Name: ")
p2 = input("Enter the Player 2 Name: ")

print(f"Hello {p1} and {p2} wait for computer to choose number between [1-10]")
num_list = []
time.sleep(5)
while len(num_list) != 5:
    d = random.randint(1,11)
    if d not in num_list:
        num_list.append(d)
    else:
        continue
p1g = []
p2g = []
s1=0
s2=0
p1s = 0
p2s = 0
c = 0
n = 3
print("Enter your Guess between [1-10]")
for i in range(n):
    
    #player One
    guess = int(input(f"[{p1}] your guess:- "))
    if guess in p1g or guess in p2g:
        print(f"{guess} is already Guessed")
        n = n +1
    else:
        if guess in num_list:
            p1g.append(guess)
            s1+=1
            c+=1
            print(f'Yes, [{p1}] as guessed "Right"')
        else:
            p2g.append(guess)
            c+=1
            print(f'No, [{p1}] as guessed "Wrong"')
    
    #player Two        
    guess1 = int(input(f"[{p2}] your guess:- "))
    if guess in p1g or guess in p2g:
        print(f"{guess1} is already Guessed")
        n = n + 1
    else:
        if guess1 in num_list:
            p2g.append(guess1)
            s2+=1
            c+=1
            print(f'Yes, [{p2}] as guessed "Right"')
        else:
            p2g.append(guess1)
            c+=1
            print(f'No, [{p2}] as guessed "Wrong"')
            

print(f'''
      
Computer guessings are {num_list}
-----------------------------------\n
{p1}:
    Number guess {p1g},
    Score {s1}/3
------------------------------- \n  
{p2}:
    Number guess {p2g},
    Score {s2}/3
------------------------------- \n
Game Result:
    [{p1 if s1 > s2 else p2}] <----- Won the Game 
      ''')
            
    