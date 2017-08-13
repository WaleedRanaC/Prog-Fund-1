#this program removes from list

def main():
    #create list w/ items
    food=['pizza','burgers','chips']

    #display list
    print("Items in the food list: ")
    print(food)

    #get the item to change
    item=input('Which item should I remove? ')

    try:
        #remove item
        food.remove(item)

        #display what you removed
        print("This is the revised list")
        print(food)
        
    except ValueError:
        print("The item was not found in the list")

#call main
main()
