#this program displays the total amount in
#the sales2.txt file

def main():
    #initialize an accumulator
    total=0

    try:
        #open the sales2.file
        infile=open('sales2.txt','r')

        #read values from the file and accumulate them
        for line in infile:
            amount=float(line)
            total+=amount

        #close the file
        infile.close()

    except Exception as err:
        print(err)
    else:
        #print the total
        print(format(total, '.2f'))

#call main
main()
        
