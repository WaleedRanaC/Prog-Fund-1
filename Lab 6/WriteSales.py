#this program prompts the user for sales amount
#then writes to a text file

def main():
    #get the number of days
    numDays=int(input("For how many days do you have sales?"))

    #open new file named sales.txt
    salesFile=open('sales.txt', 'w')

    #get amount of sales for each day then write to file
    for count in range(1, numDays+1):
        #get sales for a day
        sales=float(input("Enter the sales for day #"+str(count)+': '))
        salesFile.write(str(sales)+ '\n')

    salesFile.close()
    print("Data written from sales.txt")

main()
