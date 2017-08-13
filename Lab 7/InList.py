#this program demonstrates the in operator
#used with a list

def main():
      #create list of numbers
      prodNums= ["v4d3","x3few", "as8", "gw3ff3g"]

      #get a product number to search for
      search= input("Enter product number ")

      #determine if it's in the list
      if search in prodNums:
            print(search, "was found in list")
      else:
            print(search, "was NOT found in list")

#call main
main()
