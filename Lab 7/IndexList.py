#this program demonstrates how to get the
#index of an item in a list and replace it w/
# a new one

def main():
      #create a list with some items
      food=["pizza","chips","burgers"]

      #display the list
      print("Here are the utens ub the food list: ")
      print(food)

      #get the item to change
      item=input("Which item should I change? ")

      try:
            #get the item's index in the list
            itemIndex=food.index(item)

            #get the value to replace it with
            newItem=input("Enter the new value")

            #replace the old with the new
            food[itemIndex]=newItem

            #display the list
            print("Here is the revised list: ")
            print(food)

      except ValueError:
            print("This item was not found in the list")
main()
