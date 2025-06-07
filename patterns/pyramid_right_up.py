#goal is to print the below star pattern
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
'''

n = 5

for c in range(0,5):
    for r in range(c+1):
        print(f"*  ",end='')
    print()