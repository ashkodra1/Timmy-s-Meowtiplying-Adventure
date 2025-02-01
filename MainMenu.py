import pygame, sys
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

#Load the button images
start_img = pygame.image.load("images/start.png").convert_alpha()
exit_img = pygame.image.load("images/exit.png").convert_alpha()

#Create the buttons
start_btn = Button.Button(((SCREEN_WIDTH/2)-(start_img.get_width())), ((SCREEN_HEIGHT/2)-(start_img.get_height())), start_img, 2)
exit_btn = Button.Button(((SCREEN_WIDTH/2)-(exit_img.get_width())), ((SCREEN_HEIGHT/2)-(exit_img.get_height()))+100, exit_img, 2)

#For when we need to display text
def draw_text(text, font, text_color, posx, posy):
    img = font.render(text,True,text_color)
    screen.blit(img, (posx,posy))


#Game loop
run = True
draw_buttons = True

while run:
    screen.fill(BG_COLOR)

    if (draw_buttons and start_btn.draw(screen)): #if the button is clicked
        print("CLicked") #REMOVE LATER
        draw_buttons = False #Stop drawing the buttons
        #--- DISPLAY THE ACTUAL GAME HERE ---
    if (draw_buttons and exit_btn.draw(screen)):
        draw_buttons = False #Stop drawing the buttons
        sys.exit()
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("YAY") #REMOVE LATER
                draw_buttons = True
        if event.type== pygame.QUIT :
            run = False

    pygame.display.update() #Update the display

pygame.quit()


