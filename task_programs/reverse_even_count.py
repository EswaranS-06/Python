def loop():
    while True:
        rec()

def rec():
    num = input('Enter the Number: ')

    if int(num) < 1:
        print(f"{num} is an Invalid Value, \n Value must be Postive Number\n")
        return 0

    r_num = num[::-1]
    print(f"Reversed Number: {r_num}")

    even_count = 0

    for i in r_num:
        if int(i)%2 == 0:
            even_count += 1

    print(f"Count of Even Digits:{even_count}\n")

loop()
