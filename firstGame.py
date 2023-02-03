import pygame 
from sys import exit 
#initializing pygame 

def display_score():
    current_time = int(pygame.time.get_ticks()/1000)- start_time
    score_surf = test_font.render(f' Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    #don't forget screen.blit without it you cannot draw 
    screen.blit(score_surf,score_rect)
    
    print(current_time)
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
game_active =True
start_time =0 

sky_surface = pygame.image.load(('images/Sky.png')).convert()
ground_surface = pygame.image.load('images/ground.png').convert()

#score_surf =test_font.render('My Game',False,(64,64,64))
#score_rect = score_surf.get_rect(center =(400,50))
#convert alpha removes alpha values, the black and white values 
snail_surf = pygame.image.load('images/snail1.png').convert_alpha()
player_surf = pygame.image.load('images/player_walk_1.png').convert_alpha()
#player_rect= pygame.Rect(left,top,width,height)


player_rect= player_surf.get_rect(midbottom =(80,300))
snail_rect = snail_surf.get_rect(bottomright=(600,300))

#player_gravity = 0
player_gravity = 0
#snail prototype 
#test_surface = pygame.Surface((400,100))
#test_surface.fill('Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:    
        
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    player_gravity =-20
            if event.type ==pygame.KEYDOWN:
                #print('key down')
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity = -20
       # if event.type == pygame.KEYUP:
           # print('key up')  
        
        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)                        
            
         
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
            #you get coordinates from here 
            #print (event.pos)      
  
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
    #    pygame.draw.rect(screen,'#c0e8ec', score_rect)
     #   pygame.draw.rect(screen,'#c0e8ec', score_rect,10)
     # screen.blit(score_surf,score_rect)
        display_score()
    
        
        #screen.blit(snail_surf,(snail_x_pos,250))
        screen.blit(snail_surf,(snail_rect))
        #we are taking player surface and placing it in the position of a rectangle 
        
        
        #player 
        #player_rect.left +=1
        snail_rect.left -=4
        if snail_rect.right <=0: snail_rect.left = 800
        screen.blit(player_surf,(player_rect))
        player_gravity +=1 
        player_rect.y +=player_gravity
        #it does a parabola when I do this 
        #player_rect.y -=player_gravity
        #with this code the player stands 
        if player_rect.bottom>=300:
            player_rect.bottom =300
        screen.blit(player_surf,player_rect)
        
        #collision 
        if snail_rect.colliderect(player_rect):
           game_active =False 
    else: 
        screen.fill('Red')    
    
    pygame.display.update()
        #if clock.tick is updated to 1 or 600 it will be very slow or fast respectively
    clock.tick(60)
        
