#write a short program using while loop
#that displays each line of the file

def main():
    #open file
    infile=open('data.txt','r')
    
    #assign and define line
    line=infile.readline()
    #while loop
    while line !='':
        printn(line)
        line=infile.readline()
    infile.close()
main()
    
