import math
import os
import pygame
import random

pygame.init()
self_screen_widht , self_screen_height = pygame.display.Info().current_w , pygame.display.Info().current_h
screen_widht,screen_height =self_screen_widht/4.8 , self_screen_height/1.8#400,600


# -------------------------------------(FROG Pictures)-------------------------
script_directory = os.path.dirname(os.path.abspath(__file__))
# ------------------------(BACKGROUND)
background_path = os.path.join(script_directory, "backgrounds")

not_ready = "not_ready.png"
not_ready = pygame.image.load(os.path.join(background_path, not_ready))

back_white = "back_white.png"
back_white = pygame.image.load(os.path.join(background_path, back_white))

back_purple = "back_purple.png"
back_purple = pygame.image.load(os.path.join(background_path, back_purple))

blue_background = "blue_background.png"
blue_background = pygame.image.load(os.path.join(background_path, blue_background))
blue_background = pygame.transform.scale(blue_background, (screen_widht / 1.152737752161383, screen_height / 1.634877384196185))  # 346
blue_background_mask = pygame.mask.from_surface(blue_background)
background_width = blue_background.get_width()
background_height = blue_background.get_height()

# ------------------------(FROGS)
frogs_path = os.path.join(script_directory, "frogs")

frog = "frog.png"
frog = pygame.image.load(os.path.join(frogs_path, frog))
frog = pygame.transform.scale(frog, (screen_widht/6.557377049180328,screen_height/11.32075471698113))
frog_mask = pygame.mask.from_surface(frog)
#frog_width = blue_background.get_width()
#frog_height = blue_background.get_height()
frog_mask_width, frog_mask_height = frog_mask.get_size()
# ------------------------(ENEMİES)
enemies_path = os.path.join(script_directory, "enemies")

manta = "manta_fish.png"
manta = pygame.image.load(os.path.join(enemies_path, manta))
manta = pygame.transform.scale(manta, (screen_widht, screen_height))
manta_mask = pygame.mask.from_surface(manta)

creep = "creep.png"
creep = pygame.image.load(os.path.join(enemies_path, creep))
#creep = pygame.transform.scale(manta, (screen_widht, screen_height))
creep_mask = pygame.mask.from_surface(creep)
creep = pygame.transform.rotate(creep, 180)
#creep_width = blue_background.get_width()
#creep_height = blue_background.get_height()
#creep_mask_width, creep_mask_height = creep_mask.get_size()

# ------------------------(LOTUS)
lotus_path = os.path.join(script_directory, "lotus")

lotus = "lotus.png"
lotus = pygame.image.load(os.path.join(lotus_path, lotus))
lotus = pygame.transform.scale(lotus, (screen_widht/5.479452054794521, screen_height/8.219178082191781))
lotus_mask = pygame.mask.from_surface(lotus)
# ------------------------(LOTUS)
guns_path = os.path.join(script_directory, "guns")

tongue = "frog_tongue.png"
tongue = pygame.image.load(os.path.join(guns_path, tongue))
#tongue = pygame.transform.scale(tongue, (screen_widht/5.479452054794521, screen_height/8.219178082191781))
#tongue_mask = pygame.mask.from_surface(tongue)
#tongue_width = blue_background.get_width()
#tongue_height = blue_background.get_height()

parça = "parça.png"
parça = pygame.image.load(os.path.join(guns_path, parça))
parça_mask = pygame.mask.from_surface(parça)



tng_offscreen = 0
radius = 0
angle = 0
tng_ctr_x = 200
tng_y = 40
#tongue_center = (200,223)#(200,223)
attack = False
tng_back = False
elongation = False
konum = (193, 95)#(200,150)
tongue_velocity = pygame.Vector2(0, 0)
#tongue_center = (200, 223)
tongue_center = pygame.Vector2(200, 223)
class background():
    def __init__(self, screen):
        self.screen = screen
    def draw(self):
        self.screen.blit(blue_background,(26.5,40))  #(26.5,40)

class frogs():
    def __init__(self,screen):
        self.screen = screen

    def rotation(self,keys):
        global angle
        global tongue
        global tongue_center
        global tongue_velocity
        global attack
        global tng_y
        global tng_back
        global radius
        global elongation
        global tng_offscreen
        global creep
        global konum
        global creep_mask
        global parça_mask


        tongue_center.x = 200 + radius * math.cos(math.radians(angle + 90))
        tongue_center.y = 223 - radius * math.sin(math.radians(angle + 90))
        tongue_center.x += tongue_velocity.x
        tongue_center.y += tongue_velocity.y



        if keys[pygame.K_a] and tng_y==40:
            angle += 6

            #tng_ctr_y += 1
        if keys[pygame.K_d] and tng_y == 40:
            angle -= 6

        if keys[pygame.K_SPACE]:

            attack = True
            #print(angle)

        if attack == True and tng_y == 40:
            elongation = True

        if tng_y < 151 and elongation == True:
            tng_y+=5
            radius+=5

        if tng_y == 130:
            tng_back = True
            attack = False
            elongation = False

        if tng_back == True:
            tng_y -= 5
            radius-= 5
            attack = False
            elongation = False
            if tng_y == 40:
                tng_back = False
                #elongation = True



        #tng_offscreen = creep_mask.overlap(tongue_mask, (0, 0))
        #print(tng_offscreen)
        tongue = pygame.transform.scale(tongue, (5, tng_y))



        self.frog = pygame.transform.rotate(frog, angle)
        self.tongue = pygame.transform.rotate(tongue, angle)
        self.parça = pygame.transform.rotate(parça, angle)

        self.frog_rect = self.frog.get_rect(center=(200,223))
        self.tongue_rect = self.tongue.get_rect(center=tongue_center)#screen_widht / 2.446483180428135, screen_height / 3.20855614973262

        parça_mask = pygame.mask.from_surface(self.parça)
        tongue_mask = pygame.mask.from_surface(self.tongue)
        tongue_mask_width, tongue_mask_height = tongue_mask.get_size()
        #creep_mask = pygame.mask.from_surface(creep)
        creep_mask_width, creep_mask_height = creep_mask.get_size()
        tng_offscreen = parça_mask.overlap(creep_mask,(creep_mask.get_size()[0] - parça_mask.get_size()[0],creep_mask.get_size()[1] - parça_mask.get_size()[1]))

        if self.parça.get_size()[0] == creep.get_size()[0] and self.parça.get_size()[1] == creep.get_size()[1]:
            print("Collision detected at:", tng_offscreen)
            konum = (random.randint(10, 390), random.randint(10, 590))
            print("New creep position:", konum)
            creep_mask = pygame.mask.from_surface(creep)
        print(tng_offscreen)


    def draw(self):
            #global tongue
            global konum
            self.screen.blit(lotus,(screen_widht/2.446483180428135,screen_height/3.20855614973262))

            self.screen.blit(self.tongue, self.tongue_rect.topleft)
            self.screen.blit(self.frog, self.frog_rect.topleft)
            #self.screen.blit(self.parça, self.tongue_rect)
            parça_mask = pygame.mask.from_surface(self.parça)
            self.screen.blit(creep, konum)
            #tongue = pygame.transform.scale(tongue, (5, tng_y))

class enemies():
    pass


def sayı():
    print("1")
def start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos):
    global game_exit
    back_button = back_white
    """
    bg = background(screen)
    bg.draw()
    frg = frogs(screen)     burayı oyun tamamlayınca açarsın
    frg.rotation(keys)
    frg.draw()
    """

    """
    def background_draw(self):
        pass
    def frog_rotation(self):
        pass
    def frog_attack(self):
        pass
    def enemies_draw(self):
        pass
    def collision(self):
        pass
    def level(self):
        pass

    """
    screen.blit(not_ready,(27,40))
    if (screen_widht/2-back_white.get_width()/2) <= mouse_pos[0] <= (screen_widht/2-back_white.get_width()/2)+back_white.get_width() and 270 <= mouse_pos[1] <= 270+back_white.get_height():
        back_button = back_purple
        if left_click == True:
            game_exit = True
    screen.blit(back_button, (screen_widht/2-back_white.get_width()/2, 270))

def return_menu():
    global game_exit
    return game_exit
def return_false():
    global game_exit
    game_exit = False

def reset():
    pass

