#Alan Ngo
#
#a.
#define mile
#define kilo
#input miles
#conversion 1.6
#display conversion in kilometers
#
print("UNIT CONVERSION")
kilometer=1.6
mile=float(input("enter miles "))
lengthConversion=mile*1.6
print("There are ",lengthConversion, " kilometers in ", mile, "miles")
#b.
#input F
#conversion(F-32)*(5/9)
#display conversion in celcius
#
f=float(input("enter farenhiet"))
tempConversion=(f-32)*5/9
print("It is ",tempConversion, "° celcius")
#c.
#divine liter
#input gallon
#conversion 3.9
#display conversion on gallons
liter=3.9
gallon=float(input('enter gallons'))
volumeConversion=gallon*liter
print("There are ",volumeConversion," liters in", gallon, "gallons")
#d.
#define kilogram
#input pound
#conversion .45
#display conversion in kilogram
#
kilogram=.45
pound=float(input("enter pounds"))
massConversion=pound*kilogram
print("There are ",massConversion, "kilograms in ",pound, "pounds")
#e.
#define cenimeter
#input inches
#conversion 2.54
#display conversion in centimeters
#
centimeter=2.54
inches=float(input("enter inches"))
inchConversion=centimeter*inches
print("There are ",inchConversion, "in ",inches, "inches")
