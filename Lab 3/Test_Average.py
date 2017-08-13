HIGH_SCORE=95
def main():
    test1=int(input('Enter the score for test 1: '))
    test2=int(input('Enter the score for test 2: '))
    test3=int(input('Enter the score for test 3: '))

    average=(test1+test2+test3)/3

    print('The average of the test scores is ',format(average, '.2f'))

    if average>=HIGH_SCORE:
        print('Congratulations')
        print("That is a great average")
main()
