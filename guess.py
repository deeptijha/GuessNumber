from random import *
##function guess
def guess(num,attempt):
    count=0
    for i in range(1,attempt+1):
        print("Enter your",i,"th attempt")
        x=int(input())
        if x>num:
            count=count+1
            print("Too High")
        elif x<num:
            count=count+1
            print("Too Low")
        elif x==num:
            if count<=attempt:
                print("You Win")
                contnue()
    if count==attempt and x!=num:
        print("You Lost")
        contnue()

#Difference of range
def genNum(start,end):
    if end-start<50:
        start=int(input("Difference between start and end range be >=50.\nEnter start range"))
        end=int(input("Enter end range"))
        genNum(start,end)
    else:
        attempts(start,end)

#Attempts       
def attempts(start,end):
    attempt=int(input("Enter no. of attempts not more than 10"))
    if attempt<1 or attempt>10:
        attempts(start,end)
    else:
        num=randint(start,end)
        guess(num,attempt)

#Continue Game
def contnue():
    y_no=input("Do you want to play again press:Y/N")
    if y_no=="y" or y_no=="Y":
        start=int(input("Enter start range"))
        end=int(input("Enter end range"))
        genNum(start,end)
    elif y_no=="n" or y_no=="N":
        exit()
    else:
        contnue()

#Main Program
start=int(input("Enter start range"))
end=int(input("Enter end range"))
genNum(start,end)
