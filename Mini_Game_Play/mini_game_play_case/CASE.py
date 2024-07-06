import pygame
import os
pygame.init()

self_screen_widht , self_screen_height = pygame.display.Info().current_w , pygame.display.Info().current_h
screen_widht,screen_height =self_screen_widht/4.8 , self_screen_height/1.8#400,600

script_directory = os.path.dirname(os.path.abspath(__file__))
# -------------------------------------(Mini Game Player CASE Pictures)-------------------------
outer_case_path = os.path.join(script_directory, "outer_case")

red_outher_case = "red_outher_case.png"
red_outer_case = pygame.image.load(os.path.join(outer_case_path, red_outher_case))
#self.red_outer_case = pygame.transform.scale(red_outer_case, (self.screen_widht, self.screen_height))

# ------------------------
# arrow_keys_path = "C:\\Users\Mert6\\PycharmProjects\\PyCharm Kodlama Klasörüm\\Mini_Oyun_Oynatıcı_Dosyalar\\mini_game_play_case\\arrow_keys"#os.path.join(os.getcwd(),'arrow_keys')
arrow_keys_path = os.path.join(script_directory, "arrow_keys")

arrow_keys = "yön_tuşları.png"
arrow_keys = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys))
#self.arrow_keys = pygame.transform.smoothscale(arrow_keys, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_w = "yön_tuşları_w.png"
arrow_keys_w = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_w))
#self.arrow_keys_w = pygame.transform.scale(arrow_keys_w, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_w_grey = "yön_tuşları_w_grey.png"
arrow_keys_w_grey = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_w_grey))
#self.arrow_keys_w_grey = pygame.transform.scale(arrow_keys_w_grey, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_s = "yön_tuşları_s.png"
arrow_keys_s = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_s))
#self.arrow_keys_s = pygame.transform.scale(arrow_keys_s, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_s_grey = "yön_tuşları_s_grey.png"
arrow_keys_s_grey = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_s_grey))
#self.arrow_keys_s_grey = pygame.transform.scale(arrow_keys_s_grey, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_a = "yön_tuşları_a.png"
arrow_keys_a = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_a))
#self.arrow_keys_a = pygame.transform.scale(arrow_keys_a, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_a_grey = "yön_tuşları_a_grey.png"
arrow_keys_a_grey = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_a_grey))
#self.arrow_keys_a_grey = pygame.transform.scale(arrow_keys_a_grey, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_d = "yön_tuşları_d.png"
arrow_keys_d = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_d))
#self.arrow_keys_d = pygame.transform.scale(arrow_keys_d, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))

arrow_keys_d_grey = "yön_tuşları_d_grey.png"
arrow_keys_d_grey = pygame.image.load(os.path.join(arrow_keys_path, arrow_keys_d_grey))
#self.arrow_keys_d_grey = pygame.transform.scale(arrow_keys_d_grey, ((self.screen_widht / 3.252032520325203), (self.screen_height / 4.878048780487805)))
# ------------------------
space_button_path = os.path.join(script_directory, "space_button")

space_button_black = "space_buton.png"
space_button_black = pygame.image.load(os.path.join(space_button_path, space_button_black))
#self.space_button_black = pygame.transform.scale(space_button_black, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))

space_button_white = "space_buton_white.png"
space_button_white = pygame.image.load(os.path.join(space_button_path, space_button_white))
#self.space_button_white = pygame.transform.scale(space_button_white, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))

space_button_grey = "space_buton_grey.png"
space_button_grey = pygame.image.load(os.path.join(space_button_path, space_button_grey))
#self.space_button_grey = pygame.transform.scale(space_button_grey, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))
# ------------------------
e_button_path = os.path.join(script_directory, "E_button")

e_button_black = "E_buton.png"
e_button_black = pygame.image.load(os.path.join(e_button_path, e_button_black))
#self.e_button_black = pygame.transform.scale(e_button_black, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))

e_button_white = "E_buton_white.png"
e_button_white = pygame.image.load(os.path.join(e_button_path, e_button_white))
#self.e_button_white = pygame.transform.scale(e_button_white, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))

e_button_grey = "E_buton_grey.png"
e_button_grey = pygame.image.load(os.path.join(e_button_path, e_button_grey))
#self.e_button_grey = pygame.transform.scale(e_button_grey, ((self.screen_widht / 5.714285714285714), (self.screen_height / 8.571428571428571)))
# ------------------------
reset_button_path = os.path.join(script_directory, 'reset_button')

reset_button_black = "RESET_BUTON.png"
reset_button_black = pygame.image.load(os.path.join(reset_button_path, reset_button_black))
#self.reset_button_black = pygame.transform.scale(reset_button_black, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))

reset_button_white = "RESET_BUTON_white.png"
reset_button_white = pygame.image.load(os.path.join(reset_button_path, reset_button_white))
#self.reset_button_white = pygame.transform.scale(reset_button_white, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))

reset_button_grey = "RESET_BUTON_grey.png"
reset_button_grey = pygame.image.load(os.path.join(reset_button_path, reset_button_grey))
#self.reset_button_grey = pygame.transform.scale(reset_button_grey, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))
# ------------------------
start_button_path = os.path.join(script_directory, 'start_button')

start_button_black = "START_BUTON.png"
start_button_black = pygame.image.load(os.path.join(start_button_path, start_button_black))
#self.start_button_black = pygame.transform.scale(start_button_black, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))

start_button_white = "START_BUTON_white.png"
start_button_white = pygame.image.load(os.path.join(start_button_path, start_button_white))
#self.start_button_white = pygame.transform.scale(start_button_white, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))

start_button_grey = "START_BUTON_grey.png"
start_button_grey = pygame.image.load(os.path.join(start_button_path, start_button_grey))
#self.start_button_grey = pygame.transform.scale(start_button_grey, ((self.screen_widht / 5.633802816901408), (self.screen_height / 54.54545454545455)))
# -------------------------------------------------------------------------------------------

def start(screen,left_click,keys,mouse_pos):
    screen.blit(red_outer_case, (0, 0))
    # ----------
    arrwkys = True
    w_white = False
    a_white = False
    d_white = False
    s_white = False
    if ((70<mouse_pos[0]<150) and (445<mouse_pos[1]<(490))):
        screen.blit(arrow_keys_w_grey, (25,445))
        arrwkys = False
        if left_click == True:
            w_white = True

    if ((100<mouse_pos[0]<220) and (490 <mouse_pos[1]< 520)):
        screen.blit(arrow_keys_d_grey, ((screen_widht/16), (screen_height/1.348314606741573)))
        arrwkys = False
        if left_click == True:
            d_white = True
    if ((25<mouse_pos[0]<70) and (490<mouse_pos[1]<520)):
        screen.blit(arrow_keys_a_grey, ((screen_widht/16), (screen_height/1.348314606741573)))
        arrwkys = False
        if left_click == True:
            a_white = True

    if ((70<mouse_pos[0]<100) and (515<mouse_pos[1]<565)):
        screen.blit(arrow_keys_s_grey, ((screen_widht/16), (screen_height/1.348314606741573)))
        arrwkys = False
        if left_click == True:
            s_white = True


    # ----------
    if keys[pygame.K_w] or w_white == True:
        screen.blit(arrow_keys_w, (25,445))
        arrwkys = False

    if keys[pygame.K_d]or d_white == True:
        screen.blit(arrow_keys_d, (25,445))
        arrwkys = False

    if keys[pygame.K_a] or a_white == True:
        screen.blit(arrow_keys_a, (25,445))
        arrwkys = False

    if keys[pygame.K_s] or s_white == True:
        screen.blit(arrow_keys_s, (25,445))
        arrwkys = False

    if arrwkys == True:
        screen.blit(arrow_keys, (25,445))
    #----------
    space_cntrl = False
    space_with_cntrl = False
    if ((205<mouse_pos[0]<(275)) and (470<mouse_pos[1]<(540))):
        screen.blit(space_button_grey, (205,470))
        space_cntrl = True
        if left_click == True:
            space_with_cntrl = True

    if keys[pygame.K_SPACE] or space_with_cntrl == True:
        screen.blit(space_button_white, (205,470))
        space_cntrl = True

    if space_cntrl == False:
        screen.blit(space_button_black, (205, 470))
    # ----------
    e_cntrl = False
    e_with_ctrl = False
    if ((295<mouse_pos[0]<(365)) and (470<mouse_pos[1]<(540))):
        screen.blit(e_button_grey, (295, 470))
        e_cntrl = True
        if left_click == True:
            e_with_ctrl = True

    if keys[pygame.K_e] or e_with_ctrl == True:
        screen.blit(e_button_white, (295, 470))
        e_cntrl = True
    if e_cntrl == False:
        screen.blit(e_button_black, (295, 470))
    # ----------
    if (215 < mouse_pos[0] < 286) and (570< mouse_pos[1] <581):
        if left_click == True:
            screen.blit(reset_button_white,(215, 570))
        else:
            screen.blit(reset_button_grey,(215, 570))

    else:
        screen.blit(reset_button_black, (215, 570))
    # ----------
    if 130< mouse_pos[0] < (201) and (570< mouse_pos[1] <581):
        if left_click == True:
            screen.blit(start_button_white, (130, 570))
        else:
            screen.blit(start_button_grey, (130, 570))
    else:
        screen.blit(start_button_black, (130, 570))






