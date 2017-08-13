import random

#constants
ROWS=3
COLS=4

def main():
    #create a 2-d list
    values=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    #fill w/ random numbers

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c]=random.randint(1,100)

    #display list
    print(values,'\n')

#call main
main()
