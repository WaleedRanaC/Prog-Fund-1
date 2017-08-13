#Alan Ngo
import sys
#define chance

def main():
       
#a.
#define mile
#define kilo
#input miles
#conversion 1.6
#display conversion in kilometers
    print("UNIT CONVERSION")
    count=0
    for count in range(3):
        kilometer=1.6
        mile=float(input("How many miles do you want to convert? "))
        if mile>=0:
            break
        print("Enter a POSITIVE mile")
#error
    else:
        print("Strike 3! Get out of here!")
        exit()
    lengthConversion=mile*1.6
    print("There are ",lengthConversion, " kilometers in ", mile, "miles")
    
#sys.exit()
#b.
#input F
#conversion(F-32)*(5/9)
#display conversion in celcius
#
    count=0
    for count in range(3):
        f=float(input("How much farenhiet do you want to convert? "))
        if f<=1000:
            break
        print("Enter a temperature LESS than 1000 degrees")
#error
    else:
        print("Strike 3! Get out of here!")
        exit()
    tempConversion=(f-32)*5/9
    print("It is ",tempConversion, "° celcius")

    
#sys.exit()    
#c.
#divine liter
#input gallon
#conversion 3.9
#display conversion on gallons
    count=0
    for count in range(3):
        liter=3.9
        gallon=float(input('How many gallons do you want to convert? '))
        if gallon>=0:
            break
        print("Enter a POSITIVE gallon")
    else:
        print("Strike 3! Get out of here!")
        exit()
    volumeConversion=gallon*liter
    print("There are ",volumeConversion," liters in", gallon, "gallons")
#sys.exit() 
#d.
#define kilogram
#input pound
#conversion .45
#display conversion in kilogram
#
    count=0
    for count in range(3):
        kilogram=.45
        pound=float(input("How many pounds do you want convert"))
        if pound>=0:
            break
        print("Enter a POSITIVE pound")
    else:
        print("Strike 3! Get out of here!")
        exit()
    massConversion=pound*kilogram
    print("There are ",massConversion, "kilograms in ",pound, "pounds")
#e.
#define cenimeter
#input inches
#conversion 2.54
#display conversion in centimeters
#
    count=0
    for count in range(3):
        centimeter=2.54
        inches=float(input("How many inches do you want to convert?"))
        if inches>=0:
            break
        print("Enter a POSITIVE inch")
    else:
        print("Strike 3! Get out of here!")
        exit()
    inchConversion=centimeter*inches
    print("There are ",inchConversion, " cm in ",inches, "inches")
main()
