#goal is to print the below star pattern
'''
            *  
         *  *  
      *  *  *  
   *  *  *  *  
*  *  *  *  *  
'''

n = 5

for j in range(0,n+1):
   print(" "*(2*(n - j))+"* "*j)