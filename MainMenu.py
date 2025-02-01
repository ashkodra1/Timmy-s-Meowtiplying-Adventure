import pygame
import Button

pygame.init()

#Set the window size
SCREEN_WIDTH = 600 
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#Defining fonts
font = pygame.font.SysFont("courier", 40)

#Defining colors
BG_COLOR = (30, 122, 201) #background color
TEXT_COLOR = (255, 255, 255) #text color

#For when we need to display text
def draw_text(text, font, text_color, posx, posy):
    img = font.render(text,True,text_color)
    screen.blit(img, (posx,posy))


#Game loop
run = True

while run:
    screen.fill(BG_COLOR)

    draw_text("Press SPACE to play", font, TEXT_COLOR, 75, SCREEN_HEIGHT/2)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("YAY")
        if event.type== pygame.QUIT :
            run = False

    pygame.display.update() #Update the display

pygame.quit()


