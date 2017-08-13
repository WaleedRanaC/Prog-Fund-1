#this program displays the records from
#coffee.txt file

def main():
    #open the coffee.txt file
    coffeeFile=open('coffee.txt','r')

    #read the first record's description in field
    descr=coffeeFile.readline()

    #read the rest of the file
    while descr!='':
        #read the quantity field
        qty=float(coffeeFile.readline())

        #strip the \n from description
        descr=descr.rstrip('\n')

        #display the record
        print("Description: ", descr)
        print("Quantity: ", qty)

        #read the next description
        descr=coffeeFile.readline()

    #close file
    coffeeFile.close()

#call main
main()
