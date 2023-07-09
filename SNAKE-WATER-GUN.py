import random
option=["S","W","G"]
i=10
My_score=0
CPU_score=0
print('"S" for snake "W" for water and "G" for gun"')
while i!=0:
    choice=random.choice(option)
    your_choice=input(print('Enter your choice:'))
    if choice==your_choice:
        print("Tie,no points")
        print(f"You have {i-1} choice left")
    elif choice=="S" and your_choice=="W":
        print("CPU wins")
        CPU_score+=1
        print(f"You have {i-1} choice left")
    elif choice=="S" and your_choice=="G":
        print("You wins")
        My_score+=1
        print(f"You have {i-1} choice left")
    elif choice=="W" and your_choice=="S":
        print("You wins")
        My_score+=1
        print(f"You have {i-1} choice left")
    elif choice=="W" and your_choice=="G":
        print("CPU wins")
        CPU_score+=1
        print(f"You have {i-1} choice left")
    elif choice=="G" and your_choice=="S":
        print("CPU wins")
        CPU_score+=1
        print(f"You have {i-1} choice left")
    elif choice=="G" and your_choice=="W":
        print("You wins")
        My_score+=1
        print(f"You have {i-1} choice left")
    i-=1
if My_score>CPU_score:
    print("You won the damn game")
    print(f"Your score is {My_score} and CPU score is {CPU_score}")
else:
    print("You lost the damn game")
    print(f"Your score is: {My_score} and CPU score is : {CPU_score}")

