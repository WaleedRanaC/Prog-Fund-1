#Alan Ngo
def menu():
    print("a. miles-kilometers")
    print("b. gallons-liters")
    print("c. punds-kilograms")
    print("d. inches-centimeter")
    print("e. farenhiet-celcius")

def main():
    menu()
    choice=input("Enter the letter choice" )
    try:
        if choice=="a":
            print("")
            miKm()
        elif choice=="b":
            print("")
            galLit()
        elif choice=="c":
            print()
            lbKg()
        elif choice=="d":
            print()
            inCm()
        elif choice=="e":
            print()
            FC()
        else:
            print("")
    except ValueError as err:
       print(err)

#conversion functions
def miKm():
    count=0
    i=0
    for i in range (10):
        try:
            for count in range(3):
                mile=float(input("How many miles do you want to convert? "))
                if mile>=0:
                    break
                print("Enter a POSITIVE mile")
            else:
                print("Strike 3! Get out of here!")
                exit()
            
        except ValueError as err:
            print("ERROR! Enter numbers!")
            print(err)
            exit()
        miToKm(mile)
def FC():
    count=0
    i=0
    for i in range (10):
        try:
            for count in range(3):
                f=float(input("How much farenhiet do you want to convert? "))
                if f<=1000:
                    break
                print("Enter a temperature LESS than 1000 degrees")
            else:
                    print("Strike 3! Get out of here!")
                    exit()

        except ValueError as err:
            print("ERROR! Enter numbers!")
            print(err)
            exit()
        fahToCel(f)
def galLit():
    count=0
    i=0
    for i in range (10):
        try:
            for count in range(3):
                gallon=float(input('How many gallons do you want to convert? '))
                if gallon>=0:
                    break
                print("Enter a POSITIVE gallon")
            else:
                print("Strike 3! Get out of here!")
                exit()
            
        except ValueError as err:
            print("ERROR! Enter numbers!")
            print(err)
            exit()
        galTolit(gallon)
def lbKg():
    count=0
    i=0
    for i in range (10):
        try:
            for count in range(3):
                pound=float(input("How many pounds do you want convert"))
                if pound>=0:
                    break
                print("Enter a POSITIVE pound")
            else:
                print("Strike 3! Get out of here!")
                exit()
            
        except ValueError as err:
            print("ERROR! Enter numbers!")
            print(err)
            exit()
        poundToKg(pound)
def inCm():
    count=0
    i=0
    for i in range (10):
        try:
            for count in range(3):
                inches=float(input("How many inches do you want to convert?"))
                if inches>=0:
                    break
                print("Enter a POSITIVE inch")
            else:
                print("Strike 3! Get out of here!")
                exit()
            
        except ValueError as err:
            print("ERROR! Enter numbers!")
            print(err)
            exit()
        inToCm(inches)

#other functions
def miToKm(mi):
    #open textFile
    textFile= open('conversions.txt', 'a')
    kilometer=1.6
    lengthConversion=mi*kilometer
    print("There are ",lengthConversion, " kilometers in ", mi, "miles")

    textFile.write("There are "+str(lengthConversion)+ " kilometers in "+ str(mi)+ "miles"+"\n")

    #close textFile
    textFile.close()

def fahToCel(fah):
    #open textFile
    textFile= open('conversions.txt', 'a')
    tempConversion=(fah-32)*5/9
    print("It is ",tempConversion, "° celcius")

    textFile.write("It is "+str(tempConversion)+ "° celcius "+"\n")

    #close textFile
    textFile.close()
    
def galTolit(gal):
    #open textFile
    textFile= open('conversions.txt', 'a')
    liter=3.9
    volumeConversion=gal*liter
    print("There are ",volumeConversion," liters in", gal, "gallons")

    textFile.write("There are "+str(volumeConversion)+" liters in "+ str(gal)+ " gallons"+"\n")

    #close textFile
    textFile.close()
    
def poundToKg(lb):
    #open textFile
    textFile= open('conversions.txt', 'a')
    kilogram=.45
    massConversion=lb*kilogram
    print("There are ",massConversion, "kilograms in ",lb, "pounds")
    textFile.write("There are "+str(massConversion)+ " kilograms in "+str(lb)+ " pounds"+"\n")
    #close textFile
    textFile.close()

def inToCm(inch):
    #open textFile
    textFile= open('conversions.txt', 'a')
    centimeter=2.54
    inchConversion=centimeter*inch
    print("There are ",inchConversion, "centimeter in ",inch, " inches")

    textFile.write("There are "+str(inchConversion)+ " centimeter in "+str(inch)+ " inches"+"\n")

    #close textFile
    textFile.close()
#call main
main()
