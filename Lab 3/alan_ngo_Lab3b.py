#constants
BASE_SALARY=2000
MIN_TIME=3
MAX_VAC=3
FIVE_YEAR_BONUS=1000
THREE_MONTH=0

def main():
#variables    
    employeeName=input("Enter Employee Name: ")
    longevity=int(input("How many MONTHS have you been working? "))
    sales=float(input("How much do you make in sales? "))
    vacTime=int(input("How many days have you been on vacation this month? "))
    commisionRate=0.0
#salary=0
    bonus=0.00
    grossPay=0.00
    deductions=0.00
    additionalBonus=0.00
#sales/commision table
    if sales<10000: 
        commisionRate=0
        bonus=0
    elif sales>=10000 and sales<=100000: 
        commisionRate=.02
        bonus=0
    elif sales>=100001 and sales<=500000: 
        commisionRate=.15
        bonus=1000
    elif sales>=500001 and sales<=1000000: 
        commisionRate=.28
        bonus=5000
    elif sales>1000000: 
        commisionRate=.35
        bonus=100000
    else:
        commisionRate=0
        bonus=0
#commision calculation
    commision=commisionRate*sales

#vacation time
    if vacTime>MAX_VAC:
        deductions=200
    else:
        deductions=0

#three month requirement
    if longevity<3:
        bonus=0

#five year bonus
    if longevity>=60 and sales>100000:
        additionalBonus=FIVE_YEAR_BONUS
    else:
        additionalBonus=0

#grossPay
    grossPay=BASE_SALARY+commision+bonus+additionalBonus-deductions

#print
    
#name
    print("Employee Name: ",employeeName)
#longevity
    print("Months worked: ",longevity)
#base salary
    print("Base Salary: $",format(BASE_SALARY, '.2f'))
#commision
    print("Commision: $",format(commision, '.2f'))
#bonus
    print("Bonus: $",format(bonus, '.2f'))
#additional bonus
    print("Additional Bonus: $",format(additionalBonus, '.2f'))
#deductions
    print("Deductions: -$",format(deductions, '.2f'))
    print("*If your vacation days of this month exceed 3, you will be deducted $200")
#final gross paycheck
    print("Gross Pay: $",format(grossPay, '.2f'))
main()    
        
    
