#enter their name and email adresses before displaying conversions
def miToKm(mi):
    kilometer=1.6
    lengthConversion=mi*kilometer
    print("There are ",lengthConversion, " kilometers in ", mi, "miles")
    print("")
def fahToCel(fah):
    tempConversion=(fah-32)*5/9
    print("It is ",tempConversion, "° celcius")
    print("")
def galTolit(gal):
    liter=3.9
    volumeConversion=gal*liter
    print("There are ",volumeConversion," liters in", gal, "gallons")
    print("")
def poundToKg(lb):
    kilogram=.45
    massConversion=lb*kilogram
    print("There are ",massConversion, "kilograms in ",lb, "pounds")
    print("")
def inToCm(inch):
    centimeter=2.54
    inchConversion=centimeter*inch
    print("There are ",inchConversion, "centimeter in ",inch, "inches")
    print("")

def main():
    name=input("Enter your name: ")
    email=input("Enter your email address: ")
    
    i=email.find("@")
    if i==-1:
        while i==-1:
            email=input("Enter your email address: ")
            i=email.find("@")
    else:
        print()

#mi-km
    count=0
    for count in range(3):
        mile=float(input("How many miles do you want to convert? "))
        if mile>=0:
            break
        print("Enter a POSITIVE mile")
    else:
        print("Strike 3! Get out of here!")
        exit()
    print(name,"'s mile conversion")
    print("Email: ", email)
    print("__________________________________________________")
    miToKm(mile)

#F-C
    count=0
    for count in range(3):
        f=float(input("How much farenhiet do you want to convert? "))
        if f<=1000:
            break
        print("Enter a temperature LESS than 1000 degrees")
    else:
        print("Strike 3! Get out of here!")
        exit()
    print(name,"'s temperature conversion")
    print("Email: ", email)
    print("__________________________________________________")
    fahToCel(f)

#gal-lit
    count=0
    for count in range(3):
        gallon=float(input('How many gallons do you want to convert? '))
        if gallon>=0:
            break
        print("Enter a POSITIVE gallon")
    else:
        print("Strike 3! Get out of here!")
        exit()
    print(name,"'s gallon conversion")
    print("Email: ", email)
    print("__________________________________________________")
    galTolit(gallon)
#lb-kg
    count=0
    for count in range(3):
        pound=float(input("How many pounds do you want convert"))
        if pound>=0:
            break
        print("Enter a POSITIVE pound")
    else:
        print("Strike 3! Get out of here!")
        exit()
    print(name,"'s pound conversion")
    print("Email: ", email)
    print("__________________________________________________")
    poundToKg(pound)

#in-cm
    count=0
    for count in range(3):
        inches=float(input("How many inches do you want to convert?"))
        if inches>=0:
            break
        print("Enter a POSITIVE inch")
    else:
        print("Strike 3! Get out of here!")
        exit()
    print(name,"'s inch conversion")
    print("Email: ", email)
    print("__________________________________________________")
    inToCm(inches)
main()
