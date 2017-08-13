def main():
    value=99
    print("The value is ", value)
    changeMe(value)
    print("Back in main the value is ", value)
def changeMe(arg):
    print("I am changing the value")
    arg=0
    print("Now the value is ",arg)
main()
