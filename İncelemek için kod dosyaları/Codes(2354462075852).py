import os
import pygame

pygame.init()


#-----------------------------------------------------------------------------------------------------------------------
script_directory = os.path.dirname(os.path.abspath(__file__))
# ------------------------(BACKGROUND)-----------------------------------
Pictures_path = os.path.join(script_directory, "Pictures(2354462075852)")

backgorund = pygame.image.load(os.path.join(Pictures_path, "background.png"))

game_bg_yellow = pygame.image.load(os.path.join(Pictures_path, "game_bg_yellow.png"))
game_bg_green = pygame.image.load(os.path.join(Pictures_path, "game_bg_green.png"))
game_bg_blue = pygame.image.load(os.path.join(Pictures_path, "game_bg_blue.png"))
game_bg_red = pygame.image.load(os.path.join(Pictures_path, "game_bg_red.png"))

write_bg_purple = pygame.image.load(os.path.join(Pictures_path, "write_bg_purple.png"))

play_button = pygame.image.load(os.path.join(Pictures_path, "play.png"))

character1 = pygame.image.load(os.path.join(Pictures_path, "character_y_negative_1.png"))
character2 = pygame.image.load(os.path.join(Pictures_path, "character_y_negative_2.png"))

motorcycle1 = pygame.image.load(os.path.join(Pictures_path, "motorcycle1.png"))
motorcycle2 = pygame.image.load(os.path.join(Pictures_path, "motorcycle2.png"))
motorcycle3 = pygame.image.load(os.path.join(Pictures_path, "motorcycle3.png"))

hand1 = pygame.image.load(os.path.join(Pictures_path, "hand1.png"))
hand2 = pygame.image.load(os.path.join(Pictures_path, "hand2.png"))
hand3 = pygame.image.load(os.path.join(Pictures_path, "hand3.png"))

frog1 = pygame.image.load(os.path.join(Pictures_path, "frog1.png"))
frog2 = pygame.image.load(os.path.join(Pictures_path, "frog2.png"))
frog3 = pygame.image.load(os.path.join(Pictures_path, "frog3.png"))
frog4 = pygame.image.load(os.path.join(Pictures_path, "frog4.png"))
frog5 = pygame.image.load(os.path.join(Pictures_path, "frog5.png"))
frog6 = pygame.image.load(os.path.join(Pictures_path, "frog6.png"))
frog7 = pygame.image.load(os.path.join(Pictures_path, "frog7.png"))
frog8 = pygame.image.load(os.path.join(Pictures_path, "frog8.png"))
frog9 = pygame.image.load(os.path.join(Pictures_path, "frog9.png"))

Sound_path = os.path.join(script_directory, "Sound(2354462075852)")
choice_sound = "happy-pop-3-185288.mp3"
choice_sound = pygame.mixer.Sound(os.path.join(Sound_path,choice_sound))
choice_sound.set_volume(0.3)
ready_sound = "retro-video-game-coin-pickup-38299.mp3"
ready_sound = pygame.mixer.Sound(os.path.join(Sound_path,ready_sound))
ready_sound.set_volume(0.3)
#-----------------------------------------------------------------------------------------------------------------------



class Game_Choice():
    def __init__(self,write,write_bg,bg,img_list,x_cor,y_cor):
        self.bg = bg
        self.img_list = img_list
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.img_num = 0
        self.write_bg = write_bg
        self.write = write
    def blit_func(self,screen,display_again,dividing):
        #------------------------------------------------------------------------------------#
        bg_xcor,bg_ycor = 27+self.x_cor,40+self.y_cor
        screen.blit(self.bg,(bg_xcor,bg_ycor))              #Küçük resim arka planı gösterimi
        # -----------------------------------------------------------------------------------#
        write_bg_xcor,write_bg_ycor = ( bg_xcor + self.bg.get_width() ) , ( bg_ycor+(self.bg.get_height()/2)-(self.write_bg.get_height()/2) )
        screen.blit(self.write_bg,(write_bg_xcor,write_bg_ycor))    #Yazı arkaplanı
        # --------------------------------------------------------------------------------------------#
        font = pygame.font.SysFont("Arial", 15, bold=True)
        write = font.render(self.write,1,(255,255,255))
        write_xcor, write_ycor = (write_bg_xcor + (self.write_bg.get_width() - write.get_width()) / 2) , (write_bg_ycor + (self.write_bg.get_height() - write.get_height()) / 2)
        screen.blit(write, (write_xcor, write_ycor))
        # --------------------------------------------------------------------------------------------#
        if display_again%dividing == 0:
            self.img_num+=1
            if self.img_num == len(self.img_list):
                self.img_num = 0                            #Küçük resim animasyon ve gösterim

        img = self.img_list[self.img_num]

        img_xcor, img_ycor = ( bg_xcor+(self.bg.get_width()/2)-(img.get_width()/2) ) , ( bg_ycor+(self.bg.get_height()/2)-(img.get_height()/2) )
        screen.blit(img, (img_xcor,img_ycor))
        # ---------------------------------------------------------------------------------------------#

farm_game = Game_Choice("Farm(DEMO)",write_bg_purple,game_bg_green,[character1,character2],12,14)
motorcycle_game = Game_Choice("Jet Ski and Barriers",write_bg_purple,game_bg_blue,[motorcycle1,motorcycle2,motorcycle3],12,102)
rock_paper_scissors_game = Game_Choice("Rock Paper Scissors",write_bg_purple,game_bg_red,[hand1,hand2,hand1,hand3],12,190)
frog_game = Game_Choice("Frog",write_bg_purple,game_bg_blue,[frog1,frog2,frog3,frog4,frog5,frog6,frog7,frog8,frog8,frog9,frog9],12,278)


def Play_Button(screen,x_cor,y_cor):
    screen.blit(play_button, (x_cor,y_cor))
    font = pygame.font.SysFont("Arial", 15, bold=True)
    write = font.render("Play", 1, (0, 0, 0))
    screen.blit(write,(x_cor+25,y_cor-1))

game_list = [farm_game,motorcycle_game,rock_paper_scissors_game,frog_game]
game_num = 0
ready = False
menu_exit = False
def start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos):
    # --------------------------------------------------------------------------------------------------------
    global menu_exit
    global game_num
    global ready
    menu_exit = False
    # --------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------
    screen.blit(backgorund,(27,40))

    farm_game.blit_func(screen,display_again,10)
    motorcycle_game.blit_func(screen,display_again,10)
    rock_paper_scissors_game.blit_func(screen,display_again,20)
    frog_game.blit_func(screen,display_again,15)
    # --------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------
    selected_game = game_list[game_num]
    play_ycor = ((selected_game.y_cor + game_bg_green.get_height() / 2) - (play_button.get_height() / 2) + 40)
    if (one_down == True) and ((key_name == "s") or (key_name == "down")):
        choice_sound.play()
        game_num += 1
        if game_num == len(game_list):
            game_num = 0
    if (one_down == True) and ((key_name == "w") or (key_name == "up")):
        choice_sound.play()
        game_num -= 1
        if game_num == -1:
            game_num = len(game_list)-1
    Play_Button(screen,290,play_ycor)
    if one_down == True and (key_name == "space"):
        ready_sound.play()

    #--------------------------------------------------------------------------------------------------------

    if one_down == True and (key_name == "space"):
        ready = True
        menu_exit = True
    #--------------------------------------------------------------------------------------------------------
    print("menü çalışıyor",menu_exit)
def game_num_ctrl():
    return [game_num,ready]
def ready_false():
    global ready
    ready = False
def menu_status():
    return menu_exit





