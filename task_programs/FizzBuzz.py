num = 20#int(input('Enter the number: '))

if num < 1:
    print(f'{num} is an Ivalid Number')
else:
    for i in range(1,num+1):
        if i%3 == 0 and i%5 == 0:
            print(f"FizzBuzz({i})")
        elif i%3 == 0:
            print(f"Fizz({i})")
        elif i%5 == 0:
            print(f"Buzz({i})")
        else:
            print(i)