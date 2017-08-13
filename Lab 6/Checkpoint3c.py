#use for loop instead of while loop

def main():
    #open file
    infile=open('data.txt','r')

    #assign and define line
    line=infile.readline()
    
    #for loop
    for line in  infile:

        print(line)
    infile.close()
main()
