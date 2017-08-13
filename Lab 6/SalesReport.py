#This program displays the total
#amounts in the salesData.txt file

def main():
    #initialize accumulator
    total=0

    try:
        #open salesData
        infile=open('sales2.txt', 'r')

        #read the values from the file
        #and accumulate them

        for line in infile:
            amount=float(line)
            total+=amount

        #close file
        infile.close()

        #print the total
        print(format(total, ',.2f'))

        #exceptions
    except IOError:
        print("An error occured in trying to read the file")

    except ValueError:
        print("Non numeric data found in the file")

    except:
        print(" an error has occured")

#call main
main()
        
