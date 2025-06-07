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


n = int(input('Enter the grid value: '))

for j in range(0,n+1):
    print('\n',j,"|",end='')
    for i in range(1,n+1):
        if j == 0:
            print("\t",i,end='')
        else:
            print("\t",i*j,end="")
    if j == 0:
        print("\n","---------"*n)
    print("\n   |",end='')
    