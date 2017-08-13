#how to write numbers
#must be converted into strings before written

def main():
    outfile=open('numbers.txt', 'w')

    #Get 3 numbers
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    num3=int(input("Enter a number"))

    #Write to file
    outfile.write(str(num1)+'\n')
    outfile.write(str(num2)+'\n')
    outfile.write(str(num3)+'\n')

    #Close
    outfile.close()
    print("Data written to numbers.txt")

main()
