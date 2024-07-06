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

dot = "dot1.png"
dot = pygame.image.load(os.path.join(gold_path, dot))

dot_list = [dot,dot,dot,dot,dot,dot]


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


paper_choice_button_x = 27 + background_width / 2 - paper_choice.get_width() / 2
choice_x = paper_choice_button_x-2
time = 3
index = 0
counter_index = 3
ready = False
round_ctrl = False
scoreless = False
hand_index = 1
gold_index = 0
round = 0
person_score = 0
computer_score = 0
gold_list1 = dot_list
gold_list2 = dot_list
gold_list3 = dot_list
def start(screen,keys,display_again,left_click,mouse_pos):
    global index
    global time
    global counter_index
    global choice_x
    global ready
    global randomx
    global hand_index
    global gold_index
    global gold_list1
    global gold_list2
    global gold_list3
    global red_list
    global round
    global round_ctrl
    global person_score
    global computer_score
    global scoreless
    screen.blit(grey_background,(27,40))


    rock_choice_button = indicator(rock_choice, screen, paper_choice_button_x-50,370)
    paper_choice_button = indicator(paper_choice,screen,paper_choice_button_x,370)
    scissors_choice_button = indicator(scissors_choice, screen,paper_choice_button_x+50,370 )


    if keys[pygame.K_a] and display_again%7 == 0 and choice_x != paper_choice_button_x-52:
        choice_x -= 50
        if ready == False:
            hand_index -= 1
    if keys[pygame.K_d] and display_again%7 == 0 and choice_x != paper_choice_button_x+48:
        choice_x += 50
        if ready == False:
            hand_index+=1
    choice = indicator(choice_yellow,screen,choice_x,368)

    tally_indicator =   indicator(tally, screen,365-tally.get_width(),40 + background_height / 2 - tally.get_height() / 2)
    score_table_indicator = indicator(score_table, screen,35,40 + background_height / 2 - score_table.get_height() / 2)

    print(round)
    counter_list = [zero,one,two,three]
    counter = indicator(counter_list[counter_index], screen, 27 + background_width / 2 - three.get_width() / 2,40 + background_height / 2 - three.get_height() / 2)
    if display_again%70 == 0 and counter_index != 0 and ready == False:
        counter_index-=1

    if counter_index==0 and display_again%140==0:
        ready = True

    if ready==False:
        randomx = random.choice([3, 4, 5])

        #print(round)
    if ready == True:
        counter_index = 3
        #round_ctrl = True

        if display_again%400==0:
            ready = False


        computer = hands(randomx)
        person = hands(hand_index)
        computer.blit(screen)
        person.blit(screen)




        if randomx == 3 :
            if hand_index == 0:
                scoreless = True

            elif hand_index == 1:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = yellow_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = yellow_list
                if round == 1:
                    gold_list1 = yellow_list

            elif hand_index == 2:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = red_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = red_list
                if round == 1:
                    gold_list1 = red_list




        elif randomx == 4:
            if hand_index == 0:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = red_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = red_list
                if round == 1:
                    gold_list1 = red_list

            elif hand_index == 1:
                scoreless = True

            elif hand_index == 2:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = yellow_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = yellow_list
                if round == 1:
                    gold_list1 = yellow_list




        elif randomx == 5:
            if hand_index == 0:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = yellow_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = yellow_list
                if round == 1:
                    gold_list1 = yellow_list
            elif hand_index == 1:
                scoreless = False
                if gold_list2 != dot_list and round == 3:
                    gold_list3 = red_list
                if gold_list1 != dot_list and round == 2:
                    gold_list2 = red_list
                if round == 1:
                    gold_list1 = red_list


            elif hand_index == 2:
                scoreless = True

    if scoreless == False and ready == True:
        round += 1


    tally_indicator.blit()
    if display_again%5 == 0:
        gold_index+=1
    if gold_index == 6:
        gold_index = 0


    gold_indicator1 = indicator(gold_list1[gold_index], screen,336,157)
    gold_indicator2 = indicator(gold_list2[gold_index], screen, 336, 210)
    gold_indicator3 = indicator(gold_list3[gold_index], screen, 336, 263)
    gold_indicator1.blit()
    gold_indicator2.blit()
    gold_indicator3.blit()

    score_table_indicator.blit()
    if ready == False:
        rock_choice_button.blit()
        paper_choice_button.blit()
        scissors_choice_button.blit()
        choice.blit()
        counter.blit()

    if round == 4:
        round = 0
        if display_again % 100 == 0:
            gold_list1 = dot_list
            gold_list2 = dot_list
            gold_list3 = dot_list


    if (gold_list1 == yellow_list and gold_list2 == yellow_list) or (gold_list1 == yellow_list and gold_list3 == yellow_list) or (gold_list2 == yellow_list and gold_list3 == yellow_list) or (gold_list1 == yellow_list and gold_list2 == yellow_list and gold_list3 == yellow_list) and round == 3:

        person_score += 1

    elif (gold_list1 == red_list and gold_list2 == red_list) or (gold_list1 == red_list and gold_list3 == red_list) or (gold_list2 == red_list and gold_list3 == red_list) or (gold_list1 == red_list and gold_list2 == red_list and gold_list3 == red_list) or round == 3:

        computer_score += 1


    font1 = pygame.font.SysFont("Arial", 30, bold=True)
    person_score_write = font1.render(f"{person_score}", 1, (255, 255, 255))
    computer_score_write = font1.render(f"{computer_score}", 1, (255, 255, 255))
    screen.blit(person_score_write,(45,366))
    screen.blit(computer_score_write,(45,49))








