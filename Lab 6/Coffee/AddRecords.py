#this program adds coffee inventory records to
#coffee.txt

def main():

    #create a variable to control loop
    another='y'

    #open the coffee.txt file in append mode
    coffeeFile=open('coffee.txt', 'a')

    #add records to the file
    while another=='y' or another=='Y':
        #get coffee record data
        print("Enter the following coffee data")
        descr=input("Description: ")
        qty=int(input("Quantity: "))

        #append the data to the file
        coffeeFile.write(descr+'\n')
        coffeeFile.write(str(qty)+'\n')

        #Determine wether the user wants to add
        #another record to file
        print("Do you want to add another record? ")
        another=input("'Y' =yes, anything else=no")

    #close file
    coffeeFile.close()
    print("Data appended to coffee.txt")

#call main
main()
