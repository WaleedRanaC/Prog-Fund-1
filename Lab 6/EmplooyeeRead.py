#this program dieplays the
#records that are in employee.txt

def main():
    #open the employee.txt file
    employeeFile=open('employee.txt', 'r')
    
    #read the first line from the file
    #which is the name of the field of the
    #first record
    name=employeeFile.readline()

    #If a field was read, continue processing
    while name!='':
        idNum=employeeFile.readline()
        dept=employeeFile.readline()

        #strip the newlines from the fields
        name=name.rstrip('\n')
        idNum=idNum.rstrip('\n')
        dept=dept.rstrip('\n')
        
        #display record
        print("Name: ", name)
        print("ID number: ", idNum)
        print("Dept number: ", dept)
        print()

        #Read the name field of the next record
        name=employeeFile.readline()

    #close file
    employeeFile.close()
    
#call main
main()
