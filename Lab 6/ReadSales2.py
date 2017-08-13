#This program uses the for tloop to read
#all values in the sales.txt file

def main():
    #open the sales.txt file
    salesFile=open('sales.txt','r')

    #read all the lines from the file
    for line in salesFile:
        #convert line to float
        amount=float(line)
        #format and display amount
        print(format(amount, '.2f'))

    #close file
    salesFile.close()

main()
