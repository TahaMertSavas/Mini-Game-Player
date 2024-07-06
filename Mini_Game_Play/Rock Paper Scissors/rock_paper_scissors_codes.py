import os
import pygame
import random


#-----------------------------------------------------------------------------------------------------------------------
script_directory = os.path.dirname(os.path.abspath(__file__))
# ------------------------(BACKGROUND)
background_path = os.path.join(script_directory, "background18")

grey_background = "grey_background.png"
grey_background = pygame.image.load(os.path.join(background_path, grey_background))
background_width,background_height = grey_background.get_size()
#-------------------------------------
hands_path = os.path.join(script_directory, "Hand18")

rock1 = "rock1.png"
rock1 = pygame.image.load(os.path.join(hands_path, rock1))
rock1_width,rock1_height = rock1.get_size()

rock2 = "rock2.png"
rock2 = pygame.image.load(os.path.join(hands_path, rock2))
rock2_width,rock2_height = rock2.get_size()

paper1 = "paper1.png"
paper1 = pygame.image.load(os.path.join(hands_path, paper1))

paper2 = "paper2.png"
paper2 = pygame.image.load(os.path.join(hands_path, paper2))

scissors1 = "scissors1.png"
scissors1 = pygame.image.load(os.path.join(hands_path, scissors1))

scissors2 = "scissors2.png"
scissors2 = pygame.image.load(os.path.join(hands_path, scissors2))

#-------------------------------------
choice_path = os.path.join(script_directory, "Choice18")

choice_yellow = "choice.png"
choice_yellow = pygame.image.load(os.path.join(choice_path, choice_yellow))

paper_choice = "paper_choice.png"
paper_choice = pygame.image.load(os.path.join(choice_path, paper_choice))

rock_choice = "rock_choice.png"
rock_choice = pygame.image.load(os.path.join(choice_path, rock_choice))

scissors_choice = "scissors_choice.png"
scissors_choice = pygame.image.load(os.path.join(choice_path , scissors_choice))

score_table = "score.png"
score_table = pygame.image.load(os.path.join(choice_path, score_table))

tally = "tally.png"
tally = pygame.image.load(os.path.join(choice_path, tally))
#-------------------------------------
countdown_path = os.path.join(script_directory, "Countdown18")

one = "one.png"
one = pygame.image.load(os.path.join(countdown_path, one))

two = "two.png"
two = pygame.image.load(os.path.join(countdown_path, two))

three = "three.png"
three = pygame.image.load(os.path.join(countdown_path, three))

zero = "zero.png"
zero = pygame.image.load(os.path.join(countdown_path, zero))

countdown_list = [three,two,one,zero]
countdown_index = 0
#-------------------------------------
gold_path = os.path.join(script_directory, "Gold18")

gold1 = "gold1.png"
gold1 = pygame.image.load(os.path.join(gold_path, gold1))

gold2 = "gold2.png"
gold2 = pygame.image.load(os.path.join(gold_path, gold2))

gold3 = "gold3.png"
gold3 = pygame.image.load(os.path.join(gold_path, gold3))

gold4 = "gold4.png"
gold4 = pygame.image.load(os.path.join(gold_path, gold4))

gold5 = "gold5.png"
gold5 = pygame.image.load(os.path.join(gold_path, gold5))

gold6 = "gold1.png"
gold6 = pygame.image.load(os.path.join(gold_path, gold6))

yellow_list = [gold1,gold2,gold3,gold4,gold5,gold6]


red_gold1 = "red_gold1.png"
red_gold1 = pygame.image.load(os.path.join(gold_path, red_gold1))

red_gold2 = "red_gold2.png"
red_gold2 = pygame.image.load(os.path.join(gold_path, red_gold2))

red_gold3 = "red_gold3.png"
red_gold3 = pygame.image.load(os.path.join(gold_path, red_gold3))

red_gold4 = "red_gold4.png"
red_gold4 = pygame.image.load(os.path.join(gold_path, red_gold4))

red_gold5 = "red_gold5.png"
red_gold5 = pygame.image.load(os.path.join(gold_path, red_gold5))

red_gold6 = "red_gold1.png"
red_gold6 = pygame.image.load(os.path.join(gold_path, red_gold6))

red_list = [red_gold1,red_gold2,red_gold3,red_gold4,red_gold5,red_gold6]



#-------------------------------------
game_over_path = os.path.join(script_directory, "Game_Over18")

game_over_green = "game_over_green.png"
game_over_green = pygame.image.load(os.path.join(game_over_path, game_over_green))

game_over_red = "game_over_red.png"
game_over_red = pygame.image.load(os.path.join(game_over_path, game_over_red))

game_over_yellow = "game_over_yellow.png"
game_over_yellow = pygame.image.load(os.path.join(game_over_path, game_over_yellow))

game_over_purple = "game_over_purple.png"
game_over_purple = pygame.image.load(os.path.join(game_over_path, game_over_purple))

game_over_win_green = "game_over_win_green.png"
game_over_win_green = pygame.image.load(os.path.join(game_over_path, game_over_win_green))

game_over_win_red = "game_over_win_red.png"
game_over_win_red = pygame.image.load(os.path.join(game_over_path, game_over_win_red))

game_over_win_yellow = "game_over_win_yellow.png"
game_over_win_yellow = pygame.image.load(os.path.join(game_over_path, game_over_win_yellow))

game_over_win_purple = "game_over_win_purple.png"
game_over_win_purple = pygame.image.load(os.path.join(game_over_path, game_over_win_purple))

game_over_win_list = [game_over_win_green,game_over_win_red,game_over_win_yellow,game_over_win_purple]
game_over_lose_list = [game_over_green,game_over_red,game_over_yellow,game_over_purple]

again_button = "again_white.png"
again_button = pygame.image.load(os.path.join(game_over_path, again_button))

back_button = "back_white.png"
back_button = pygame.image.load(os.path.join(game_over_path, back_button))

#-------------------------------------
sound_path = os.path.join(script_directory, "Sound18")

choice_sound = "whoosh-transitions-sfx-01-118227.mp3"
choice_sound = pygame.mixer.Sound(os.path.join(sound_path,choice_sound))
choice_sound.set_volume(0.3)

round_win_sound = "new-level-142995.mp3"
round_win_sound = pygame.mixer.Sound(os.path.join(sound_path,round_win_sound))
round_win_sound.set_volume(0.3)

round_lose_sound = "invalid-selection-39351.mp3"
round_lose_sound = pygame.mixer.Sound(os.path.join(sound_path,round_lose_sound))
round_lose_sound.set_volume(0.3)

game_over_lose_sound = "kl-peach-game-over-i-132096.mp3"
game_over_lose_sound = pygame.mixer.Sound(os.path.join(sound_path,game_over_lose_sound))
game_over_lose_sound.set_volume(0.3)

game_over_win_sound = "game-bonus-144751.mp3"
game_over_win_sound = pygame.mixer.Sound(os.path.join(sound_path,game_over_win_sound))
game_over_win_sound.set_volume(0.3)

point_sound = "coin-collect-retro-8-bit-sound-effect-145251.mp3"
point_sound = pygame.mixer.Sound(os.path.join(sound_path,point_sound))
point_sound.set_volume(0.3)

#-------------------------------------


class hands(object):
    def __init__(self,index):
        self.hand_list = [rock1, paper1, scissors1, rock2, paper2, scissors2]
        self.index = index
        self.img = None
        self.x = None
        self.y = None
    def hand(self):
        self.img = self.hand_list[self.index]
        self.x = 27+background_width/2-self.img.get_width()/2
        if self.index in [3,4,5]:
            self.y = 40
        else:
            self.y = 40 + background_height - self.img.get_height()
    def blit(self,screen):
        hands.hand(self)
        screen.blit(self.img,(self.x,self.y))

class indicator(object):
    def __init__(self,img,screen,x,y):
        self.img = img
        self.screen = screen
        self.x = x
        self.y = y

    def blit(self):
        self.screen.blit(self.img,(self.x,self.y))

class Gold(object):
    def __init__(self,img_list,index,screen,x,y):
        self.img_list = img_list
        self.index = index
        self.screen = screen
        self.x = x
        self.y = y
        self.index = index

    def blit(self,display_again):
        if display_again % 5 == 0:
            self.index += 1
        if self.index == 6:
            self.index = 0
        self.screen.blit(self.img_list[self.index],(self.x,self.y))




paper_choice_button_x = 27 + background_width / 2 - paper_choice.get_width() / 2
choice_x = paper_choice_button_x-2
hand_index = 1
ready = False
choice_wait = True
computer_point = 0
peaople_point = 0
gold_animation_list = []
gold_list = None
gold_y = 157
gold_index = 0
gold_ctrl = False
person_score = 0
computer_score = 0
game_over_cntrl = False
game_over_index = 0
game_over_sound_ctrl = True
game_exit = False
def start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos):
    #----------->(GLOBAL)<-------------
    global choice_x
    global choice_wait
    global ready
    global hand_index
    global random_index
    global countdown_index
    global peaople_point
    global computer_point
    global gold_y
    global gold_list
    global gold_index
    global gold_ctrl
    global person_score
    global computer_score
    global gold_animation_list
    global game_over_cntrl
    global game_over_situation
    global game_over_index
    global sound
    global game_over_sound_ctrl
    global game_exit
    #----------------------------------
    if game_over_cntrl == False:
        screen.blit(grey_background, (27, 40))

        score_table_indicator = indicator(score_table, screen, 35,40 + background_height / 2 - score_table.get_height() / 2)
        score_table_indicator.blit()

        tally_indicator = indicator(tally, screen, 365 - tally.get_width(),40 + background_height / 2 - tally.get_height() / 2)
        tally_indicator.blit()
        #-------------------------(skill gösterme ve seçme kısmı)---------------------------------

        rock_choice_button = indicator(rock_choice, screen, paper_choice_button_x - 50, 370)
        paper_choice_button = indicator(paper_choice, screen, paper_choice_button_x, 370)
        scissors_choice_button = indicator(scissors_choice, screen, paper_choice_button_x + 50, 370)
        choice = indicator(choice_yellow, screen, choice_x, 368)

        if display_again%20==0:
            choice_wait = True
        if ready == False:
            if (keys[pygame.K_a]) and (choice_wait == True) and (choice_x > paper_choice_button_x -50):
                choice_wait = False
                hand_index-=1
                choice_x-=50
                choice_sound.play()
            if (keys[pygame.K_d]) and (choice_wait == True) and (choice_x < paper_choice_button_x):
                choice_wait = False
                choice_x+=50
                hand_index += 1
                choice_sound.play()



            rock_choice_button.blit()
            paper_choice_button.blit()
            scissors_choice_button.blit()
            choice.blit()
            #counter.blit()

        #-----------------------------------------------------------------------------------------

        # ------------------------------------(Geri Sayım)----------------------------------------
        countdown_num = indicator(countdown_list[countdown_index], screen, 27 + background_width / 2 - three.get_width() / 2,40 + background_height / 2 - three.get_height() / 2)
        if ready == False:
            if display_again % 70 == 0:
                countdown_index += 1
                if countdown_index == len(countdown_list):
                    countdown_index = 0
                    ready = True
                    gold_ctrl = True
            countdown_num.blit()
        #-----------------------------------------------------------------------------------------


        if ready==False:
            random_index = random.choice([3, 4, 5])


        if ready == True:
            computer = hands(random_index)
            person = hands(hand_index)
            computer.blit(screen)
            person.blit(screen)

        #-------------------------------------(Çarpışma yeri)-------------------------------------

        if ready == True:
            if (hand_index == 0):
                if (random_index == 3):
                    gold_ctrl = False
                elif (random_index == 4):
                    computer_point += 1
                    gold_list = red_list
                    sound = round_lose_sound
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
                elif (random_index == 5):
                    peaople_point+=1
                    gold_list = yellow_list
                    sound = round_win_sound
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
            elif (hand_index == 1):
                if (random_index == 3):
                    peaople_point+=1
                    gold_list = yellow_list
                    sound = round_win_sound
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
                elif (random_index == 4):
                    gold_ctrl = False
                elif (random_index == 5):
                    computer_point+=1
                    sound = round_lose_sound
                    gold_list = red_list
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
            elif (hand_index == 2):
                if (random_index == 3):
                    computer_point+=1
                    sound = round_lose_sound
                    gold_list = red_list
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
                elif (random_index == 4):
                    peaople_point+=1
                    gold_list = yellow_list
                    sound = round_win_sound
                    if gold_ctrl == True:
                        #gold_animation_list.append(gold)
                        if len(gold_animation_list) != 0:
                            gold_y += 53
                        #gold_ctrl = False
                elif (random_index == 5):
                    gold_ctrl = False

            # [rock1, paper1, scissors1, rock2, paper2, scissors2]
        #gold = indicator(gold_list[gold_index], screen, 336, gold_y)
        if gold_ctrl == True:
            gold = Gold(gold_list, gold_index, screen, 336, gold_y)
            sound.play()

            gold_animation_list.append(gold)
            gold_ctrl = False


        for gold_animation in gold_animation_list:
            gold_animation.blit(display_again)
        print(len(gold_animation_list))

        print("People {} --- Computer {}".format(peaople_point,computer_point))
        #-----------------------------------------------------------------------------------------

        if ready == True and display_again%200==0:
            ready=False

        if (len(gold_animation_list) == 3) and (ready == False):
            list_y = []
            list_r = []
            for color in gold_animation_list:
                if color.img_list == yellow_list:
                    list_y.append(color)
                elif color.img_list == red_list:
                    list_r.append(color)
            if len(list_y) > len(list_r):
                person_score += 1
            if len(list_y) < len(list_r):
                computer_score += 1
            gold_animation_list = []
            gold_y = 157
            point_sound.play()
        #-----------------------------------------------------------------------------------------

        font1 = pygame.font.SysFont("Arial", 30, bold=True)
        person_score_write = font1.render(f"{person_score}", 1, (255, 255, 255))
        computer_score_write = font1.render(f"{computer_score}", 1, (255, 255, 255))
        screen.blit(person_score_write, (45, 366))
        screen.blit(computer_score_write, (45, 49))

        if (person_score == 3) or (computer_score == 3) and (ready == False):
            game_over_cntrl = True
            if (person_score == 3):
                game_over_situation = "WIN"
            elif (computer_score == 3):
                game_over_situation = "LOSE"
        #-----------------------------------------------------------------------------------------

        #game_over_cntrl = True
        #game_over_situation = "LOSE"

    elif game_over_cntrl == True:

        if display_again % 6 == 0:
            game_over_index += 1
        if game_over_index == 4:
            game_over_index = 0

        if game_over_situation == "WIN":
            screen.blit(game_over_win_list[game_over_index],(27, 40))
            if game_over_sound_ctrl == True:
                game_over_win_sound.play()
                game_over_sound_ctrl = False
        elif game_over_situation == "LOSE":
            screen.blit(game_over_lose_list[game_over_index],(27, 40))
            if game_over_sound_ctrl == True:
                game_over_lose_sound.play()
                game_over_sound_ctrl = False
        if 215<=mouse_pos[0]<=241 and 300<=mouse_pos[1]<=330:
            screen.blit(again_button, (215, 301))
            if left_click == True:
                game_over_cntrl = False
                person_score = 0
                computer_score = 0
                game_over_sound_ctrl = True

        if 161<=mouse_pos[0]<=201 and 311<=mouse_pos[1]<=326:
            screen.blit(back_button, (161,311))
            if left_click == True:
                game_exit = True


        font1 = pygame.font.SysFont("Arial", 30, bold=True)
        person_score_write =   font1.render(f"You: {person_score}", 1, (255, 255, 255))
        computer_score_write = font1.render(f"Computer: {computer_score}", 1, (255, 255, 255))
        screen.blit(person_score_write, (45, 366))
        screen.blit(computer_score_write, (45, 49))

def return_menu():
    return game_exit
def return_false():
    global game_exit
    game_exit = False

def reset():
    global game_over_cntrl
    global person_score
    global computer_score
    global game_over_sound_ctrl
    game_over_cntrl = False
    person_score = 0
    computer_score = 0
    game_over_sound_ctrl = True