import pygame
import math
import os
import pygame
import random
#import time
pygame.init()
self_screen_widht , self_screen_height = pygame.display.Info().current_w , pygame.display.Info().current_h
screen_widht,screen_height =400,600#self_screen_widht/4.8 , self_screen_height/1.8#400,600


# -------------------------------------(FROG Pictures)-------------------------
script_directory = os.path.dirname(os.path.abspath(__file__))
# ------------------------(BACKGROUND)
background_path = os.path.join(script_directory, "backgrounds")

blue_background = "blue_background.png"
blue_background = pygame.image.load(os.path.join(background_path, blue_background))
background_width,background_height = blue_background.get_size()

# ------------------------(motorcycle)
motorcycle_path = os.path.join(script_directory, "motorcycles")

jetski = "motorcycle.png"
jetski = pygame.image.load(os.path.join(motorcycle_path, jetski))
motorcycle_width,motorcycle_height = jetski.get_size()
motorcycle_locationx,motorcycle_locationy = (background_width/2-motorcycle_width/2 + 26.5) , (background_height+motorcycle_height)#(background_height-motorcycle_height)

motorcycle_fly = "motorcycle_fly.png"
motorcycle_fly = pygame.image.load(os.path.join(motorcycle_path, motorcycle_fly))
motorcycle_fly_width,motorcycle_fly_height = motorcycle_fly.get_size()

# ------------------------(wave)
wave_path = os.path.join(script_directory, "waves")

wave_1 = "wave.png"
wave_1 = pygame.image.load(os.path.join(wave_path, wave_1))

wave_2 = "wave2.png"
wave_2 = pygame.image.load(os.path.join(wave_path, wave_2))

wave_3 = "wave3.png"
wave_3 = pygame.image.load(os.path.join(wave_path, wave_3))

wave_list = [wave_1,wave_2,wave_3]
wave_index = 0
# ------------------------
barriers_path = os.path.join(script_directory, "barriers")

lifebuoy = "lifebuoy.png"
lifebuoy = pygame.image.load(os.path.join(barriers_path, lifebuoy))
lifebuoy_width,lifebuoy_height = lifebuoy.get_size()
x = 200
y = 40 - lifebuoy_height

sea_ball = "sea_ball.png"
sea_ball = pygame.image.load(os.path.join(barriers_path, sea_ball))
sea_ball_width,sea_ball_height = lifebuoy.get_size()

lifebuoy_donat = "lifebuoy_donat.png"
lifebuoy_donat = pygame.image.load(os.path.join(barriers_path, lifebuoy_donat))
lifebuoy_donat_width,lifebuoy_donat_height = lifebuoy.get_size()

tornado = "tornado.png"
tornado = pygame.image.load(os.path.join(barriers_path, tornado))
tornado_width,tornado_height = tornado.get_size()

gold_heart = "gold_heart.png"
gold_heart = pygame.image.load(os.path.join(barriers_path, gold_heart))
gold_heart_width,gold_heart_height = tornado.get_size()

red_heart = "red_heart.png"
red_heart = pygame.image.load(os.path.join(barriers_path, red_heart))
red_heart_width,red_heart_height = tornado.get_size()

white_heart = "white_heart.png"
white_heart = pygame.image.load(os.path.join(barriers_path, white_heart))
white_heart_width,white_heart_height = tornado.get_size()

# ------------------------(game over)
game_over_path = os.path.join(script_directory, "game_over")

game_over_yellow = "game_over_yelleow.png"
game_over_yellow = pygame.image.load(os.path.join(game_over_path, game_over_yellow))

game_over_red = "game_over_red.png"
game_over_red = pygame.image.load(os.path.join(game_over_path, game_over_red))

game_over_green = "game_over_green.png"
game_over_green = pygame.image.load(os.path.join(game_over_path, game_over_green))

game_over_purple = "game_over_purple.png"
game_over_purple = pygame.image.load(os.path.join(game_over_path, game_over_purple))

again_button = "again_white.png"
again_button = pygame.image.load(os.path.join(game_over_path, again_button))

back_button = "back_white.png"
back_button = pygame.image.load(os.path.join(game_over_path, back_button))

signboard = "signboard.png"
signboard = pygame.image.load(os.path.join(game_over_path, signboard))


game_over_list = [game_over_yellow,game_over_green,game_over_red,game_over_purple]
game_over_index = 0

# ------------------------(game over)
impact_path = os.path.join(script_directory, "impact_pictures")

impact1 = "impact1.png"
impact1 = pygame.image.load(os.path.join(impact_path, impact1))

impact2 = "impact2.png"
impact2 = pygame.image.load(os.path.join(impact_path, impact2))

impact3 = "impact3.png"
impact3 = pygame.image.load(os.path.join(impact_path, impact3))

impact4 = "impact4.png"
impact4 = pygame.image.load(os.path.join(impact_path, impact4))

impact5 = "impact5.png"
impact5 = pygame.image.load(os.path.join(impact_path, impact5))

impact6 = "impact6.png"
impact6 = pygame.image.load(os.path.join(impact_path, impact6))

impact7 = "impact7.png"
impact7 = pygame.image.load(os.path.join(impact_path, impact7))

impact8 = "impact8.png"
impact8 = pygame.image.load(os.path.join(impact_path, impact8))

impact_game_over_purple = "impact_game_over_purple.png"
impact_game_over_purple = pygame.image.load(os.path.join(impact_path, impact_game_over_purple))


impact_list_barrier = [impact1,impact2,impact3,impact4,impact5,impact6,impact7,impact8,impact_game_over_purple]
impact_index = 0

#----------------------

impact1_red = "impact1_red.png"
impact1_red = pygame.image.load(os.path.join(impact_path, impact1_red))

impact2_red = "impact2_red.png"
impact2_red = pygame.image.load(os.path.join(impact_path, impact2_red))

impact3_red = "impact3_red.png"
impact3_red = pygame.image.load(os.path.join(impact_path, impact3_red))

impact4_red = "impact4_red.png"
impact4_red = pygame.image.load(os.path.join(impact_path, impact4_red))

impact5_red = "impact5_red.png"
impact5_red = pygame.image.load(os.path.join(impact_path, impact5_red))

impact6_red = "impact6_red.png"
impact6_red = pygame.image.load(os.path.join(impact_path, impact6_red))

impact7_red = "impact7_red.png"
impact7_red = pygame.image.load(os.path.join(impact_path, impact7_red))

impact8_red = "impact8_red.png"
impact8_red = pygame.image.load(os.path.join(impact_path, impact8_red))

impact_list_heart = [impact1_red,impact2_red,impact3_red,impact4_red,impact5_red,impact6_red,impact7_red,impact8_red,impact_game_over_purple]

impact1_gold = "impact1_gold.png"
impact1_gold = pygame.image.load(os.path.join(impact_path, impact1_gold))

impact2_gold = "impact2_gold.png"
impact2_gold = pygame.image.load(os.path.join(impact_path, impact2_gold))

impact3_gold = "impact3_gold.png"
impact3_gold = pygame.image.load(os.path.join(impact_path, impact3_gold))

impact4_gold = "impact4_gold.png"
impact4_gold = pygame.image.load(os.path.join(impact_path, impact4_gold))

impact5_gold = "impact5_gold.png"
impact5_gold = pygame.image.load(os.path.join(impact_path, impact5_gold))

impact6_gold = "impact6_gold.png"
impact6_gold = pygame.image.load(os.path.join(impact_path, impact6_gold))

impact7_gold = "impact7_gold.png"
impact7_gold = pygame.image.load(os.path.join(impact_path, impact7_gold))

impact8_gold = "impact8_gold.png"
impact8_gold = pygame.image.load(os.path.join(impact_path, impact8_gold))


impact_list_gold = [impact1_gold,impact2_gold,impact3_gold,impact4_gold,impact5_gold,impact6_gold,impact7_gold,impact8_gold,impact_game_over_purple]
# ------------------------
impact1_white = "impact1_white.png"
impact1_white = pygame.image.load(os.path.join(impact_path, impact1_white))

impact2_white = "impact2_white.png"
impact2_white = pygame.image.load(os.path.join(impact_path, impact2_white))

impact3_white = "impact3_white.png"
impact3_white = pygame.image.load(os.path.join(impact_path, impact3_white))

impact4_white = "impact4_white.png"
impact4_white = pygame.image.load(os.path.join(impact_path, impact4_white))

impact5_white = "impact5_white.png"
impact5_white = pygame.image.load(os.path.join(impact_path, impact5_white))

impact6_white = "impact6_white.png"
impact6_white = pygame.image.load(os.path.join(impact_path, impact6_white))

impact7_white = "impact7_white.png"
impact7_white = pygame.image.load(os.path.join(impact_path, impact7_white))

impact8_white = "impact8_white.png"
impact8_white = pygame.image.load(os.path.join(impact_path, impact8_white))


impact_list_white = [impact1_white,impact2_white,impact3_white,impact4_white,impact5_white,impact6_white,impact7_white,impact8_white,impact_game_over_purple]
# ------------------------
sound_path = os.path.join(script_directory, "sound")

game_over_cntrl_False = "music-for-arcade-style-game-146875.mp3"
game_over_cntrl_False = pygame.mixer.Sound(os.path.join(sound_path,game_over_cntrl_False))
game_over_cntrl_False.set_volume(0.2)


game_over_cntrl_True = "kl-peach-game-over-ii-135684.mp3"
game_over_cntrl_True = pygame.mixer.Sound(os.path.join(sound_path,game_over_cntrl_True))
game_over_cntrl_True.set_volume(0.2)


jetski_sound = "distant-small-boat-returning-to-marina-18705.mp3"
jetski_sound = pygame.mixer_music.load(os.path.join(sound_path,jetski_sound))
pygame.mixer.music.set_volume(1)


impact_sound = "splash-by-blaukreuz-6261.mp3"
impact_sound = pygame.mixer.Sound(os.path.join(sound_path,impact_sound))
impact_sound.set_volume(0.4)

health0 = "game-over-arcade-6435.mp3"
health0 = pygame.mixer.Sound(os.path.join(sound_path,health0))
health0.set_volume(1)

red_heart_sound = "health-pickup-6860.mp3"
red_heart_sound = pygame.mixer.Sound(os.path.join(sound_path,red_heart_sound))
red_heart_sound.set_volume(1)

gold_heart_sound = "harp-glissando-ascending-short-103885.mp3"
gold_heart_sound = pygame.mixer.Sound(os.path.join(sound_path,gold_heart_sound))
gold_heart_sound.set_volume(1)

white_heart_sound = "eagle-scream-112940.mp3"
white_heart_sound = pygame.mixer.Sound(os.path.join(sound_path,white_heart_sound))
white_heart_sound.set_volume(1)
white_heart_sound.set_volume(1)

# ------------------------

class Motorcycle(object):
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.img)

class barriers(object):
    barrier_list = [lifebuoy,lifebuoy,lifebuoy,lifebuoy_donat,lifebuoy_donat,sea_ball,sea_ball,tornado,lifebuoy,lifebuoy,lifebuoy,lifebuoy_donat,lifebuoy_donat,sea_ball,sea_ball,tornado,gold_heart,red_heart,white_heart]
    #barrier_list = [white_heart,white_heart,white_heart,white_heart,white_heart,white_heart]
    def __init__(self,x, y, index):
        #self.screen = screen
        self.x = x
        self.y = y
        #self.index = index
        self.barrier_img = None
        self.barrier_img = self.barrier_list[index]
        self.barriers = []
        #self.mask = pygame.mask.from_surface(self.barrier_img)
        self.img_height = self.barrier_img.get_height()
        self.img_width = self.barrier_img.get_width()

    def forward(self,speed):
        self.y = self.y + speed
        self.mask = pygame.mask.from_surface(self.barrier_img)

    def draw(self,screen,speed):
        barriers.forward(self,speed)
        screen.blit(self.barrier_img, (self.x, self.y))



def carpisma(obj):
    fark_x = obj.x - motorcycle_locationx
    fark_y = obj.y - motorcycle_locationy
    return motorcycle_mask.overlap(obj.mask, (fark_x,fark_y)) != None


def score_saves(score):
    file_name = "Score.txt"  # Skorların kaydedileceği dosyanın adı
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Skriptin bulunduğu dizini al

    score_path = os.path.join(script_directory, file_name)

    try:
        with open(score_path, "a") as file:
            file.write(str(score) + "\n")  # Skoru dosyaya yaz ve yeni satıra geç
        print("Skor başarıyla kaydedildi!")
    except IOError:
        print("Dosya açma veya yazma hatası oluştu.")

def score_save(score):
    file_name = "Score.txt"  # Skorların kaydedileceği dosyanın adı
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Skriptin bulunduğu dizini al
    score_path = os.path.join(script_directory, file_name)

    try:
        with open(score_path, "r") as file:
            saved_score = int(file.read().strip())  # Dosyadaki skoru oku

        if score > saved_score:
            with open(score_path, "w") as file:
                file.write(str(score))  # Yeni skoru dosyaya yaz
            print("Yeni skor kaydedildi: {}".format(score))
        else:
            print("Mevcut skor daha yüksek. Skor kaydedilmedi.")

        print("Kaydedilen skor: {}".format(score))
    except FileNotFoundError:
        with open(score_path, "w") as file:
            file.write(str(score))  # İlk skoru dosyaya yaz
        print("Yeni skor kaydedildi: {}".format(score))


dusmanlar = []
health = 3
score = 0
barrier_index_and = 1
game_over_cntrl = False
sleep_cntrl = True
impact_ctrl = False
keys_ctrl = False
fly_cntrl = False
music_cntrl = True
MIN_DISTANCE = 50
loop = 0
fly_time = 0
speed = 3
barrier_number = 1
motorcycle = jetski
game_over_time = 0
game_exit = False
def start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos):
    global motorcycle_locationx
    global motorcycle_locationy
    global keys_ctrl
    global wave_index
    global game_over_index
    global motorcycle_mask
    global health
    global score
    global game_over_cntrl
    global sleep_cntrl
    global impact_index
    global barrier_index
    global impact_ctrl
    global impactx
    global impacty
    global impact_animation
    global dusmanlar
    global barrier_index_and
    global loop
    global speed
    global barrier_number
    global motorcycle
    global fly_cntrl
    global fly_time
    global game_over_time
    global music_cntrl
    global game_exit
    if music_cntrl == True:
        game_over_cntrl_False.play()
        pygame.mixer.music.play()
    music_cntrl = False
    if game_over_cntrl == False:

        if display_again%100==0:

            for i in range(barrier_number):

                new_x = random.randrange(27, background_width - 27)
                new_y = random.randrange(-600, -50)
                # Check if there is a barrier too close to this position
                if any(math.sqrt((x.x - new_x) ** 2 + (x.y - new_y) ** 2) < MIN_DISTANCE for x in dusmanlar):
                    continue  # If there is, generate a new position and check again
                # If there isn't, create the new barrier
                barrier_index = random.randint(0, barrier_index_and-1)

                barrier = barriers(new_x, new_y, barrier_index)
                barrier_index_and = (len(barrier.barrier_list))
                dusmanlar.append(barrier)

        screen.blit(blue_background, (27, 40))

        if motorcycle_locationy > (background_height-motorcycle_height):
            motorcycle_locationy-=1
            if  motorcycle_locationy == (background_height-motorcycle_height):
                keys_ctrl = True
        if motorcycle == jetski:
            if keys[pygame.K_d] and (motorcycle_locationx<background_width-motorcycle_width+26.5) and keys_ctrl==True:
                motorcycle_locationx+=3
            if keys[pygame.K_a] and (motorcycle_locationx>26.5) and keys_ctrl==True:
                motorcycle_locationx-=3
        if motorcycle == motorcycle_fly:
            if keys[pygame.K_d] and (motorcycle_locationx<background_width-motorcycle_width-50) and keys_ctrl==True:
                motorcycle_locationx+=3
            if keys[pygame.K_a] and (motorcycle_locationx>30-77) and keys_ctrl==True:
                motorcycle_locationx-=3

        if fly_cntrl == False:
            screen.blit(wave_list[wave_index], (motorcycle_locationx, motorcycle_locationy+60))
        if display_again%6==0:
            wave_index+=1
        if wave_index == 2:
            wave_index=0

        for x in dusmanlar:
            x.draw(screen,speed)
            motorcycle_mask = pygame.mask.from_surface(motorcycle)

            if carpisma(x) and fly_cntrl == False:
                print("Gerçekleşti")

                impact_ctrl = True
                impactx, impacty = x.x + x.img_width / 2, x.y + x.img_height / 2
                impact_index = 0

                if x.barrier_img == red_heart:
                    red_heart_sound.play()
                    health += 1
                    impact_animation = impact_list_heart
                elif x.barrier_img == gold_heart:
                    gold_heart_sound.play()
                    impact_animation = impact_list_gold

                elif x.barrier_img == white_heart:
                    white_heart_sound.play()
                    impact_animation = impact_list_white
                    #impact_animation = impact_list_gold
                    motorcycle = motorcycle_fly
                    motorcycle_locationx -= 77
                    fly_cntrl = True
                else:
                    impact_sound.play()
                    health-=1
                    impact_animation = impact_list_barrier
                dusmanlar.remove(x)


                if health == 0:
                    health0.play()
                    game_over_cntrl = True
                    impact_index = 8

            if x.y >= 40+background_height:
                dusmanlar.remove(x)


            #if display_again%99 == 0:
                #score+=1

        if impact_index <= 8 and impact_ctrl==True:
            impact = impact_animation[impact_index]
            if impact_animation == impact_list_gold:
                dusmanlar = []
            screen.blit(impact, (impactx-impact.get_width()/2 , impacty-impact.get_height()/2))
            impact_index += 1
            if impact_index == 7:
                impact_ctrl = False

        if fly_cntrl == True :
            fly_time += 1

        if fly_time == 250:
            fly_time = 0
            fly_cntrl = False
            motorcycle = jetski
            motorcycle_locationx += 77


        screen.blit(motorcycle, (motorcycle_locationx,motorcycle_locationy))
        font1 = pygame.font.SysFont("Arial", 15, bold= True)
        health_write = font1.render(f"Health: {health}", 1, (0, 0, 0))
        score_write = font1.render(f"Score(m): {score}", 1, (0, 0, 0))
        screen.blit(health_write, (30, 45))
        screen.blit(score_write, (110, 45))


    elif game_over_cntrl == True:
        if game_over_time == 99:
            game_over_cntrl_True.play()
            score_save(score)
        if game_over_time < 100:
            game_over_time += 1
        #print(game_over_time)
        file_name = "Score.txt"  # Skorların kaydedildiği dosyanın adı
        script_directory = os.path.dirname(os.path.abspath(__file__))  # Skriptin bulunduğu dizini al
        score_path = os.path.join(script_directory, file_name)
        with open(score_path, "r") as file:
            current_score = int(file.read().strip())  # Dosyadan mevcut skoru oku
        #print("Mevcut skor: {}".format(current_score))


    if game_over_time == 100:
        game_over_cntrl_False.stop()
        pygame.mixer_music.stop()
        #print(score)
        sleep_cntrl = False


        screen.blit(game_over_list[game_over_index], (26.5, 40))
        font1 = pygame.font.SysFont("Arial", 15)
        highest_score_write = font1.render(f"Highest Score: {current_score}", 1, (0, 0, 0))
        new_score_write = font1.render(f"New Score: {score}", 1, (0, 0, 0))
        screen.blit(signboard, (118, 335))
        screen.blit(highest_score_write, (125, 356))
        screen.blit(new_score_write, (125, 340))

        red_heart_write = font1.render(f"health", 1, (0, 0, 0))
        white_heart_write = font1.render(f"fly", 1, (0, 0, 0))
        gold_heart_write = font1.render(f"clear", 1, (0, 0, 0))
        screen.blit(red_heart_write, (115, 391))
        screen.blit(white_heart_write, (180, 391))
        screen.blit(gold_heart_write, (230, 391))

        if display_again % 6 == 0:
            game_over_index += 1
        if game_over_index == 3:
            game_over_index = 0

        if 201<=mouse_pos[0]<=228 and 300<=mouse_pos[1]<=330:
            screen.blit(again_button, (201, 300))
            if left_click == True:
                game_over_time = 0
                game_over_cntrl = False
                dusmanlar = []
                health = 3
                score = 0
                barrier_index_and = 1
                game_over_cntrl = False
                sleep_cntrl = True
                impact_ctrl = False
                keys_ctrl = False
                pygame.mixer.music.play()
                loop = 0
                speed = 3
                barrier_number = 1
                motorcycle_locationx, motorcycle_locationy = (background_width / 2 - motorcycle_width / 2 + 26.5), (background_height + motorcycle_height)
                game_over_cntrl_True.stop()
                game_over_cntrl_False.play()
                pygame.mixer_music.play()

        if 141<=mouse_pos[0]<=181 and 309<=mouse_pos[1]<=324:
            screen.blit(back_button, (141,309))
            if left_click == True:
                game_exit = True
                game_over_cntrl_True.stop()


    loop+=1
    if loop == 120:
        speed += 0.05
        loop = 0
        if game_over_cntrl == False:
            score += 1
        if score%5 == 0:
            barrier_number += 1

    print("Motor çalışıyor",game_exit)
def return_menu():
    return game_exit
def return_false():
    global game_exit
    game_exit = False
def reset():
    global game_over_time
    global game_over_cntrl
    global dusmanlar
    global health
    global score
    global barrier_index_and
    global sleep_cntrl
    global impact_ctrl
    global keys_ctrl
    global loop
    global speed
    global barrier_number
    global motorcycle_locationx
    global motorcycle_locationy


    game_over_time = 0
    game_over_cntrl = False
    dusmanlar = []
    health = 3
    score = 0
    barrier_index_and = 1
    sleep_cntrl = True
    impact_ctrl = False
    keys_ctrl = False
    pygame.mixer.music.play()
    loop = 0
    speed = 3
    barrier_number = 1
    motorcycle_locationx, motorcycle_locationy = (background_width / 2 - motorcycle_width / 2 + 26.5), (background_height + motorcycle_height)
    game_over_cntrl_True.stop()
    game_over_cntrl_False.play()
    pygame.mixer_music.play()

























