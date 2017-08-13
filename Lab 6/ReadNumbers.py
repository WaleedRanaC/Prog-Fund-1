#reading numbers from external file

def main():
    infile=open('numbers.txt', 'r')

    #reading from file
    num1=int(infile.readline())
    num2=int(infile.readline())
    num3=int(infile.readline())

    infile.close()

    #Add the three numbers
    total=num1+num2+num3

    #display numbers
    print("The numbers are ",num1, num2, num3)
    print("Total is ", total)

main()
