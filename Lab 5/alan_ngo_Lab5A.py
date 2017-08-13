#Alan Ngo
def main():
    count=0
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
    inToCm(inches)

#other functions
def miToKm(mi):
    kilometer=1.6
    lengthConversion=mi*kilometer
    print("There are ",lengthConversion, " kilometers in ", mi, "miles")
def fahToCel(fah):
    tempConversion=(fah-32)*5/9
    print("It is ",tempConversion, "° celcius")
def galTolit(gal):
    liter=3.9
    volumeConversion=gal*liter
    print("There are ",volumeConversion," liters in", gal, "gallons")
def poundToKg(lb):
    kilogram=.45
    massConversion=lb*kilogram
    print("There are ",massConversion, "kilograms in ",lb, "pounds")
def inToCm(inch):
    centimeter=2.54
    inchConversion=centimeter*inch
    print("There are ",inchConversion, "centimeter in ",inch, "inches")

#call main
main()
