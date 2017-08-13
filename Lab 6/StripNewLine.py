def main():
    #open philosophers.txt
    infile=open('philosophers.txt','r')

    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()

    #strip the \n
    line1=line1.rstrip('\n')
    line2=line2.rstrip('\n')
    line3=line3.rstrip('\n')

    #close file
    infile.close()

    #print what was read into memory
    print(line1)
    print(line2)
    print(line3)
main()    
