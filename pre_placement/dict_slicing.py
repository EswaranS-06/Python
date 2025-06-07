stu = [
    {'name':'Gokul', 'marks':[10,20,30,90,50]},
    {'name':'Raj', 'marks':[50,20,80,40,50]},
    {'name':'Roy', 'marks':[10,90,30,40,58]}
]

stu

for i in range(len(stu)):
    #avg =len(stu[i]['marks'])-sum(stu[i]['marks'])
    print(stu[i]['name'],(sum(stu[i]['marks'])/500)*100)