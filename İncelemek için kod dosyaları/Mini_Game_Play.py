import sys
import ursina
import pygame
import os
import importlib.util
from sys import exit

# Script'in bulunduğu klasör yolunu belirle
script_directory = os.path.dirname(os.path.abspath(__file__))
#------------------(CASE MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
CASE_directory = os.path.join(script_directory, "mini_game_play_case")
# Modülün tam yolunu oluştur
CASE_module_path = os.path.join(CASE_directory, "CASE.py")
# Modülü yükle
spec = importlib.util.spec_from_file_location("CASE", CASE_module_path)
CASE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CASE)
#-----------------------------------------------------

#"""
#------------------(FROG MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
FROG_directory = os.path.join(script_directory, "FROG")
# Modülün tam yolunu oluştur
FROG_module_path = os.path.join(FROG_directory, "FROG_codes.py")
# Modülü yükle
FROG_spec = importlib.util.spec_from_file_location("FROG", FROG_module_path)
FROG = importlib.util.module_from_spec(FROG_spec)
FROG_spec.loader.exec_module(FROG)
#-----------------------------------------------------

#------------------(MOTORCYCLE MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
MOTORCYCLE_directory = os.path.join(script_directory, "MOTORCYCLE")
# Modülün tam yolunu oluştur
MOTORCYCLE_module_path = os.path.join(MOTORCYCLE_directory, "motorcycle_codes.py")
# Modülü yükle
MOTORCYCLE_spec = importlib.util.spec_from_file_location("MOTORCYCLE", MOTORCYCLE_module_path)
MOTORCYCLE = importlib.util.module_from_spec(MOTORCYCLE_spec)
MOTORCYCLE_spec.loader.exec_module(MOTORCYCLE)
#-----------------------------------------------------

#------------------(ROCK PAPER SCİSSORS MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
Rock_Paper_Scissors_directory = os.path.join(script_directory, "Rock Paper Scissors")
# Modülün tam yolunu oluştur
Rock_Paper_Scissors_module_path = os.path.join(Rock_Paper_Scissors_directory, "rock_paper_scissors_codes.py")
# Modülü yükle
Rock_Paper_Scissors_spec = importlib.util.spec_from_file_location("Rock Paper Scissors", Rock_Paper_Scissors_module_path)
Rock_Paper_Scissors = importlib.util.module_from_spec(Rock_Paper_Scissors_spec)
Rock_Paper_Scissors_spec.loader.exec_module(Rock_Paper_Scissors)
#-----------------------------------------------------

#------------------(FARM MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
Farm_directory = os.path.join(script_directory, "FARM")
# Modülün tam yolunu oluştur
Farm_module_path = os.path.join(Farm_directory, "farm_codes.py")
# Modülü yükle
Farm_spec = importlib.util.spec_from_file_location("FARM", Farm_module_path)
FARM = importlib.util.module_from_spec(Farm_spec)
Farm_spec.loader.exec_module(FARM)
#-----------------------------------------------------

#------------------(MENU MODULE)----------------------
# CASE.py'nin bulunduğu klasör yolunu belirle
Menu_directory = os.path.join(script_directory, "Menu")
# Modülün tam yolunu oluştur
Menu_module_path = os.path.join(Menu_directory, "Codes(2354462075852).py")
# Modülü yükle
Menu_spec = importlib.util.spec_from_file_location("Menu", Menu_module_path)
Menu = importlib.util.module_from_spec(Menu_spec)
Menu_spec.loader.exec_module(Menu)
#-----------------------------------------------------


pygame.init()

#------------------------#                                                            #------------------------#
self_screen_widht , self_screen_height = pygame.display.Info().current_w , pygame.display.Info().current_h
screen_widht,screen_height =400,600#self_screen_widht/4.8 , self_screen_height/1.8#400,600
#print(self_screen_widht,self_screen_height)
screen = pygame.display.set_mode((screen_widht,screen_height))
pygame.display.set_caption("Mini Game Player")
logo = pygame.image.load("Logo/TmS_logo.png")
pygame.display.set_icon(logo)
#------------------------#                                                            #------------------------#

game_list = [FARM,MOTORCYCLE,Rock_Paper_Scissors,FROG]

clock = pygame.time.Clock()
FPS = 60
display_again = 1
reset_status = False
game = MOTORCYCLE
while True:

    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    left_click = False
    one_down = False
    key_name = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
        if event.type == pygame.KEYDOWN:
            one_down = True
            key_name = pygame.key.name(event.key)



    if (game.return_menu() == True):#menünün ilk den sonraki çalışma sorgusu
        Menu.ready_false()
        Menu.start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos)
        reset_status = True

    elif ((Menu.game_num_ctrl()[1]) == False):#menünün ilk çalışması
        Menu.start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos)

    if Menu.game_num_ctrl()[1] == True:
        game = game_list[Menu.game_num_ctrl()[0]]

    if (Menu.game_num_ctrl()[1] == True) and (Menu.menu_status() == True):
        game.return_false()
        if reset_status == True:
            reset_status = False
            game.reset()

            print("reset")
            print(game)
        game_list[int(Menu.game_num_ctrl()[0])].start(screen, keys, one_down, key_name, display_again, left_click,mouse_pos)
    CASE.start(screen,left_click,keys,mouse_pos)


    pygame.display.flip()
    display_again += 1

# oyundan çıkıp balka oyuna girince yine jetski resetkenip müziği çalıyor sorun