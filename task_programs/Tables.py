def loop():
    while True:
        tables()
        print("_________________________________________\n")

def tables():
    
    value = int(input('Enter the Table Value: '))
    times = int(input('Enter the No of Times to run: '))

    lenght = (value*times)+1

    for i in range(value, lenght, value):
        print(f'{value} x {i//value} = {i}')

    


loop()