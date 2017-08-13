#This program allows the user to modify
#the quantity in a record in the coffee.txt file

import os #needed to rename and remove functions
def main():
    #create a boolean variable as a flag
    found=False

    #get the search value and the new quantity
    search=input("Enter the description to search for ")
    newQty=int(input("Enter a new quantity "))

    #open the original coffee.txt file
    coffeeFile=open('coffee.txt', 'r')

    #open temporary file
    tempFile=open('temp.txt','w')

    #read the first record's description field
    descr=coffeeFile.readline()

    #read the rest of the new file
    while descr!='':
        #read the quantity field
        qty=float(coffeeFile.readline())

        #Strip the \n from the description
        descr=descr.rstrip('\n')

        #write either this record to temporary file or to the new record
        #if this one is the one that will be modifed
        if descr==search:
            #write the modified record to the temp file
            tempFile.write(descr+ '\n')
            tempFile.write(str(newQty)+'\n')

            #set flag to true
            found=True
        else:
            #Write the original record in the temp file
            tempFile.write(descr+ '\n')
            tempFile.write(str(qty)+ '\n')

        #Read the next description
        descr=coffeeFile.readline()

    #close the coffee file and temporary file
    coffeeFile.close()
    tempFile.close()

    #delete the original coffee.txt
    os.remove('coffee.txt')

    #rename the temporary file
    os.rename('temp.txt', 'coffee.txt')

    #if the search value was not found
    #display a message

    if found:
        print("The file has been updated")
    else:
        print("That item was not found in the file")

#call main
main()
