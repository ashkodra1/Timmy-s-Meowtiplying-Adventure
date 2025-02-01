import sys
import pygame
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

        self.sprites_walk.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/walk/01.png'),(100,100)))
        self.sprites_walk.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/walk/02.png'),(100,100)))

        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/01.png'),(100,100)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/02.png'),(100,100)))
        self.sprites_idle.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/idle/03.png'),(100,100)))

        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/01.png'),(100,100)))
        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/02.png'),(100,100)))
        self.sprites_sad.append(pygame.transform.scale(pygame.image.load('data/images/entities/player/sad/03.png'),(100,100)))

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.walk()
            if event.key == pygame.K_d:
                player.sad()
            if event.key == pygame.K_w:
                player.idle()
        #if event.type == pygame.KEYUP:
         #   player.idle()

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.1,3)
    pygame.display.flip()
    clock.tick(60)
