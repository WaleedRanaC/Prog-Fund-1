#this program reads all of the values in sales.txt

def main():
    #open the sales.txt file for reading
    salesFile=open('sales.txt','r')

    #read first line from the file
    #don't convert to a number yet

    line=salesFile.readline()

    #as long as an empty string is not returned,
    #it will continue processing

    while line!='':
        #convert line to float
        amount=float(line)

        #format and display amount
        print(format(amount, '.2f'))

        #read the next line
        line=salesFile.readline()

    salesFile.close()

main()
    
