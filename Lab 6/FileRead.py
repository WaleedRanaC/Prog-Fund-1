def main():
    #open file named philosophers.txt
    infile=open('philosophers.txt','r')

    #read file's contents
    fileContents=infile.read()
    

    #close file
    infile.close()

    #print the data that was read into memory
    print(fileContents)

main()
