# import the pygame module, so you can use it
#this is a test comment to see if this will fix trh problem
import pygame
pygame.init()
import math
screen_w = 500
screen_h = 500
pygame.display.set_caption("game")
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()
GREEN = (24,92,26)
RED = (255,0,0)

class Player():

    def __init__(self):
        self.x = 50
        self.y = 50
        self.pos = (self.x,self.y)
        self.sped = 2
        self.Helth = 20

    def take_dmg(self):
        self.Helth = self.Helth - 1

    def get_cords(self):
        return (self.x,self.y)

class Zombie():

    def __init__(self):
        self.x = 250
        self.y = 250
        self.sped = .5
        self.Helth = 5

    def take_dmg(self):
        self.Helth = self.Helth - 1

class Bullet():

    def __init__(self, cords, endpoint):
        #self.time = 0
        self.sped = 10
        #make so starts not top left player
        self.x = cords[0]
        self.y = cords[1]
        self.w = 1
        self.h = 1
        
    def find_line(self):
        return ((self.endy - self.y) / (self.endx - self.x), self.y)

    def move(self):
        self.x += self.sped
        self.y += ((self.endy - self.y) / float(self.endx - self.x)) * self.sped
        #self.time += 1
        


# define a main function

def main():    
    p= Player()
    zed = Zombie()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        screen.fill(GREEN)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                angle_1 = math.degrees(math.atan2(p.y-mousey, p.x-mousex))+180
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.line(screen, RED, (p.x,p.y), (mousex,mousey), 5)
                print (mousex,mousey)
                print "button pressed"
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pressedkeys = pygame.key.get_pressed()
        pressedmouse = pygame.mouse.get_pressed()
        pygame.key.set_repeat(0,1)
        if pressedkeys[pygame.K_a]:
            if (p.x + 16) > 0:
                p.x -= p.sped
            elif p.x <= 0:
                p.x = p.x +10
        if pressedkeys[pygame.K_d]:
            if (p.x + 16) < screen_w:
                p.x += p.sped
            elif (p.x + 16) >= screen_w:
                p.x = p.x -10
        if pressedkeys[pygame.K_w]:
            if (p.y + 56) > 0:
                p.y -= p.sped
            elif p.y <= 0:
                p.y = p.y +10
        if pressedkeys[pygame.K_s]:
            if (p.y + 56) < screen_h:
                p.y += p.sped
            elif (p.y + 56) >= screen_h:
                p.y = p.y -10

        image = pygame.image.load("player_noArm.png")
        image = pygame.transform.scale(image, (16,56))
        gun_test = pygame.image.load("M9_v1.png")
        gun_test = pygame.transform.scale(gun_test, (20,16))
        zombie = pygame.image.load("zombie_0.png")
        zombie = pygame.transform.scale(zombie, (34,56))
        if angle_1 > 270 or angle_1 < 90:
          gun_test = pygame.transform.rotate(gun_test, angle_1)
          gun_test = pygame.transform.flip(gun_test, 1,0)
          image = pygame.transform.flip(image, 1,0)
        else:
          gun_test = pygame.transform.rotate(gun_test, -angle_1)
          gun_test = pygame.transform.flip(gun_test, 1,1)
        CH = pygame.image.load("crosshair.png")
        CH = pygame.transform.scale(CH, (10,10))
        if p.x > zed.x:
            zed.x+=zed.sped
        elif p.x < zed.x:
            zed.x-=zed.sped
        if p.y > zed.y:
            zed.y+=zed.sped
        elif p.y < zed.y:
            zed.y-=zed.sped
        if angle_1 < 270 or angle_1 > 90:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x - 2,p.y +12))
        else:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x +18,p.y +12))
        screen.blit(zombie, (zed.x,zed.y))
        pygame.mouse.set_visible( False ) 
        screen.blit(CH, (mousex, mousey))
        pygame.display.flip()
        clock.tick(60)     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

