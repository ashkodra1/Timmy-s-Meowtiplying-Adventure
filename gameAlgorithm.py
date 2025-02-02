import sys
import pygame
import random
import time
#from scripts.utilities import load_image, load_images
#from scripts.player import Player
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y): 
        super().__init__()
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.walk_animation = False
        self.idle_animation = True
        self.sad_animation = False
        self.sprites_walk = []      #list of sprites for the walking animation
        self.sprites_idle = []      #list of sprites for the idle animation
        self.sprites_sad = []       #list of sprites for the sad animation

        self.cat_size = (100,100)       #Size of the cat

        self.sprites_walk.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/walk/01.png'),self.cat_size))
        self.sprites_walk.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/walk/02.png'),self.cat_size))

        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/01.png'),self.cat_size))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/02.png'),self.cat_size))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/03.png'),self.cat_size))

        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/01.png'),self.cat_size))
        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/02.png'),self.cat_size))
        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/03.png'),self.cat_size))

        self.num_loops_walk = 0   #number of loops for the walk_animation

        self.current_sprite = 0
        self.image = self.sprites_walk[self.current_sprite]
        self.image = self.sprites_idle[self.current_sprite]
        self.image = self.sprites_sad[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]


    def walk(self):
        self.walk_animation = True
        self.idle_animation = False
        self.sad_animation = False

    def idle(self):
        self.idle_animation = True
        self.walk_animation = False
        self.sad_animation = False

    def sad(self):
        self.sad_animation = True
        self.walk_animation = False
        self.idle_animation = False
    
    
    def update(self,speed,num_walk):
        if self.idle_animation == True:
            self.current_sprite +=speed
            if int(self.current_sprite) >= len(self.sprites_idle):
                self.current_sprite =0
            self.image = self.sprites_idle[int(self.current_sprite)]

        if self.walk_animation==True:
            self.current_sprite += speed   #makes the walking slower
            if int(self.current_sprite) >= len(self.sprites_walk):
               self.current_sprite =0
               self.num_loops_walk=self.num_loops_walk+1
               self.pos_x+=33 #move the cat
               self.rect.topleft = [self.pos_x,self.pos_y] #move the cat
               #self.walk_animation=False  #makes it go once
            if self.num_loops_walk >= num_walk:
                self.walk_animation=False
                self.num_loops_walk=0
                self.idle_animation = True

            self.image = self.sprites_walk[int(self.current_sprite)]
        

        if self.sad_animation == True:
            self.current_sprite +=speed
            if int(self.current_sprite) >= len(self.sprites_idle):
                self.current_sprite =0
                self.sad_animation=False
                self.idle_animation=True
            self.image = self.sprites_sad[int(self.current_sprite)]

def draw_text(text, font, text_col, x, y):
    img=font.render(text, True, text_col)
    screen.blit(img, (x,y))


def calculateTime(start, end):
    #calculate time
    timeTaken=int(end-start)
    if timeTaken/60>=1:
        mins=int (timeTaken/60)
        sec=timeTaken-(mins*60)
        message="You took "+ str(mins)+" minutes and "+str(sec)+ " seconds to get Timmy home."
    else:
        message="You took "+ str(timeTaken)+ " seconds to get Timmy home."
    return message

def playGame():
    pygame.init()
    pygame.display.set_caption('Game!')
    pygame.display.set_icon(pygame.image.load('data/images/background/icon.png'))
    #screen = pygame.display.set_mode((600,480))
    screen = pygame.display.set_mode((1200,500))
    display = pygame.Surface((320,240))
    clock = pygame.time.Clock()

    moving_sprites=pygame.sprite.Group()
    player = Player(50,300)
    moving_sprites.add(player)

    points=0 #total number of points of the user
    gameOver=False #checks to see if the game is done to display the final messages
    text_font=pygame.font.SysFont("Arial", 50, bold=True)
    instruction_font = pygame.font.SysFont("Arial", 30, bold=True)
    userText='' #users entry
    question='' #the question asked to the user


    generate=True
    message=''#displays the time taken by the user
    start=time.time()
    gameContinue = True
    escape = False

    while gameContinue:
        #screen.fill((0,0,0))
        #screen.blit(pygame.image.load('data/images/background/background.png'),(0,0))
        screen.blit(pygame.transform.scale(pygame.image.load('data/images/background/background.png'),(1200,500)),(0,0))
        #pygame.transform.scale(pygame.image.load('data/images/background/background.png'),(0,0))

        current=time.time()

        #draw_text("Welcome to the game!", text_font, (255,255,255), 0, 0)

        if generate:
            n1=random.randint(0,12)
            n2=random.randint(0,12)
            correct=n1*n2
            question+=str(n1)+'x'+str(n2)+'='
            generate=False

        draw_text(question, text_font, (255,255,255),50,0)
        draw_text("Press SPACE to restart", instruction_font, (255,255,255),(SCREEN_WIDTH/2) - 120 ,SCREEN_HEIGHT-40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                #typing on the screen    
                if event.key==pygame.K_BACKSPACE:
                    userText=userText[:-1]

                elif event.key == pygame.K_ESCAPE: #When escape is pressed, the game goes back to the main menu
                    # --- MAKE IT GO BACK TO THE MAIN MENU ---
                    gameContinue = False
                    escape = True
                    
                elif event.key == pygame.K_SPACE: #if space is pressed
                    gameContinue = False

                elif event.key==pygame.K_RETURN: #if enter is pressed
                    generate=True
                    try:
                        answer=int(userText)
                        if answer==correct:
                            points+=1
                            player.walk()
                        else:
                            player.sad()
                        userText=''
                        question=''

                        if points==10:
                            gameOver=True
                            end=time.time()
                            message=calculateTime(start,end)
                            generate=False
                    except:
                        userText=''
                        question=''
                        player.sad()
                else:
                    userText+=event.unicode
            #if event.type == pygame.KEYUP:
            #   player.idle()

        if gameOver:
            draw_text("Yay! Timmy is home!", text_font, (255,255,255), 50, 0)
            draw_text(message, text_font, (255,255,255), 50, 60)

        draw_text(userText, text_font, (255,255,255),50,60) #display of user inputs
        currentTime=int(current-start)
        mins=int (currentTime/60)
        sec=currentTime-(mins*60)
        if sec<10 and mins<10:
            timeMessage="0"+str(mins)+":0"+str(sec)
        elif sec>=10 and mins<10:
            timeMessage="0"+str(mins)+":"+str(sec)
        elif sec<10 and mins>=10:
            timeMessage=str(mins)+":0"+str(sec)
        else:
            timeMessage=str(mins)+":"+str(sec)

        if gameOver==False:
            draw_text(timeMessage, text_font, (255,255,255), 1050,0) #display of the time


        moving_sprites.draw(screen)
        moving_sprites.update(0.1,3)
        pygame.display.flip()
        clock.tick(60)
    
    return escape
    #pygame.quit()