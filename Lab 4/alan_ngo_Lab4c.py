#Alan Ngo
#variables
newStudent='y'
count=0
gradeTotal = 0
classAverage = 0
#while loop
while newStudent=="y":
    total=0.0
    name=input("Enter student's name: ")
    numTest=int(input("How many tests?"))
    print("Name", name)
    print("______________________________")
    for tests in range(numTest):
        print("Test number", tests+1)
        score=float(input("Enter score: "))
#sentinel
        if score<0:
            print("Enter a POSITIVE score")
            exit()
        total+=score
        studentAverage=0.0
        studentAverage=total/numTest
    #grade conversion
    #A 90-100
    if studentAverage>=90:
        letterGrade="A"
        print("Congrats!")
        #print("A")
    #B 80-89
    elif studentAverage>=80:
        letterGrade="B"
        print("Nice Work! You still suck cuz you didn't get an A")
        #print("B")
    #C 70-79
    elif studentAverage>=70:
        letterGrade="C"
        print("You could do better! goddamn it!")
        #print("C")
    #D 60-69
    elif studentAverage>=60:
        letterGrade="D"
        print("Study the fuck Harder!")
        #print("D")
    #F <60
    else:
        letterGrade="F"
        print("You made an F! Obviously you were out partying all night!")
    
    print(name,"'s average", format(studentAverage, '.2f'))
    print("Letter Grade", letterGrade)
    print("Number of tests per student: ",numTest)
    print("")
    print("___________________________________________________")
#classAverage
    count = count + 1
    gradeTotal = gradeTotal + numTest
    classAverage = classAverage + studentAverage 

    finalClassAverage = classAverage / count
    print("Number of names entered: ",count)
    print("Class Average: ",finalClassAverage)
    newStudent=input("Do you want another student? ('y' for yes) ")

