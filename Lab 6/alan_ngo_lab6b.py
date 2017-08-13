#take grades from 12 kids
#write to text text file
#raise exceptions if they enter (-inf, 0)U(100, inf)
#IO exceptions

def main():

    
    count = 1
    outfile = open('grades.txt', 'w')
    

    while count <= 12:
        name = input('Enter name for student #' + str(count) + ': ')
        entry = False
        while entry == False:
            try:
                grade = int(input('Enter student average: '))
                if grade < 0 or grade > 100:
                    raise ValueError
                else:
                    entry = True
            except ValueError:
                print('Invalid grade entry! Grade must be between 0 and 100!')
        outfile.write('Student name: ' + name + '\n')
        outfile.write('Student average: ' + str(grade) + '\n')
        count += 1

    outfile.close()
    print('Student names and grades written to grades.txt')
#IO Error
    try:
        infile = open('grades.txt', 'r')
        descr = infile.readline()
        while descr != '': # Continue while text is found in the file
            #Strip \n and print the line
            descr = descr.rstrip('\n')
            print(descr)
            descr = infile.readline()
        infile.close() #File close
            
    except Exception as err: #Create exception 
        print(err)

#call main
main()

