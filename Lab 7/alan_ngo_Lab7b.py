def alphabatize(nameList):
    nameList.sort()
    print("")
    print("Sorted List")
    print(nameList)

def flip(nameList):
    nameList.reverse()
    print("")
    print("Reverse Sorted List")
    print(nameList)

def convertToTuple(nameList):
    nameTuple=tuple(nameList)
    print("List converted to tuple")
    print(nameTuple)

def appendList(nameList):
    nameList.append("Rene")
    print("")
    print("Appended List")
    print(nameList)

def insertName(nameList):
    nameList.insert(0,"Alan")
    print("")
    print("List with my name inserted")
    print(nameList)

def writeNames(nameList):
    print("")
    
    #open outfile
    outfile=open("names.txt",'w')
    for i in nameList:
        outfile.write(i+'\n')
    outfile.close()
    print("Names written to names.txt")
    print("")

def main():
    #define list
    nameList=[]

    #for loop
    for i in range(0,12):
        name=input("Enter a name: ")
        nameList.append(name)
    
    print("Original List")
    print(nameList)

    #sort
    alphabatize(nameList)
    
    #reverse sort
    flip(nameList)
       
    #Instructor's name append
    appendList(nameList)
    
    #My name inserted to the list
    insertName(nameList)

    #write names to list   
    writeNames(nameList)

    #tuple conversion
    convertToTuple(nameList)

main()


