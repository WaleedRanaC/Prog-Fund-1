#this program calculates the total of the values in the list

def main():
    #create list
    numbers=[2,4,6,8,10]

    #create a variable to use as an accumulator
    total=0

    #calculate the total of the list elements
    for value in numbers:
        total+=value

    #display total list
    print("The total is ",total)

main()
