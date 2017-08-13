#write a short program hat uses a for loop
#to write the numbers 1-100 to file
def main():
    outfile=open('checkpoint3.txt','w')
    number=0

    #For loop
    for count in range(number, 10):
        number=number+1
        outfile.write(str(number)+" ")
    #close file
    outfile.close()
    print("Data written to checkpoint3.txt")
main()
