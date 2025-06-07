#In this our goal is to get this output format
'''
    1   2   3   4   5
  ---------------------
1 | 1   2   3   4   5
2 | 2   4   6   8  10
3 | 3   6   9  12  15
4 | 4   8  12  16  20
5 | 5  10  15  20  25

'''


start_value = int(input('Enter the grid value: '))
stop_value = int(input('Enter the grid value: '))

for j in range(start_value,stop_value+1):
    print('\n',j,"|",end='')
    for i in range(start_value,stop_value+1):
        if j == start_value:
            print("\t",i,end='')
        else:
            print("\t",i*j,end="")
    if j == start_value:
        print("\n","---------"*stop_value)
    print("\n   |",end='')
    