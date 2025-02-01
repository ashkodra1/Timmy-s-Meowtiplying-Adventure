import random
import time
import pygame

pygame.init()
SCREEN_WIDTH=200
SCREEN_HEIGHT=200
BACKGROUND_COLOR=(0,0,0)

points=0 #total number of points of the user
gameContinue=True

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

text_font=pygame.font.SysFont("Arial", 18, bold=True)

userText='' #users entry
question='' #the question asked to the user

def draw_text(text, font, text_col, x, y):
    img=font.render(text, True, text_col)
    screen.blit(img, (x,y))


def calculateTime(start, end):
    #calculate time
    timeTaken=int(end-start)
    if timeTaken/60>=1:
        mins=int (timeTaken/60)
        sec=timeTaken-(mins*60)
        print("That took", mins, "minutes and", sec, "seconds.")
    else:
        print("That took", timeTaken, "seconds.")


generate=True
start=time.time()

run=True
while run:
    screen.fill(BACKGROUND_COLOR)
    draw_text("Welcome to the game!", text_font, (255,255,255), 0, 0)

    if generate:
        n1=random.randint(0,12)
        n2=random.randint(0,12)
        correct=n1*n2
        question+=str(n1)+'x'+str(n2)+'='
        generate=False


    draw_text(question, text_font, (255,255,255),0,20)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                userText=userText[:-1]
            elif event.key==pygame.K_RETURN:
                generate=True
                try:
                    answer=int(userText)
                    if answer==correct:
                        draw_text("Correct!", text_font, (255,255,255), 0, 80)
                        points+=1
                    else:
                        draw_text(("Incorrect. The right answer is", correct,"."), text_font, (255,255,255), 0,80)
                    userText=''
                    question=''

                    if points==10:
                        draw_text("Game over! You won!", text_font, (255,255,255), 0, 80)
                        end=time.time()
                        calculateTime(start,end)
                        generate=False
                except:
                    draw_text("Invalid answer.", text_font, (255,255,255), 0, 80)
                    userText=''
                    question=''
            else:
                userText+=event.unicode

    draw_text(userText, text_font, (255,255,255),0,40)
    pygame.display.flip()
pygame.quit()



#print("Welcome to the game!")
#start=time.time()

# while gameContinue:
#     n1=random.randint(0,12)
#     n2=random.randint(0,12)
#     correct=n1*n2

#     try:
#         print(n1,"x",n2, "=")
#         answer=input()
#         answer=int(answer)

#         if answer==correct:
#             print("Correct!")
#             points+=1
#         else:
#             print("Incorrect. The right answer is", correct,".")

#         if points==10:
#             gameContinue=False
#             #end=time.time()
#     except:
#         print("Not a valid entry!")

# print("Game over! You won!")

# #calculate time
# timeTaken=int(end-start)
# if timeTaken/60>=1:
#     mins=int (timeTaken/60)
#     sec=timeTaken-(mins*60)
#     print("That took", mins, "minutes and", sec, "seconds.")
# else:
#     print("That took", timeTaken, "seconds.")


