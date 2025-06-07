class employee:
    company = "Gooogle"
    company_profit = 1000000
    def __init__(self, name, age, salary, tax_percentage, share_percentage):
        self.name = name
        self.age = age 
        self.salary = salary
        self.tp = tax_percentage
        self.sp = share_percentage
        
        
    def tax_cal(self):
        #p = self.tp/100
        self.tax =  self.salary * self.tp/100
        
    def share_cal(self):
        #p = self.sp/100
        self.share = self.company_profit * self.sp/100
        
    def dis_info(self):
        print(f'''
              ------------{employee.company}-------------\n
              Name: {self.name}
              Age: {self.age}
              Salary: {self.salary}
              Tax to Pay: {self.tax_cal()}
              Share From Company: {self.share_cal()}
              ---------------------------------------\n
              ''')
        
emp1 = employee('Rex',25,100000,10,20)
emp2 = employee('Ray',26,200000,12,25)
emp1.dis_info()
emp2.dis_info()
