def main():
    showInterest(rate=.01, periods=10, principle=10000)

def showInterest(principle, rate, periods):
    interest=principle*rate*periods
    print("The simple interest will be $", format(interest, '.2f'))
main()    
