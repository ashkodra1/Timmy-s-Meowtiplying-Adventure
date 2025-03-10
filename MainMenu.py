import pygame, sys, os
import Button
import gameAlgorithm

os.environ['SDL_VIDEO_CENTERED'] = '1' #Center the window

pygame.init()

#Set the window size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BTN_SCALE_START = 1.5 #Scale of the start buttons
BTN_SCALE_EXIT = 1.5 #Scale of the exit buttons

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
pygame.display.set_icon(pygame.image.load('data/images/background/icon.png'))

#Defining fonts
font = pygame.font.SysFont("courier", 40)

#Defining colors
BG_COLOR = (30, 122, 201) #background color
TEXT_COLOR = (255, 255, 255) #text color

#Load the button images
start_img = pygame.image.load("images/start.png").convert_alpha()
exit_img = pygame.image.load("images/exit.png").convert_alpha()
start_active_img = pygame.image.load("images/start_hover.png").convert_alpha()
exit_active_img = pygame.image.load("images/exit_hover.png").convert_alpha()
background_img = pygame.image.load("images/background.png").convert_alpha()
img = pygame.image.load("images/logo.png").convert_alpha()
logo_img = pygame.transform.scale(img, (int(img.get_width() * 1.5), int(img.get_height() * 1.5)))



#Create the buttons
start_btn = Button.Button(((SCREEN_WIDTH/2)-(start_img.get_width()/1.5)), ((SCREEN_HEIGHT/2)-(start_img.get_height()/2)), start_img, start_active_img, start_img, BTN_SCALE_START)
exit_btn = Button.Button(((SCREEN_WIDTH/2)-(exit_img.get_width()/1.5)), ((SCREEN_HEIGHT/2)-(exit_img.get_height()/2))+75, exit_img, exit_active_img, exit_img, BTN_SCALE_EXIT)

#For when we need to display text
def draw_text(text, font, text_color, posx, posy):
    img = font.render(text,True,text_color)
    screen.blit(img, (posx,posy))


#Game loop
run = True
draw_buttons = True
draw_game = False

while run:
    screen.blit(background_img, (0,0))
    

    if(draw_game==True): #if it's time to display the game
        #--- DISPLAY THE ACTUAL GAME HERE ---
        if (gameAlgorithm.playGame()): #check is the escape key was pressed (TRUE) or if the space key was pressed (FALSE)
            draw_game = False #stop drawing the game
            draw_buttons = True #draw the buttons

            #reajust the window to display the main menu again
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            pygame.display.set_caption("Main Menu")
            pygame.display.set_icon(pygame.image.load('data/images/background/icon.png'))
    
    else: #If it'S not time to display the game
        screen.blit(logo_img, (((SCREEN_WIDTH/2)-(logo_img.get_width()/2)),25))

    if (draw_buttons and start_btn.draw(screen)): #if the start button is clicked
        draw_buttons = False #Stop drawing the buttons
        draw_game = True #Draw the game

    if (draw_buttons and exit_btn.draw(screen)): #if the exit button is clicked
        sys.exit() #end the program
    

    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #when the escape button is pressed
                draw_buttons = True #allow to display the buttons
        if event.type== pygame.QUIT :
            run = False

    pygame.display.update() #Update the display

pygame.quit()


