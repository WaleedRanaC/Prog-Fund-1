#this program calculates gross pay
#with exceptions

def main():
    try:
        #get the number of hours worked
        hours=int(input("How many hours did you work today? "))

        #get the hourly pay rate
        payRate=float(input("Enter your hourly pay rate"))

        #calculate gross pay
        grossPay=hours*payRate

        #display gross pay
        print("Gross Pay: $", format(grossPay, ',.2f'),sep='')

    except ValueError:
        print("ERROR: Hours worked and hourly pay must be valid integers")

main()
