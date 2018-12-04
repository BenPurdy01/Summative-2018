# import the pygame module, so you can use it
#this is a test comment to see if this will fix trh problem
import pygame
pygame.init()
##import os
import math
screen_w = 500
screen_h = 500
pygame.display.set_caption("game")
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()
GREEN = (24,92,26)
"""Following functions are from stack overflow to calculateangles from vectors"""
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
"""End of stack overflow"""

class Player():

    def __init__(self):
        self.x = 50
        self.y = 50
        self.sped = 2
        self.Helth = 20

    def take_dmg(self):
        self.Helth = self.Helth - 1

##class player_run():
##    
##    def __init__(self):
##        self.myAnimation=[]
##        myAnimationSpriteDirectory=os.path.join('Sprites','playerWalk') #Folders that lead to the pictures in the directory
##        for sprite in os.listdir(myAnimationSpriteDirectory):
##            if os.path.join(myAnimationSpriteDirectory,sprite) == "Sprites\playerWalk\Thumbs.db":
##                print"nope"
##            else:
##                print os.path.join(myAnimationSpriteDirectory,sprite)
##                newframe = (os.path.join(myAnimationSpriteDirectory,sprite))
##                self.myAnimation.append(newframe)

# define a main function

def main():
##    frameNum = 0
    # load and set the logo
    
    p= Player()
##    anim = player_run()
    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
##    print anim.myAnimation
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                # build a vector between player position and mouse position
                moveVector = (mousex-p.x, mousey-p.y)
                angle_1 = angle(moveVector, (-1,0,0))
                angle_1 = (angle_1 * 180)/math.pi
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
##        isRunning = False
        pressedkeys = pygame.key.get_pressed()
        pygame.key.set_repeat(0,1)
        if pressedkeys[pygame.K_a]:
            if (p.x + 32) > 0:
##                isRunning = True
                p.x -= p.sped
            elif p.x <= 0:
                p.x = p.x +10
        if pressedkeys[pygame.K_d]:
            if (p.x + 32) < screen_w:
##                isRunning = True
                p.x += p.sped
            elif (p.x + 32) >= screen_w:
                p.x = p.x -10
        if pressedkeys[pygame.K_w]:
            if (p.y + 32) > 0:
##                isRunning = True
                p.y -= p.sped
            elif p.y <= 0:
                p.y = p.y +10
        if pressedkeys[pygame.K_s]:
            if (p.y + 32) < screen_h:
##                isRunning = True
                p.y += p.sped
            elif (p.y + 32) >= screen_h:
                p.y = p.y -10
        screen.fill(GREEN)
        image = pygame.image.load("player_noArm.png")
        image = pygame.transform.scale(image, (16,56))
        gun_test = pygame.image.load("M9_v1.png")
        gun_test = pygame.transform.scale(gun_test, (20,16))
        gun_test = pygame.transform.rotate(gun_test, angle_1)
        if angle_1 > 90:
          gun_test = pygame.transform.flip(gun_test, 0,1)
          image = pygame.transform.flip(image, 1,0)
        print angle_1
##        if isRunning == True:
##            
##            for i in range(len(anim.myAnimation)):
##                if frameNum ==5:
##                    frameNum = 0
##                else:
##                    currentFrame= pygame.image.load(anim.myAnimation[frameNum]).convert_alpha()
##                    screen.blit(currentFrame, (p.x,p.y))
##                    frameNum +=1
##        else:
        if angle_1 < 90:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x -18,p.y +12))
        elif angle_1 > 90:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x +18,p.y +12))
        pygame.display.flip()
        clock.tick(60)     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

