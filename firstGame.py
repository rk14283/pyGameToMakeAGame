import pygame 
from sys import exit 
#initializing pygame 
pygame.init()
#width and height of game window 
width = 800
height = 400 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Run Ni***')
#controls time
clock = pygame.time.Clock()
#arguments are font type and font size 
#later font is used to display score 
test_font = pygame.font.Font('images/Pixeltype.ttf', 50)
#test_surface = pygame.Surface((100,200))
#the below actually worked for the first time, now I can load images and make my game
#any imported image is a new surface
#.convert() allows pygame to work with images more easily
sky_surface = pygame.image.load(('images/Sky.png')).convert()
ground_surface = pygame.image.load('images/ground.png').convert()
#arguments are text, antialiasins, and color
text_surface =test_font.render('My Game',False,'Black')
#convert alpha removes alpha values, the black and white values 
snail_surf = pygame.image.load('images/snail1.png').convert_alpha()
player_surf = pygame.image.load('images/player_walk_1.png').convert_alpha()
#player_rect= pygame.Rect(left,top,width,height)

#player_rect= player_surf.get_rect(topleft =(80,200))
#midleft would place the player slightly higher
#player_rect= player_surf.get_rect(midleft =(80,200))
#with this the player touches ground perfectly, 300 is where the ground is  
#sprite class combines surface and rectangle and it makes it much easier to work with them 
player_rect= player_surf.get_rect(midbottom =(80,300))
snail_rect = snail_surf.get_rect(bottomright=(600,300))
#snail prototype 
#test_surface = pygame.Surface((400,100))
#test_surface.fill('Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw all our elements 
    #update everything
    #one surface on another  
    #origin point top left 
    #screen.blit(test_surface,(200,100))
    #python reads from top to bottom 
    #always remember to draw the background otherwise you will draw previous frames which will look strange 
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    #everytime we run the loop snail_x_position increases by 1
    #+=1 moves to right, -=1 moves to left 
    #if statement stops the snail from moving outside the screen
    #my code of 0 and 600 placed it at centre rather than entering at right 
  
    
    #screen.blit(snail_surf,(snail_x_pos,250))
    screen.blit(snail_surf,(snail_rect))
    #we are taking player surface and placing it in the position of a rectangle 
    player_rect.left +=1
    snail_rect.left -=4
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(player_surf,(player_rect))
    
    pygame.display.update()
    #if clock.tick is updated to 1 or 600 it will be very slow or fast respectively
    clock.tick(60)
    
#three kinds of surface, surface with color, image,text     
#creating text, creating an image of text, place it on display surface 
#creating text: create a font(text size and style), write text on a surface, blit on text surface
#pygame.error: video system not initialized-->error because we are closing but we keept the loop running
#sys module safest way to close 


#Controlling the framerate (or how fast the game runs)
#1 frame/second>10px/s*1fps>10px/second
#100 frame/second>100px/s*100fps>1000px/second

#a perfectly constant framerate is ideal>60fps for this game
#making floor is harder 

#displaying images, an important concept is surface 

#display surface and regular surface 
#diplay surface: The game window, anything displayed goes on here 
#(regular) surface: essentially a single image (something imported, rendered text or plain color). Needs to be pure display surface to be visible  

#display must be unique and is always visible and (regular) surface flexible amount 

 #plain color image text 
 
 #animating each image just means changing the position slightly on each frame 
 #rectanlges precise positioning of surfaces, basic collisions 
 #surface for image information, placement via rectangle, so you split image into two variables, and these are combined in sprite class 
 
 #collisions with rectangles can be done with rect1.colliderect(rect2)