def calculate_averages(students): 
    
    return { name:round(sum(grades)/len(grades),2) for name,grades in students.items()}
    
    """for x, y in students.items():
        
        temp = sum(y)/len(y) 
        
        dictAG.update({x:round(temp),2})""" # 👈🏽 this is converted into this 👇🏽 as a list comperhenison(LC)
                            #     < this 👇🏽 sum the list and divide it with  👇🏽  the len of the list for average >
    """student_average_grade = { name:round(sum(grades)/len(grades),2) for name,grades in students.items()} #👈🏽 (LC) find average and save dict with its name
    
    return student_average_grade"""

def filter_high_achievers(students, threshold):
    
    return { name: grade for name, grade in students.items() if grade>=threshold}
    
    """for name, grade in students.items():
        
        if grade >= threshold :
            
            threshold_students.update({name : grade})
            print(threshold_students)"""
            
    """threshold_students = { name: grade for name, grade in students.items() if grade>=threshold}
    return threshold_students"""
    



#students names and grades as a dict
students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 60, 75],
    "Charlie": [92, 88, 94]
}

threshold = 80
#assging the def return to the average
averages = calculate_averages(students)
high_achievers = filter_high_achievers(averages, threshold)

print(averages)
print(high_achievers)