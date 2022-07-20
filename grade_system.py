import math

def main():
    midterm = int(input("Enter grade on midterm: "))
    final = int(input("Enter grade on final exam: "))
    
    average = (midterm + final + final)/3
    average = math.ceil(average)
    
    grade=semesterGrade(average)
    print("Semeter Grade:",grade)

def semesterGrade(average):

    if average>= 90 :
        grade = 'A'
        
    elif average>= 80 :
        grade = 'B'
        
    elif average>= 70:
        grade = 'C'
        
    elif average>= 60 :
        grade = 'D'
        
    else:
        grade = 'F'   

    return grade

main()

 
    
