def loop():
    while True:
        armstrong()


def armstrong():
    str_num = input('Enter the number: ')
    if not str_num.isdigit or int(str_num) < 1:
        print(f"{str_num} is an Invalid,\n Enter only Postive Numbers")
        return 0
    else:
        arm_value = 0
        len_str = len(str_num)
        for i in str_num:
            arm_value += int(i)**len_str        
        print(f"Yes, {arm_value} is an Armstrong number." if arm_value == int(str_num) else f"No, {str_num} is not an Armstrong number.")

loop()