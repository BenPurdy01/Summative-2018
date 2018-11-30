# import the pygame module, so you can use it
#this is a test comment to see if this will fix trh problem
import pygame
pygame.init()
import os
screen_w = 500
screen_h = 500
pygame.display.set_caption("game")
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()
WHITE = (255,255,255)

class Player():

    def __init__(self):
        self.x = 50
        self.y = 50
        self.sped = 2
        self.Helth = 20

    def take_dmg(self):
        self.Helth = self.Helth - 1

class player_run():
    
    def __init__(self):
        self.myAnimation=[]
        myAnimationSpriteDirectory=os.path.join('Sprites','playerWalk') #Folders that lead to the pictures in the directory
        for sprite in os.listdir(myAnimationSpriteDirectory):
            if os.path.join(myAnimationSpriteDirectory,sprite) == "Sprites\playerWalk\Thumbs.db":
                print"nope"
            else:
                print os.path.join(myAnimationSpriteDirectory,sprite)
                newframe = (os.path.join(myAnimationSpriteDirectory,sprite))
                self.myAnimation.append(newframe)

# define a main function

def main():
    frameNum = 0
    # load and set the logo
    
    p= Player()
    anim = player_run()
    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
    print anim.myAnimation
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        isRunning = False
        pressedkeys = pygame.key.get_pressed()
        pygame.key.set_repeat(0,1)
        if pressedkeys[pygame.K_LEFT]:
            if (p.x + 32) > 0:
                isRunning = True
                p.x -= p.sped
            elif p.x <= 0:
                p.x = p.x +10
        if pressedkeys[pygame.K_RIGHT]:
            if (p.x + 32) < screen_w:
                isRunning = True
                p.x += p.sped
            elif (p.x + 32) >= screen_w:
                p.x = p.x -10
        if pressedkeys[pygame.K_UP]:
            if (p.y + 32) > 0:
                isRunning = True
                p.y -= p.sped
            elif p.y <= 0:
                p.y = p.y +10
        if pressedkeys[pygame.K_DOWN]:
            if (p.y + 32) < screen_h:
                isRunning = True
                p.y += p.sped
            elif (p.y + 32) >= screen_h:
                p.y = p.y -10
        screen.fill(WHITE)
        image = pygame.image.load("player_0.png")
        if isRunning == True:
            
            for i in range(len(anim.myAnimation)):
                if frameNum ==5:
                    frameNum = 0
                else:
                    currentFrame= pygame.image.load(anim.myAnimation[frameNum]).convert_alpha()
                    screen.blit(currentFrame, (p.x,p.y))
                    frameNum +=1
        else:
            screen.blit(image, (p.x,p.y))
        pygame.display.flip()
        clock.tick(60)     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

