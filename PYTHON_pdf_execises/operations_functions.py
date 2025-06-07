#1. Write a program to add two number.
def add(a, b):
    return a+b

#2. Write a python program to find square root.
def square_root(a, b):
    return a**b 

#3. Write a python program to calculate area of triangle.
#               S=(a+b+c)/2
#   Formula for Area:
#   Area =√(s ∗ (s − a) ∗ (s − b) ∗ (s − c))
def triangle_area(a, b, c):
    s = (a+b+c)/2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

#4. Write a python program to calculate simple interest and compound interest.
#                   SI=PNR/100
#                 CI=P(1+R/100)n
def simple_interest(p, n, r):
    return (p*n*r)/100

def compound_interest(p, n, r):
    return p*(1+r)**n

#5. Write a python program to convert Celsius to Fahrenheit.
#                  F=C*9/5+32
def CelsiusToFahrenheit(c):
    return c*(9/5)+32

#6. Write a python program to convert Fahrenheit to Celsius.
#                C=(F-32)*5/9
def FahrenheitToCelsius(f):
    return (f-32)*(5/9)

#7. Write a python program to swap two variable values using temp variable
def temp_swap(a, b):
    temp = a
    a = b
    b = temp
    return temp
#8. Write a python program to swap two variable values without using temp variable
def swap(a, b):
    a, b = b, a
    return a, b

#TestCases
def main():
    print('''
          1. Add two numbers
          2. Find square root
          3. Calculate area of triangle
          4. Calculate simple interest 
          5. Calculate compound interest
          6. Convert Celsius to Fahrenheit
          7. Convert Fahrenheit to Celsius
          8. Swap two variable values using temp variable
          9. Swap two variable values without using temp variable
          0. Exit
          ''')

    while True:
        c = int(input("Enter Your Choice: "))
        
        if c == 0:
            print("Exiting program.")
            break
        
        elif c == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Sum is:", add(a, b))
        
        elif c == 2:
            a = float(input("Enter number: "))
            print("Square root is:", square_root(a, 0.5))
        
        elif c == 3:
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c_ = float(input("Enter side c: "))
            print("Area of triangle is:", triangle_area(a, b, c_))
        
        elif c == 4:
            p = float(input("Enter principal amount: "))
            n = float(input("Enter time (years): "))
            r = float(input("Enter rate of interest: "))
            print("Simple Interest is:", simple_interest(p, n, r))
        
        elif c == 5:
            p = float(input("Enter principal amount: "))
            n = float(input("Enter time (years): "))
            r = float(input("Enter rate of interest: "))
            print("Compound Interest is:", compound_interest(p, n, r))
        
        elif c == 6:
            celsius = float(input("Enter temperature in Celsius: "))
            print("Fahrenheit:", CelsiusToFahrenheit(celsius))
        
        elif c == 7:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Celsius:", FahrenheitToCelsius(fahrenheit))
        
        elif c == 8:
            a = input("Enter value of a: ")
            b = input("Enter value of b: ")
            temp = a
            a = b
            b = temp
            print("Values after swapping using temp variable:")
            print("a =", a, "b =", b)
        
        elif c == 9:
            a = input("Enter value of a: ")
            b = input("Enter value of b: ")
            a, b = swap(a, b)
            print("Values after swapping without using temp variable:")
            print("a =", a, "b =", b)
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()