#creates list for conversion
def fahToCel(fah):
    return(format((fah-32)*5/9,'.2f'))

def galToLit(gal):
    return (format(gal*3.9,'.2f'))

def poundToKg(lb):
    return (format(lb*.45,'.2f'))

def inToCM(inch):
    return(format(inch*2.54, '.2f'))

def miToKm(mi):
    return(format(mi*1.6,'.2f'))

def main():
#temp conversion
    fah=0
    tempList=[[-10,fahToCel(-10)],
              [0, fahToCel(0)],
              [10,fahToCel(10)],
              [20,fahToCel(20)],
              [30,fahToCel(30)],
              [40,fahToCel(40)],
              [50,fahToCel(50)],
              [60,fahToCel(60)],
              [70,fahToCel(70)],
              [80,fahToCel(80)],
              [90,fahToCel(90)],
              [100,fahToCel(100)]]
    print("Temperature Conversion Table")
    print (tempList,'\n')

#mile conversion
    mileList=[[0,miToKm(0)],
              [10,miToKm(10)],
              [20,miToKm(20)],
              [30,miToKm(30)],
              [40,miToKm(40)],
              [50,miToKm(50)],
              [60,miToKm(60)],
              [70,miToKm(70)],
              [80,miToKm(80)],
              [90,miToKm(90)],
              [100,miToKm(100)]]
    print("Mile Conversion Table")
    print(mileList,'\n')

#gallon conversion
    gallonList=[[0,galToLit(0)],
              [10,galToLit(10)],
              [20,galToLit(20)],
              [30,galToLit(30)],
              [40,galToLit(40)],
              [50,galToLit(50)],
              [60,galToLit(60)],
              [70,galToLit(70)],
              [80,galToLit(80)],
              [90,galToLit(90)],
              [100,galToLit(100)]]
    print("Gallon Conversion Table")
    print(gallonList,'\n')

#pound conversion
    poundList=[[0,poundToKg (0)],
              [10,poundToKg (10)],
              [20,poundToKg (20)],
              [30,poundToKg (30)],
              [40,poundToKg (40)],
              [50,poundToKg (50)],
              [60,poundToKg (60)],
              [70,poundToKg (70)],
              [80,poundToKg (80)],
              [90,poundToKg (90)],
              [100,poundToKg (100)]]
    print("Pound Conversion Table")
    print(poundList,'\n')
    
#inch conversion
    inchList=[[0,inToCM (0)],
              [10,inToCM (10)],
              [20,inToCM (20)],
              [30,inToCM (30)],
              [40,inToCM (40)],
              [50,inToCM (50)],
              [60,inToCM (60)],
              [70,inToCM (70)],
              [80,inToCM (80)],
              [90,inToCM (90)],
              [100,inToCM (100)]]
    print("Inch Conversion Table")
    print(inchList,'\n')
main()
