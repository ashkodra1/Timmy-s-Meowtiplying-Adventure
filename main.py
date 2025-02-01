import sys
import pygame
import random
import time
#from scripts.utilities import load_image, load_images
#from scripts.player import Player

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y): 
        super().__init__()
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


pygame.init()
pygame.display.set_caption('Game!')
screen = pygame.display.set_mode((600,480))
display = pygame.Surface((320,240))
clock = pygame.time.Clock()

moving_sprites=pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

points=0 #total number of points of the user
gameOver=False #checks to see if the game is done to display the final messages
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
        message="That took "+ str(mins)+" minutes and "+str(sec)+ " seconds."
    else:
        message="That took "+ str(timeTaken)+ " seconds."
    return message


generate=True
message=''#displays the time taken by the user
start=time.time()

while True:
    screen.fill((0,0,0))
    draw_text("Welcome to the game!", text_font, (255,255,255), 0, 0)

    if generate:
        n1=random.randint(0,12)
        n2=random.randint(0,12)
        correct=n1*n2
        question+=str(n1)+'x'+str(n2)+'='
        generate=False


    draw_text(question, text_font, (255,255,255),0,20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_a:
            #     player.walk()
            # if event.key == pygame.K_d:
            #     player.sad()
            # if event.key == pygame.K_w:
            #     player.idle()

            #typing on the screen    
            if event.key==pygame.K_BACKSPACE:
                userText=userText[:-1]
            elif event.key==pygame.K_RETURN:
                generate=True
                try:
                    answer=int(userText)
                    if answer==correct:
                        #draw_text("Correct!", text_font, (255,255,255), 0, 80)
                        points+=1
                        player.walk()
                    else:
                        #draw_text(("Incorrect. The right answer is", correct,"."), text_font, (255,255,255), 0,80)
                        player.sad()
                    userText=''
                    question=''

                    if points==10:
                        gameOver=True
                        end=time.time()
                        message=calculateTime(start,end)
                        generate=False
                except:
                    #draw_text("Invalid answer.", text_font, (255,255,255), 0, 80)
                    userText=''
                    question=''
            else:
                userText+=event.unicode
        #if event.type == pygame.KEYUP:
         #   player.idle()

    if gameOver:
        draw_text("Game over! You won!", text_font, (255,255,255), 0, 80)
        draw_text(message, text_font, (255,255,255), 0, 100)

    draw_text(userText, text_font, (255,255,255),0,40)

    moving_sprites.draw(screen)
    moving_sprites.update(0.1,3)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()