import random;
import time;
points=0 #total number of points of the user
gameContinue=True

print("Welcome to the game!")
start=time.time()

while gameContinue:
    n1=random.randint(0,12)
    n2=random.randint(0,12)
    correct=n1*n2

    try:
        print(n1,"x",n2, "=")
        answer=input()
        answer=int(answer)

        if answer==correct:
            print("Correct!")
            points+=1
        else:
            print("Incorrect. The right answer is", correct,".")

        if points==10:
            gameContinue=False
            end=time.time()
    except:
        print("Not a valid entry!")

print("Game over! You won!")

#calculate time
timeTaken=int(end-start)
if timeTaken/60>=1:
    mins=int (timeTaken/60)
    sec=timeTaken-(mins*60)
    print("That took", mins, "minutes and", sec, "seconds.")
else:
    print("That took", timeTaken, "seconds.")


