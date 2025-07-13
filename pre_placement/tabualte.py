from tabulate import tabulate
h = ['Name', 'Age', 'Department']

data = [['Name', 'Age', 'Department'],['Ravi',25,'HR'],['Anjali',35,'Finance']]

print(tabulate(data, tablefmt='fancy_grid'))
'''
for i in data:
    print(f'|{i[0]:<20}|{i[1]:<4}|{i[2]:<10}|\n-------------------------------------')'''