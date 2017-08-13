def main():
    #open philosophers.txt
    infile=open('philosophers.txt','r')

    #read three lines from the file
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()

    #close file
    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
    
