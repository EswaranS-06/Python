#CLI looping format
def loop():
    while True:
        NumLoop()
        print("\n_________________________________NEXT LOOP STARTED__________________________________________\n")


def NumLoop():
    loopValue = int(input("Enter the number range: "))
    print("    Not Prime No    |       Prie Number      ")

    for i in range(2,loopValue):
       
        IsPrime(i)
        #print("                    |                 ")

    #print(f" From 2 to {loopValue} \n There is ___ prime numbers and ____ normal numbers")
  
def IsPrime(num):
    #num = int(input('Enter The Number: '))
    if num <= 1:
        print(f"\t{num}")

    else:
        for i in range(2,num):
            if num%i == 0:
                print(f"\t{num}          |")
                break
        else :
            print(f"\t\t    |\t\t{num}")


loop()