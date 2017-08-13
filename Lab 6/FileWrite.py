def main():
    #open file named philosophers.txt
    outfile=open('philosophers.txt', 'w')

    #Write name of three philosophers to file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #close file
    outfile.close()
main()
