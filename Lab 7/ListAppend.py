#this program demonstrates how the append method
#can be used to add items in a list

def main():
      #create empty list
      nameList=[]

      #create variable control loop
      again="y"

      #add some names to list
      while again=='y'  :
            #get a name from the user
            name=input("Enter a name: ")

            #append the name to the list
            nameList.append(name)

            #add another one?
            again=input("Add another name? 'y for yes")
            print()

      #display names entered
      print("These were the names you entered: ")

      for name in nameList:
            print(name)

#call main
main()
