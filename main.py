from settings import *
from map_data import *
from editor import *
from objects import *

window = pygame.display.set_mode((window_width, window_height), pygame.SCALED)#Create a window.
editor = Editor()

#Start main game loop.
running = True
while running:
    delta_time = refresh.tick(refresh_rate)/1000#Get the frametime.
    
    #Tap into pygame event handler.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#If the X in the window bar is pressed.
            running = False

    keys = pygame.key.get_pressed()
    print(editor.get_pos()[0], editor.get_pos()[1])
    #print(pygame.mouse.get_pressed())#
            
    #Render:
    window.fill(BLACK)#Clear screen.

    #PUT IN RENDER CODE HERE.
    editor.update(window, keys, delta_time)
    
    pygame.display.update()#Update window.

quit()#Once the loop ends, quit out of the game.