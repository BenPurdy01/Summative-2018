# import the pygame module, so you can use it
#this is a test comment to see if this will fix trh problem
import pygame
pygame.init()
pygame.font.init()
import math
import random, time
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
        self.Score = 0
        self.alive = True

    def take_dmg(self):
        self.Helth = self.Helth - 1

    def get_cords(self):
        return (self.x,self.y)

class Zombie():

    def __init__(self,startX,startY):
        self.x = startY
        self.y = startX
        self.sped = .5
        self.Helth = 5
        self.alive = True
        self.isHit = False
        self.attack_wait = time.time()

    def move(self,plyr):
        if plyr.x > self.x:
            self.x+=self.sped
        elif plyr.x < self.x:
            self.x-=self.sped
        if plyr.y > self.y:
            self.y+=self.sped
        elif plyr.y < self.y:
            self.y-=self.sped

    def attack(self,plyr):
        if plyr.x == self.x and plyr.y == self.y and time.time()-self.attack_wait >= 1:
            self.attack_wait = time.time()
            plyr.take_dmg()


    def take_dmg(self):
        self.Helth = self.Helth - 1

    def draw(self,z,z_h):
        if self.isHit == False:
            screen.blit(z, (self.x,self.y))
        elif self.isHit == True:
            screen.blit(z_h, (self.x,self.y))
            self.take_dmg()






"""Main Function"""
def main():
    p= Player()
    """running make the loop go"""
    zed_list = []
    running = True
    game_font = pygame.font.SysFont("pixelmix Regular", 12)
    """The Main loop"""
    while running:
        screen.fill(GREEN)
        if len(zed_list) < 25:
            for we in range(25-(len(zed_list))):
                temp_x = random.randint(0,screen_w)
                temp_y = random.randint(0,screen_h)
                zed_list.append(Zombie(temp_x,temp_y))

        for z in range(len(zed_list)):
            zed_list[z].isHit = False
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                angle_1 = math.degrees(math.atan2(p.y-mousey, p.x-mousex))+180
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for z in range(len(zed_list)):
                    if mousex >= zed_list[z].x and mousey >= zed_list[z].y and mousex <= (zed_list[z].x + 34) and mousey <= (zed_list[z].y + 56):
                        zed_list[z].isHit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = False
                    screen.blit(pause_display, (230, 250))
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    exit = True
                        if exit:
                            break            
            
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pause_display = game_font.render("Paused", False, (255,0,0))
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
        zombie_h = pygame.image.load("Zombie_hit.png")
        zombie_h = pygame.transform.scale(zombie_h, (34,56))
        G_O = pygame.image.load("G_O.png")
        G_O = pygame.transform.scale(G_O, (106,55))
        ammo_counter = pygame.image.load("ammo_counter.png")
        ammo_counter = pygame.transform.scale(ammo_counter, (24, 42))
        HP_Bar = pygame.image.load("HP_bar.png")
        HP_Bar = pygame.transform.scale(HP_Bar, (114, 18))
        score_display = game_font.render(("Score:"+str(p.Score)), False, (255,255,255))
        if angle_1 > 270 or angle_1 < 90:
          gun_test = pygame.transform.rotate(gun_test, angle_1)
          gun_test = pygame.transform.flip(gun_test, 1,0)
          image = pygame.transform.flip(image, 1,0)
        else:
          gun_test = pygame.transform.rotate(gun_test, -angle_1)
          gun_test = pygame.transform.flip(gun_test, 1,1)
        CH = pygame.image.load("crosshair.png")
        CH = pygame.transform.scale(CH, (10,10))
        new_zed_list = []
        for i in range(len(zed_list)):
            if zed_list[i].alive == True:
                zed_list[i].move(p)
                zed_list[i].attack(p)
                zed_list[i].draw(zombie,zombie_h)
                new_zed_list.append(zed_list[i])
                if zed_list[i].Helth <= 0:
                    zed_list[i].alive = False
                    p.Score += 10
        zed_list = new_zed_list            
        if angle_1 < 270 or angle_1 > 90:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x - 2,p.y +12))
        else:
          screen.blit(image, (p.x,p.y))
          screen.blit(gun_test, (p.x +18,p.y +12))
        if p.Helth <= 0:
            p.alive = False
        if p.alive == False:
            screen.blit(G_O, (((screen_w/2)-50), ((screen_h/2)-50)))
            running = False
        pygame.mouse.set_visible( False )
        screen.blit(CH, (mousex, mousey))
        screen.blit(ammo_counter,(120,450))
        screen.blit(HP_Bar, (0,450))
        rect_arg = (30,456,(4.2*p.Helth),12)
        pygame.draw.rect(screen, (23, 229, 16), rect_arg,0)
        screen.blit(score_display,(400,0))
        pygame.display.flip()
        clock.tick(60)
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
