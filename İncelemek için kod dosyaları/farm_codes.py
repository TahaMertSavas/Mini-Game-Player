import os
import pygame
import random
from datetime import datetime

pygame.init()


#-----------------------------------------------------------------------------------------------------------------------
script_directory = os.path.dirname(os.path.abspath(__file__))
# ------------------------(BACKGROUND)-----------------------------------
Background19_path = os.path.join(script_directory, "Background19")

back_white = "back_white.png"
back_white = pygame.image.load(os.path.join(Background19_path, back_white))

back_purple = "back_purple.png"
back_purple = pygame.image.load(os.path.join(Background19_path, back_purple))

grass = "grass2.png"
grass = pygame.image.load(os.path.join(Background19_path, grass))
grass_width,grass_height = grass.get_size()
#-------------------------------(ACCESSORY)------------------------------
Accessory19_path = os.path.join(script_directory, "Accessory19")

barn = "barn.png"
barn = pygame.image.load(os.path.join(Accessory19_path, barn))

bird_nest = "bird_nest.png"
bird_nest = pygame.image.load(os.path.join(Accessory19_path, bird_nest))

fence = "fence.png"
fence = pygame.image.load(os.path.join(Accessory19_path, fence))

water_well_empty = "water_well.png"
water_well_empty = pygame.image.load(os.path.join(Accessory19_path, water_well_empty))

water_well_full = "water_well_full.png"
water_well_full = pygame.image.load(os.path.join(Accessory19_path, water_well_full))

lake = "lake.png"
lake = pygame.image.load(os.path.join(Accessory19_path, lake))
#-------------------------------------------------------------------

#-----------------------------------(Menu)--------------------------------
menu_bg = "menu_bg.png"
menu_bg = pygame.image.load(os.path.join(Accessory19_path, menu_bg))
menu_bg_widht,menu_bg_height = menu_bg.get_size()

menu_chicken = "menu_chicken.png"
menu_chicken = pygame.image.load(os.path.join(Accessory19_path, menu_chicken))
menu_chicken_widht,menu_chicken_height = menu_chicken.get_size()


menu_cow = "menu_cow.png"
menu_cow = pygame.image.load(os.path.join(Accessory19_path, menu_cow))
menu_cow_widht,menu_cow_height = menu_cow.get_size()

menu_sheep = "menu_sheep.png"
menu_sheep = pygame.image.load(os.path.join(Accessory19_path, menu_sheep))
menu_sheep_widht,menu_sheep_height = menu_sheep.get_size()

menu_fruit_sapling = "menu_fruit_sapling.png"
menu_fruit_sapling = pygame.image.load(os.path.join(Accessory19_path, menu_fruit_sapling))
menu_fruit_sapling_widht,menu_fruit_sapling_height = menu_sheep.get_size()

menu_sapling = "menu_sapling.png"
menu_sapling = pygame.image.load(os.path.join(Accessory19_path, menu_sapling))
menu_sapling_widht,menu_sapling_height = menu_sapling.get_size()

menu_water_well = "menu_water_well.png"
menu_water_well = pygame.image.load(os.path.join(Accessory19_path, menu_water_well))
menu_water_well_widht,menu_water_well_height = menu_water_well.get_size()

#-------------------------------------------------------------------

#-------------------------------(Character Run)------------------------------
Character_Run19_path = os.path.join(script_directory, "Character_Run19")

character_swiming = "character_swiming.png"
character_swiming = pygame.image.load(os.path.join(Character_Run19_path, character_swiming))

character_y_negative_1 = "character_y_negative_1.png"
character_y_negative_1 = pygame.image.load(os.path.join(Character_Run19_path, character_y_negative_1))

character_y_negative_2 = "character_y_negative_2.png"
character_y_negative_2 = pygame.image.load(os.path.join(Character_Run19_path, character_y_negative_2))

character_x_negative_left_1 = "character_x_negative_left_1.png"
character_x_negative_left_1 = pygame.image.load(os.path.join(Character_Run19_path, character_x_negative_left_1))

character_x_negative_left_2 = "character_x_negative_left_2.png"
character_x_negative_left_2 = pygame.image.load(os.path.join(Character_Run19_path, character_x_negative_left_2))

character_x_negative_right_1 = "character_x_negative_right_1.png"
character_x_negative_right_1 = pygame.image.load(os.path.join(Character_Run19_path, character_x_negative_right_1))

character_x_negative_right_2 = "character_x_negative_right_2.png"
character_x_negative_right_2 = pygame.image.load(os.path.join(Character_Run19_path, character_x_negative_right_2))

character_picture = character_y_negative_1
character_y_negative_list = [character_y_negative_1 , character_y_negative_2]
character_x_negative_right_list = [character_x_negative_right_1,character_x_negative_right_2]
character_x_negative_left_list = [character_x_negative_left_1,character_x_negative_left_2]
character_picture_list = character_y_negative_list
character_picture_no = 0
character_y = 230
character_x = 54
#-------------------------------------------------------------------

#-------------------------------(TREE)------------------------------
Tree19_path = os.path.join(script_directory, "Tree19")

tree1_img = "tree1.png"
tree1_img = pygame.image.load(os.path.join(Tree19_path, tree1_img))

fruit_tree1_img = "fruit_tree1.png"
fruit_tree1_img = pygame.image.load(os.path.join(Tree19_path, fruit_tree1_img))

broke_tree1_img = "broke_tree1.png"
broke_tree1_img = pygame.image.load(os.path.join(Tree19_path, broke_tree1_img))

not_fruit_tree1_img = "not_fruit_tree1.png"
not_fruit_tree1_img = pygame.image.load(os.path.join(Tree19_path, not_fruit_tree1_img))
#-------------------------------------------------------------------





class Barn(object):
    def __init__(self, img, x, y):
        self.img = img
        self.height = img.get_height()
        self.width = img.get_width()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)

    def blit_func(self, screen):
        screen.blit(self.img, (self.x + 27 + added_x, self.y + 40 + added_y))

class Tree(object):
    def __init__(self, img, x, y):
        self.img = img
        self.height = img.get_height()
        self.width = img.get_width()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)
    def blit_func(self, screen):
        screen.blit(self.img, (self.x + 27 + added_x, self.y + 40 + added_y))

class Water_Well(object):
    def __init__(self, img, x, y):
        self.img = img
        self.height = img.get_height()
        self.width = img.get_width()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)
    def blit_func(self, screen):
        screen.blit(self.img, (self.x + 27 + added_x, self.y + 40 + added_y))#şurdaki x y konumlarını düzelt eklemeli direkt class girtişinde düzelt

class Bird_Nest(object):
    def __init__(self, img,x,y):
        self.img = img
        self.height = img.get_height()
        self.width = img.get_width()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)
    def blit_func(self, screen):
        screen.blit(self.img, (self.x+27+added_x, self.y+40+added_y))

class Lake(object):
    def __init__(self, img, x, y):
        self.img = img
        self.height = img.get_height()
        self.width = img.get_width()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(img)
    def blit_func(self, screen):
        screen.blit(self.img, (self.x + 27 + added_x, self.y + 40 + added_y))

#score_write_font = pygame.font.SysFont("Arial", font_size, bold=True)
#group3_score_write = score_write_font.render(f"{group3_score}", 1, (255, 255, 255))
#screen.blit(group1_score_write,(group1_score_write_xcor,group1_score_write_ycor))
class Write(object):
    def __init__(self,write_type,font_size,write_color, x, y):
        self.write_type = write_type
        self.font_size = font_size
        self.write_color = write_color
        self.x = x
        self.y = y

        self.font_x = pygame.font.SysFont(write_type,font_size,bold=True)

    def blit_func(self, screen,write):
        write_x = self.font_x.render(write,1,self.write_color)
        screen.blit(write_x, (self.x + 27 , self.y + 40))


class Menu(object):
    def __init__(self):
        pass

    def blit_func(self,screen):
        menu_x,menu_y = grass_xcor+(346/2)-(menu_bg_widht/2),grass_ycor+(367/2)-(menu_bg_height/2)
        screen.blit(menu_bg,(menu_x,menu_y))
        menu_cow_x,menu_cow_y = menu_x+(menu_bg_widht/2)-menu_cow_widht/2 , menu_y+(menu_bg_height/2)-menu_cow_height/2 - 30
        screen.blit(menu_cow, (menu_cow_x, menu_cow_y))
        screen.blit(menu_chicken, (menu_cow_x-60, menu_cow_y))
        screen.blit(menu_sheep, (menu_cow_x + 60, menu_cow_y))
        screen.blit(menu_sapling, (menu_cow_x, menu_cow_y+60))
        screen.blit(menu_fruit_sapling, (menu_cow_x-60, menu_cow_y + 60))
        screen.blit(menu_water_well, (menu_cow_x + 60, menu_cow_y + 60))


#--------------------------------(resimden obje oluşturulan kısım)---------------------------------------------
barn1 = Barn(barn,18,0)

bird_nest1 = Bird_Nest(bird_nest,191,22)
bird_nest_list = [bird_nest1]

water_well1 = Water_Well(water_well_full,159,128)
water_well_full_list = [water_well1]
water_well_empty_list = []

lake1 = Lake(lake,472,472)

fruit_tree1 = Tree(fruit_tree1_img,281,0)
fruit_tree2 = Tree(fruit_tree1_img,363,0)
fruit_tree3 = Tree(fruit_tree1_img,389,180)
fruit_tree4 = Tree(fruit_tree1_img,63,404)
fruit_tree_list = [fruit_tree1,fruit_tree2,fruit_tree3,fruit_tree4]

tree1 = Tree(tree1_img, 574, 0)
tree2 = Tree(tree1_img, 645, 0)
tree3 = Tree(tree1_img, 645, 72)
tree4 = Tree(tree1_img, 482, 408)
tree5 = Tree(tree1_img, 526, 399)
tree6 = Tree(tree1_img, 578, 419)
tree7 = Tree(tree1_img, 182, 366)
tree8 = Tree(tree1_img, 236, 570)
tree9 = Tree(tree1_img, 0, 653)
tree10 = Tree(tree1_img, 506, 608)
tree_list = [tree1,tree2,tree3,tree4,tree5,tree6,tree7,tree8,tree9,tree10]

broke_tree1 = Tree(broke_tree1_img,583,172)
broke_tree2 = Tree(broke_tree1_img,68,262)
broke_tree3 = Tree(broke_tree1_img,213,316)
broke_tree4 = Tree(broke_tree1_img,137,604)
broke_tree5 = Tree(broke_tree1_img,639,604)
broke_tree_list = [broke_tree1,broke_tree2,broke_tree3,broke_tree4,broke_tree5]



menu1 = Menu()
#-----------------------------------------------------------------------------------------


#---------------------------------(Yazı objesi oluşturulan kısım)---------------------------------------------------
wood_num = 0
wood_write = Write("Arial",15, (255,255,255), 20,5)

fruit_num = 0
fruit_write = Write("Arial",15, (255,255,255), 120,5)

water_num = 0
water_write = Write("Arial",15, (255,255,255), 220,5)
#-----------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------>listeleri oluşturduk ama bi ağaçlarda drop var gibi  ce e ye basılı tutunca error alıoyoruz
objects_list = fruit_tree_list + tree_list + broke_tree_list
objects_list.append(water_well1)
objects_list.append(bird_nest1)
print(len(objects_list))
# ------------------------------------------------------------------------------------------------------>

frame_x,frame_y = 346,367
grass_xcor,grass_ycor = 27,40
added_x,added_y=0,0
character_speed = 2
change_list = False
momentary_object = None
create_tree_list = []
def start(screen,keys,one_down,key_name,display_again,left_click,mouse_pos):
    # ----------->(GLOBAL)<-------------
    global character_y
    global character_x
    global character_picture
    global frame_x
    global frame_y
    global grass_xcor
    global grass_ycor
    global added_x
    global added_y
    global character_picture_no
    global character_picture_list
    global change_list
    global momentary_object
    global wood_num
    global fruit_num
    global water_num
    global create_tree_list
    global game_exit
    # ---------------------------------
    screen.blit(grass,(grass_xcor, grass_ycor))
    #print((barn1.y + barn1.height + 27 + added_y))
    #------------------(Karakter Yürüme)---------------
    if keys[pygame.K_w] and (( (barn1.y + barn1.height + 45 + added_y) <= (character_y + character_picture.get_height()) ) or ( (barn1.x + barn1.width + 27 + added_x) <= (character_x + character_picture.get_width()) )):
        difference_y = character_y
        if difference_y == 50:
            if grass_ycor != 40:  # burası arkaplanın sağ tarafta daha gidicek yer olup olmadığını kontrol ediyor
                grass_ycor += character_speed
                added_y += character_speed
        else:
            character_y -= character_speed

        character_picture_list = character_y_negative_list
        if (display_again % 5 == 0):  # yürüuüş animasyonu tuşa bastıkca fotoğraf değişiyor
            character_picture_no += 1
            if character_picture_no == 2:
                character_picture_no = 0


    if keys[pygame.K_s]:

        difference_y = frame_y+80 - (character_y + character_picture.get_height())
        if difference_y == 50:
            if grass_ycor != (14 + frame_x) - grass.get_width():  # burası arkaplanın sağ tarafta daha gidicek yer olup olmadığını kontrol ediyor
                grass_ycor -= character_speed
                added_y -= character_speed
        else:
            character_y += character_speed

        character_picture_list = character_y_negative_list
        if (display_again%5==0): #yürüuüş animasyonu tuşa bastıkca fotoğraf değişiyor
            character_picture_no+=1
            if character_picture_no == 2:
                character_picture_no = 0



    if keys[pygame.K_a] and (( (barn1.y + barn1.height + 40 + added_y) <= (character_y + character_picture.get_height()) ) or ( (barn1.x + barn1.width + 30 + added_x) <= (character_x ) )):
        difference_x = character_x
        if difference_x == 50:
            if grass_xcor != 27:#burası arkaplanın sağ tarafta daha gidicek yer olup olmadığını kontrol ediyor
                grass_xcor += character_speed
                added_x += character_speed
        else:
            character_x -= character_speed

        character_picture_list = character_x_negative_left_list
        if (display_again % 5 == 0):  # yürüuüş animasyonu tuşa bastıkca fotoğraf değişiyor
            character_picture_no += 1
            if character_picture_no == 2:
                character_picture_no = 0

    if keys[pygame.K_d]:
        difference_x = frame_x+54 -(character_x+character_picture.get_width())
        if difference_x == 50:
            if grass_xcor != (27+frame_x)-grass.get_width():  # burası arkaplanın sağ tarafta daha gidicek yer olup olmadığını kontrol ediyor
                grass_xcor -= character_speed
                added_x-=character_speed
        else:
            character_x += character_speed

        character_picture_list = character_x_negative_right_list
        if (display_again % 5 == 0):  # yürüyüş animasyonu tuşa bastıkca fotoğraf değişiyor
            character_picture_no += 1
            if character_picture_no == 2:
                character_picture_no = 0

    #--------------------------------------------------
    screen.blit(fence, (grass_xcor, grass_ycor))

    barn1.blit_func(screen)
    water_well1.blit_func(screen)
    bird_nest1.blit_func(screen)
    lake1.blit_func(screen)

    # ------------------------------------------------------------------------------------------------------> Ağaç Oluşturma

    if (keys[pygame.K_SPACE]) and (display_again % 25 == 0):
        tree = Tree(fruit_tree1_img, character_x, character_y)
        fruit_tree_list.append(tree)

    # ------------------------------------------------------------------------------------------------------

    #-------------------------------------->önde arkada durma kısmı burada
    character_picture = character_picture_list[character_picture_no]
    collision_occurred_list = []
    collision_occurred = False
    for object in objects_list:
        character_mask = pygame.mask.from_surface(character_picture)
        if character_mask.overlap(object.mask,((object.x + 27 + added_x) - character_x, (object.y + 40 + added_y) - character_y)):
            if (character_y + character_picture.get_height()) < (object.y + 40 + added_y + object.img.get_height()):
                screen.blit(character_picture, (character_x, character_y))
                object.blit_func(screen)
                collision_occurred = True
                collision_occurred_list.append(object)
                break
            else:
                object.blit_func(screen)
                screen.blit(character_picture, (character_x, character_y))
                collision_occurred = True
                collision_occurred_list.append(object)
                break
        else:
            object.blit_func(screen)
    if collision_occurred == True:
        objects_list.remove(collision_occurred_list[0])
        for object in objects_list:
            object.blit_func(screen)
        objects_list.append(collision_occurred_list[0])

    character_mask = pygame.mask.from_surface(character_picture)
    if character_mask.overlap(lake1.mask, (
    (lake1.x + 27 + added_x) - character_x, (lake1.y + 40 + added_y) - character_y)):  # yüzdüğümüz kısım
        character_picture = character_swiming
        print("a")

    if collision_occurred == False:
        screen.blit(character_picture, (character_x, character_y))



    # ------------------------------------------------------------------------------------------------------>Meyveleri toladığımız kısım

    for object in fruit_tree_list:#---------------------->Meyveleri toladığımız kısım
        character_mask = pygame.mask.from_surface(character_picture)
        if character_mask.overlap(object.mask,((object.x + 27 + added_x) - character_x, (object.y + 40 + added_y) - character_y)):
            if keys[pygame.K_e]:
                fruit_tree_list.remove(object)
                object.img = not_fruit_tree1_img
                momentary_object = object
                change_list = 1
                fruit_num += 10
                break
    if (change_list == 1) and (display_again%25 == 0):
        tree_list.append(momentary_object)
        change_list = False
        print("meyveyi topladıktan spnra tree liste eklendi")
    #------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------>Ağaç kırma kısmı
    for object in tree_list:#---------------------->Ağaç kırma kısmı
        character_mask = pygame.mask.from_surface(character_picture)
        if character_mask.overlap(object.mask,((object.x + 27 + added_x) - character_x, (object.y + 40 + added_y) - character_y)):
            if keys[pygame.K_e]:
                tree_bottom_midpoint = object.x + (object.img.get_width()/2)
                midpoint_of_tree_height = object.y + object.img.get_height()

                object.img = broke_tree1_img

                object.x = tree_bottom_midpoint - (object.img.get_width()/2) - 4
                object.y = midpoint_of_tree_height - (object.img.get_height() / 2) - 6

                tree_list.remove(object)
                momentary_object = object
                change_list = 2
                wood_num += 10
                break

    if (change_list == 2) and (display_again%25 == 0):
        broke_tree_list.append(momentary_object)
        change_list = False
        print("ağacı kırdıktan sonra broke liste eklendi")
    # ------------------------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------------------> Kökleri kırma
    for object in broke_tree_list:  # ---------------------->Kökleri kırma
        character_mask = pygame.mask.from_surface(character_picture)
        if character_mask.overlap(object.mask,((object.x + 27 + added_x) - character_x, (object.y + 40 + added_y) - character_y)):
            if keys[pygame.K_e]:
                broke_tree_list.remove(object)
                objects_list.remove(object)
                wood_num += 5
                print("kök kırdıktan sonra silindi")#şekli hemen değişiyor ama listeye eklenmiyor veya silinmiyorki işlem yapılsın

    #print(len(objects_list))
    #print(len(broke_tree_list))
        # ------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------> Kuyudan su çekme
    for object in water_well_full_list:#---------------------->Kuyudan su çekme
        character_mask = pygame.mask.from_surface(character_picture)
        if character_mask.overlap(object.mask,((object.x + 27 + added_x) - character_x, (object.y + 40 + added_y) - character_y)):
            if keys[pygame.K_e]:
                object.img = water_well_empty
                water_well_full_list.remove(object)
                water_well_empty_list.append(object)
                water_num += 30
                break



    # -----------------------------------------(yazıları blit etme)-----------------------------------------
    pygame.draw.rect(screen,(0,0,0),(wood_write.x+24,wood_write.y+39,78,20))
    pygame.draw.rect(screen, (0, 0, 0), (fruit_write.x + 24, fruit_write.y + 39, 65, 20))
    pygame.draw.rect(screen, (0, 0, 0), (water_write.x + 24, water_write.y + 39, 70, 20))
    wood_write.blit_func(screen,f"Wood: {wood_num}")
    fruit_write.blit_func(screen, f"Fruit: {fruit_num}")
    water_write.blit_func(screen,f"Water: {water_num}")
    # ------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------
    character_mask = pygame.mask.from_surface(character_picture)
    if character_mask.overlap(barn1.mask,((barn1.x + 27 + added_x) - character_x, (barn1.y + 40 + added_y) - character_y)):# ahırla çarpışmayı kontrol ediyorum
        if keys[pygame.K_e]:
            menu1.blit_func(screen)


    # ------------------------------------------------------------------------------------------------------
    back_button = back_white
    if 330 <= mouse_pos[0] <= 330+back_button.get_width() and 47 <= mouse_pos[1] <= 47+back_button.get_height():
        back_button = back_purple
        if left_click == True:
            game_exit = True
    screen.blit(back_button , (330, 47))


def return_menu():
    return game_exit
def return_false():
    global game_exit
    game_exit = False

def reset():
    pass