CONTRIBUTION_RATE=.05
def main():
    grossPay=float(input("Enter the gross pay"))
    bonus=float(input("Enter the amount of bonuses"))
    showPayContrib(grossPay)
    showBonusContrib(bonus)

def showPayContrib(gross):
    contrib=gross*CONTRIBUTION_RATE
    print("The contribution for gross pay: $ ",format(contrib, ',.2f'))

def showBonusContrib(bonus):
    contrib=bonus*CONTRIBUTION_RATE
    print("The contribution for gross pay: $", format(contrib, ',.2f'))
main()
