import conversion
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
    print("Mile Conversion: ", conversion.convertMiles(mile))

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
    print("Farenheit Conversion: ", conversion.convertFarenheit(f))
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
    print("Gallon Conversion: ", conversion.convertGallon(gallon))
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
    print("Pound Conversion: ", conversion.convertPound(pound))
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
    print("Inch Conversion: ", conversion.convertInch(inches))
main()
