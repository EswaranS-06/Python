def printv(): print("Hello")

def main():
    print('Enter your 5 subjects marks')

    a=int(input("Enter your mark: "))
    b=int(input("Enter your mark: "))
    c=int(input("Enter your mark: "))
    d=int(input("Enter your mark: "))
    e=int(input("Enter your mark: "))

    x = lambda a,b,c,d,e: (a+b+c+d+e)/5

    print(x(a,b,c,d,e))
    printv()

if __name__ == "__main__":
    main()