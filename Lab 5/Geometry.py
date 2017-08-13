import circle
import rectangle

#constants for menu choice
AREA_CIRCLE=1
CIRCUMFRENCE=2
AREA_RECTANGLE=3
PERIMETER_RECTANGLE=4
QUIT=5

def main():
    choice=0
    while choice!=QUIT:
        displayMenu()
        choice=int(input("Enter choice"))
    #menu choice
        if choice==AREA_CIRCLE:
            radius=float(input("Enter the circle's radius "))
            print("Area is " , circle.area(radius))
        elif choice==CIRCUMFRENCE:
            radius=float(input("Enter the circle's radius "))
            print("Circumfrence is ", circle.circumfrence(radius))
        elif choice==AREA_RECTANGLE:
            length=float(input("Enter Length "))
            width=float(input("Enter Width "))
            print("Area is ", rectangle.area(length, width))
        elif choice==PERIMETER_RECTANGLE:
            length=float(input("Enter Length "))
            width=float(input("Enter Width "))
            print("Perimeter is ",rectangle.perimeter(length, width))
        elif choice==QUIT:
            print ("Terminated")
        else:
            print("Invalid Selection")
            exit()
    
def displayMenu():
    print("MENU")
    print("1. Area of Circle")
    print("2. Circumfrence")
    print("3. Area of Rectangle")
    print("4. Perimeter of Rectangle")
    print("5. Quit")
    print("_________________________")

main()
