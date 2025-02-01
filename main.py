import random;
points=0 #total number of points of the user
gameContinue=True

print("Welcome to the game!")

while gameContinue:
    n1=random.randint(0,12)
    n2=random.randint(0,12)
    correct=n1*n2

    print(n1,"x",n2, "=")
    answer=input()
    answer=int(answer)

    if answer==correct:
        points+=1

    if points==10:
        gameContinue=False

print("Game over! You won!")

