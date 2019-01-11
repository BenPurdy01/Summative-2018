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
        self.curWep = 1

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
    wave_num = 1
    p= Player()
    """running make the loop go"""
    zed_list = []
    spawned_list = []
    ded_list = []
    running = True
    game_font = pygame.font.SysFont("pixelmix Regular", 12)
    temp = True
    
    """The Main loop"""
    while running:
        max_zeds = 10+(5*wave_num) 
        screen.fill(GREEN)
        """spawning zombies on screen"""
        if len(zed_list) < (6 + wave_num) and len(spawned_list) < max_zeds :
            for we in range((6 + wave_num)-(len(zed_list))):
                temp_x = random.randint(0,screen_w)
                temp_y = random.randint(0,screen_h)
                zed_list.append(Zombie(temp_x,temp_y))
                spawned_list.append(Zombie(temp_x,temp_y))
        """Making the zombies not hit every frame"""
        for z in range(len(zed_list)):
            zed_list[z].isHit = False
        """This is the event handling, where the event queue is checked"""
        """Weapon control"""
        for event in pygame.event.get():
            """Getting the position of the mouse and the angle from the player"""
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                angle_1 = math.degrees(math.atan2(p.y-mousey, p.x-mousex))+180
            """controling the firerate of weapons"""
            if p.curWep == 1 or p.curWep == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for z in range(len(zed_list)):
                        if mousex >= zed_list[z].x and mousey >= zed_list[z].y and mousex <= (zed_list[z].x + 34) and mousey <= (zed_list[z].y + 56):
                            zed_list[z].isHit = True
            if p.curWep == 2:
                if pygame.mouse.get_pressed()[0] == True:
                    for z in range(len(zed_list)):
                        mp40_wait = time.time()
                        if mousex >= zed_list[z].x and mousey >= zed_list[z].y and mousex <= (zed_list[z].x + 34) and mousey <= (zed_list[z].y + 56) and time.time() - mp40_wait < 0.4:
                            zed_list[z].isHit = True
                            mp40_wait = time.time()
                            
                
            """Pause button"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen.blit(pause_display, (230, 250))
                    exit = False
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    exit = True
                        if exit:
                            break
                        
            """Close the loop when you press the x"""
            if event.type == pygame.QUIT:
                running = False

        """Key control for walking/ weapon swaping"""        
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
        if pressedkeys[pygame.K_1]:
            p.curWep = 1
        if pressedkeys[pygame.K_2]:
            p.curWep = 2
        if pressedkeys[pygame.K_3]:
            p.curWep = 3

                

        """Load and scale the images"""
        image = pygame.image.load("player_noArm.png")
        image = pygame.transform.scale(image, (16,56))
        wep_1 = pygame.image.load("M9_v1.png")
        wep_1 = pygame.transform.scale(wep_1, (20,16))
        wep_2 = pygame.image.load("mp40_v1.png")
        wep_2 = pygame.transform.scale(wep_2, (32,18))
        wep_3 = pygame.image.load("pump_v1.png")
        wep_3 = pygame.transform.scale(wep_3, (52,10))
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
        wave_display = game_font.render(("Wave:"+str(wave_num)), False, (165,11,11))
        CH = pygame.image.load("crosshair.png")
        CH = pygame.transform.scale(CH, (10,10))

        """Which weapon is the player using"""
        if p.curWep == 1:
            current_weapon = wep_1
        elif p.curWep == 2:
            current_weapon = wep_2
        elif p.curWep == 3:
            current_weapon = wep_3

        """flip and rotae the player and gun based off aim direction"""
        if angle_1 > 270 or angle_1 < 90:
          current_weapon = pygame.transform.rotate(current_weapon, angle_1)
          current_weapon = pygame.transform.flip(current_weapon, 1,0)
          image = pygame.transform.flip(image, 1,0)
        else:
          current_weapon = pygame.transform.rotate(current_weapon, -angle_1)
          current_weapon = pygame.transform.flip(current_weapon, 1,1)

        """Zombie controll in program"""
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
                    ded_list.append(zed_list[i])
        zed_list = new_zed_list
        
        """Wave control"""
        if len(ded_list) == max_zeds and temp == True:
            temp = False
            wave_wait = time.time()
        if temp == False:            
            if time.time() - wave_wait >= 3:
                p.Score += max_zeds
                wave_num += 1
                spawned_list = []
                ded_list = []
                wave_wait = time.time()
                temp = True

        """Drawing player"""
        if angle_1 > 90 and angle_1 < 270:
          screen.blit(image, (p.x,p.y))
          if p.curWep == 1 or p.curWep == 2:
              screen.blit(current_weapon, (p.x -15,p.y +12))
          else:
              screen.blit(current_weapon, (p.x -20,p.y +15))
        elif angle_1 > 270 or angle_1 < 90:
          screen.blit(image, (p.x,p.y))
          if p.curWep == 1 or p.curWep == 2:
              screen.blit(current_weapon, (p.x +10,p.y +12))
          else:
              screen.blit(current_weapon, (p.x -10,p.y +15))
          
        

        """Is the player alive"""
        if p.Helth <= 0:
            p.alive = False
        if p.alive == False:
            screen.blit(G_O, (((screen_w/2)-50), ((screen_h/2)-50)))
            screen.blit(score_display,(((screen_w/2)-50), ((screen_h/2)-30)))
            running = False
        """Draw everything"""
        pygame.mouse.set_visible( False )
        screen.blit(CH, (mousex, mousey))
        screen.blit(ammo_counter,(120,450))
        screen.blit(HP_Bar, (0,450))
        rect_arg = (30,456,(4.2*p.Helth),12)
        pygame.draw.rect(screen, (23, 229, 16), rect_arg,0)
        screen.blit(score_display,(400,0))
        screen.blit(wave_display,(0,0))
        pygame.display.flip()
        clock.tick(60)
"""This runs the main loop"""
if __name__=="__main__":
    """call the fuinction"""
    main()
