#this program gets employee data from the user
#and saves it as records in the employee txt file

def main():
    #how many employees
    numEmployee=int(input("How many employees do you want to enter "))

    #open file
    employeeFile=open('employee.txt','w')

    #get each employee data and write it to
    #employeeFile

    #for loop
    for count in range(1, numEmployee+1):
        #get data for employee
        print("Enter the data for employee #", count, sep='')
        name=input("Name: ")
        idNum=input("ID number: ")
        dept=input("Department: ")

        #write the data as a record to file
        employeeFile.write(name+ '\n')
        employeeFile.write(idNum+ '\n')
        employeeFile.write(dept+ '\n')

        #display blank line
        print()
        
    #close file
    employeeFile.close()
    print("Employee records written to employee.txt")

#call main
main()
