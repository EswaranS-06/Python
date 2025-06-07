#goal is to print the below star pattern
'''
*  *  *  *  *
*  *  *  *
*  *  *
*  *  
*  
'''

n = 5

for c in range(0,n):
    for r in range(c,n):
        print(f"*",end='')
    print()