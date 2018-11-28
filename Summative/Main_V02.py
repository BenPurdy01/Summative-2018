# import the pygame module, so you can use it
import pygame
import os

WHITE = (255,255,255)

class Player():

    def __init__(self):
        self.x = 50
        self.y = 50
        self.sped = 5
        self.Helth = 20

    def take_dmg(self):
        self.Helth = self.Helth - 1

class player_run():
    
    def __init__(self):
        self.myAnimation=[]
        myAnimationSpriteDirectory=os.path.join('Sprites','playerWalk') #Folders that lead to the pictures in the directory
        for myAnimationFolder in os.listdir(myAnimationSpriteDirectory):
            self.myAnimation.append(pygame.image.load(os.path.join(myAnimationSpriteDirectory,myAnimationFolder)))

# define a main function


def main():
    screen_w = 500
    screen_h = 500
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("game")
    p= Player()
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((screen_w,screen_h))
    clock = pygame.time.Clock()
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
            if (p.x + 42.5) > 0:
                p.x -= p.sped
            elif p.x <= 0:
                p.x = p.x +10
        if pressedkeys[pygame.K_RIGHT]:
            if (p.x + 42.5) < screen_w:
                p.x += p.sped
            elif (p.x + 42.5) >= screen_w:
                p.x = p.x -10
        if pressedkeys[pygame.K_UP]:
            if (p.y + 50.5) > 0:
                p.y -= p.sped
            elif p.y <= 0:
                p.y = p.y +10
        if pressedkeys[pygame.K_DOWN]:
            if (p.y + 50.5) < screen_h:
                p.y += p.sped
            elif (p.y + 50.5) >= screen_h:
                p.y = p.y -10
        screen.fill(WHITE)
        image = pygame.image.load("The_Danny.png")
        screen.blit(image, (p.x,p.y))
        pygame.display.flip()
        clock.tick(60)     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
