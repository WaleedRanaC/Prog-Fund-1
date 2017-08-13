#this program uses writelines method to save a list
#of strings to a file

def main():
    #create list of strings
    cities=["New York","Boston","Atlanta","Dallas","Sacremento"]

    #open a file for writing
    outfile=open('cities.txt','w')

    for item in cities:
        outfile.write(item+'\n')

    #close the file
    outfile.close()

#call the main function
main()
