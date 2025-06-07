from memory_profiler import profile
"""
  0 1 2 3 4 5 6 7 8 9 
0 * * * * * * * * * * 0
1 * * * * * * * * * * 1
2 *                   2
3 *                   3
4 * * * * *           4
5 * * * * *           5
6 *                   6
7 *                   7
8 * * * * * * * * * * 8
9 * * * * * * * * * * 9
  0 1 2 3 4 5 6 7 8 9
"""
@profile
def grid():
    gird = [[" " for i in range(10)]for i in range(10)]
    for i in range(len(gird)):
        for j in range(len(gird)):
            if i == 1 or i == 9 or i == 0 or i == 8:
                gird[i][j] = "*"
            elif (i == 4 and (j <= 4 and j > 0)) or (i == 5 and (j <= 4 and j > 0)):
                gird[i][j] = "*"
            elif (j == 0 or j == 1):
                gird[i][j] = "*"
            
    for i in range(len(gird)):
        for j in range(len(gird)):
            print(gird[i][j], end=" ")
        print("")
        
grid()