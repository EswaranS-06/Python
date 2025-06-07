def main():
    n = 9474 #input("Enter the number: ")
    for i in range(1,int(n)+1):
        armstrong(str(i))

def armstrong(str_num):
    #str_num = input('Enter the number: ')
    if not str_num.isdigit() or int(str_num) < 1:
        print(f"{str_num} is an Invalid,\n Enter only Postive Numbers")
        return 0
    else:
        arm_value = 0
        len_str = len(str_num)
        for i in str_num:
            arm_value += int(i)**len_str    
        if arm_value == int(str_num):
            print(f"Yes, {arm_value} is an Armstrong number.")  
        #print(f"Yes, {arm_value} is an Armstrong number." if arm_value == int(str_num) else f"No, {str_num} is not an Armstrong number.")

if __name__ == "__main__":
    main()