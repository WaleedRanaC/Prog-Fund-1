#this is a program that allows the user
#to delete a record in the coffee.txt file

import os #needed for the remove and rename functions
def main():
    #create variable as flag
    found=False

    #get the coffee to delete
    search=input("Which coffee do you want to delete? ")

    #open the original coffee.txt file
    coffeeFile=open('coffee.txt','r')

    #Open the temporary file
    tempFile=open('temp.txt','w')

    #read the first record's description field
    descr=coffeeFile.readline()

    #read the rest of the file
    while descr!='':
        #read qty field
        qty=float(coffeeFile.readline())

        #strip the \n from description
        descr=descr.rstrip('\n')

        #if this is not the record to delete, write to
        #temp file
        if descr !=search:
            #write record to temp file
            tempFile.write(descr + '\n')
            tempFile.write(str(qty) + '\n')
        else:
            #set flag equal true
            found=True

        #Read next description
        descr=coffeeFile.readline()

    # Close the coffee file and the temporary file.
    coffeeFile.close()
    tempFile.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file

    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
main()
