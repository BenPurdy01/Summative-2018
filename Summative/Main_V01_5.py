# import the pygame module, so you can use it
import pygame
WHITE = (255,255,255)
# define a main function


def main():
    player_x = 50
    player_y = 50
    sped = 5
    screen_w = 500
    screen_h = 500
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("game")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((screen_w,screen_h))
     
    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pressedkeys = pygame.key.get_pressed()
        pygame.key.set_repeat(0,1)
        if pressedkeys[pygame.K_LEFT]:
            if (player_x + 42.5) > 0:
                player_x -= sped
            elif player_x <= 0:
                player_x = player_x +10
        if pressedkeys[pygame.K_RIGHT]:
            if (player_x + 42.5) < screen_w:
                player_x += sped
            elif (player_x + 42.5) >= screen_w:
                player_x = player_x -10
        if pressedkeys[pygame.K_UP]:
            if (player_y + 50.5) > 0:
                player_y -= sped
            elif player_y <= 0:
                player_y = player_y +10
        if pressedkeys[pygame.K_DOWN]:
            if (player_y + 50.5) < screen_h:
                player_y += sped
            elif (player_y + 50.5) >= screen_h:
                player_y = player_y -10
        screen.fill(WHITE)
        image = pygame.image.load("The_Danny.png")
        screen.blit(image, (player_x,player_y))
        pygame.display.flip()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
