name, age, city = "Eswaran", 19, "Chennai"
print("I am "+name+" and ",age ," years old, I am From "+city)

x,y,z=int(input("Enter Num 1: ")), int(input("Enter Num 2: ")), int(input("Enter Num 3: "))
print(x*y*z)

num, name, bool1, flt = 19, "Name:-", True, 2.5
print(f"Integer: {num}\nString: {name}\nBoolean: {bool1}\nFloat: {flt}")

l,b=int(input("Enter Length: ")), int(input("Enter breath: ")) 
print("Area is ",l*b)

a=int(input("Enter Square Length: "))
print("Area of the Square is ",a)

r=int(input("Enter Radius: "))
print("Area of Circal is ",3.14*r*r)

p,n,r=int(input("Enter Principal: ")),int(input("Enter No of Years: ")),int(input("Enter Rate of Interest: "))
print("The simple interest is ",(p*n*r)/100)

c=int(input("Enter Celsius: "))
print("The Fahrenheit is",c*(9/5)+32)

h, w=int(input("Enter Height: ")),int(input("Enter Weight: "))
print("BMI: ",w/h**h)