from tabulate import tabulate
h = ['Name', 'Age', 'Department']

data = [['Name', 'Age', 'Department'],['Ravi',25,'HR'],['Anjali',35,'Finance']]

print(tabulate(data, headers=h, tablefmt='fancy_grid'))
table = tabulate(data, headers=h, tablefmt='grid')

with open('pf/tabulate.txt', 'w') as file:
    file.write(table)
    
print("Okay!!!")