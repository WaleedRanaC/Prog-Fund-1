#the NUMDAYS constant holds
#the number of days we will gather sales
#data for

NUMDAYS=5

def main():
    #create list to hold sales for each day
    sales=[0]*NUMDAYS

    #create a variable to hold index
    index=0

    print("Enter the sales for each day")

    #Get sales for each day
    while index < NUMDAYS:
        print("Day #", index+1, ": ")
        sales[index]=float(input())
        index+=1

    #display values entered
    print("Here are the values you entered")
    for value in sales:
        print(value)

#call main
main()
