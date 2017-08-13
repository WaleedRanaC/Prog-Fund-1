#Alan Ngo
#
#a.
#define mile
#define kilo
#input miles
#conversion 1.6
#display conversion in kilometers
#
import sys
print("UNIT CONVERSION")
kilometer=1.6
mile=float(input("How many miles do you want to convert? "))
if mile>=0:
    lengthConversion=mile*1.6
    print("There are ",lengthConversion, " kilometers in ", mile, "miles")
else:
    print("You can't enter a negative mile")
    sys.exit()
#b.
#input F
#conversion(F-32)*(5/9)
#display conversion in celcius
#
f=float(input("How much farenhiet do you want to convert? "))
if f<=1000:
    tempConversion=(f-32)*5/9
    print("It is ",tempConversion, "° celcius")
else:
    print("You can't enter a temperature greater than 1000")
    sys.exit()    
#c.
#divine liter
#input gallon
#conversion 3.9
#display conversion on gallons
liter=3.9
gallon=float(input('How many gallons do you want to convert? '))
if gallon>=0:
    volumeConversion=gallon*liter
    print("There are ",volumeConversion," liters in", gallon, "gallons")
else:
    print("You can't enter a negative gallon")
    sys.exit() 
#d.
#define kilogram
#input pound
#conversion .45
#display conversion in kilogram
#
kilogram=.45
pound=float(input("How many pounds do you want convert"))
if pound>=0:
    massConversion=pound*kilogram
    print("There are ",massConversion, "kilograms in ",pound, "pounds")
else:
    print("You can't enter a negative pound")
    sys.exit() 
#e.
#define cenimeter
#input inches
#conversion 2.54
#display conversion in centimeters
#
centimeter=2.54
inches=float(input("How many inches do you want to convert?"))
if inches>=0:
    inchConversion=centimeter*inches
    print("There are ",inchConversion, "in ",inches, "inches")
else:
    print("You can't enter a negative inch")
    sys.exit() 
