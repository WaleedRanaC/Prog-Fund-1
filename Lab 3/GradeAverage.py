#constant scores
A_SCORE=90
B_SCORE=80
C_SCORE=70
D_SCORE=60
#input score
def main():
    score=int(input("Input Test Score"))
    if score>=A_SCORE:
        print("You get an A")
    elif score>=B_SCORE:
        print("You get a B")
    elif score>=C_SCORE:
        print("You get a C")
    elif score>=D_SCORE:
        print("You get a D")
    else:
        print("You get an F")
#>=90 A
#>=80 B
#>=70 C
#>=60 D
#else F
main()

