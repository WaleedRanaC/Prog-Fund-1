#input date in numeric format
def printDate(m, d, y):
    if y=="13":
        y="2013"

    if m=="01":
        m="January"
    if m=="02":
        m="Febuary"
    if m=="03":
        m="March"
    if m=="04":
        m="April"
    if m=="05":
        m="May"
    if m=="06":
        m="June"
    if m=="07":
        m="July"
    if m=="08":
        m="August"
    if m=="09":
        m="September"
    if m=="10":
        m="October"
    if m=="11":
        m="November"
    if m=="12":
        m="December"
    print(m+" "+d+" "+y)

def main():
    again=True
    while again==True:
        date= input("Enter the date in mm/dd/yy")
        splitDate=date.split("/")
        month=splitDate[0]
        day=splitDate[1]
        year=splitDate[2]
        
        print (splitDate)
    #check to see if they enter month out of the range (1-12)
        
        if month<"01" or month>"12":
            #while month<"01" or month>"12":
            print("Error! Month out of range")
            #date= input("Enter the date in mm/dd/yy") 
        else:
            print()

    #perform validation check for days (1-31) and year 2013
        if day<"01" or day>"31":
            #while date[1]<"1" or date[1]>"31":
            print("Error! Day out of range")
            #date= input("Enter the date in mm/dd/yy") 
        else:
            print()

        if year!="13":
            print("Error! Year must be 2013")
                
        else:
            print()
#output as example: June 12 2013
            printDate(month, day, year)
            again=False
main()
    

