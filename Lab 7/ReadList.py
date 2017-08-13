#this program reads a file's contents into a list

def main():
    #open a file for reading
    infile=open('cities.txt','r')

    #read the contents of the file into a list
    cities=infile.readlines()

    #close infile
    infile.close()

    #strip \n from each element
    i=0
    while i<len(cities):
        cities[i]=cities[i].rstrip('\n')
        i+=1

    #print contents of the list
    print(cities)

main()
