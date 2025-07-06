from random import shuffle as su
def rand():
    c = []
    # for i in range(65, 91):
    #     c.append(chr(i))
        
    for i in range(32, 127):
        c.append(chr(i))
    su(c)
    return c

def cool():
    c = rand()

    s = input("Enter any String: ")
    e = ""

    for i in s:
        su(c)
        for j in c:
            if i == j:
                e+=j
                print(e)
                break
            else:
                print(e+j)
                
def main():
    cool()
    
if __name__ == main():
    main()