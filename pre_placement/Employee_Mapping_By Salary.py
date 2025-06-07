names = ["A",'B','C','D','E','F','G','H','I','J']
salary = [10000,20000,12000,55000,45000,20000,26000,60000,17000,25000]
memo = [0,1,1,1,2,3,2,0,2,2]

#ziping
emp = [[j,k,i] for i, j, k in zip(names, salary, memo)]

#sorting
emp = sorted(emp, reverse=True)

#Sorting High Salary
dis = [i for i in emp if i[0] >= 40000]
 
#Sorting Memo more than 2      
dis.extend(i for i in emp if  i[1] >= 2 and i[2] not in dis)    

#Displaying the Top 5  
print(' Name, Salary,Memo')        
for i in range(5):  
    print(f'{i+1}. {dis[i][2]} , {str(dis[i][0])} , {dis[i][1]}')