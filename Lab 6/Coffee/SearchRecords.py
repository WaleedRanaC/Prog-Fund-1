#this program allows the user to search
#the coffee.txt file for records matching
#description

def main():
    #create a boolean variable as a flag
    found=False

    #get search value
    search=input("Enter the description you want to search for: ")

    #open coffee.txt file
    coffeeFile=open('coffee.txt', 'r')

    #read the first record's description field
    descr=coffeeFile.readline()

    #Read the rest of the file
    while descr!='':
        #read the quantity field
        qty=float(coffeeFile.readline())

        #strip the \n from the description
        descr=descr.rstrip('\n')

        #determine wether the record matches the search value
        if descr==search:
            #dieplay the record
            print("Description: ",descr)
            print("Quantity: ",qty)
            print()

            #set found= true
            found=True

        #Read the next description
        descr=coffeeFile.readline()

    #close file
    coffeeFile.close()

    #if the search value was not found,
    #display message
    if found==False:
        print("No item was found in that file")
#call main
main()
