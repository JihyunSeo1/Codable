import pygame, math , time ,os, random

pygame.init()


# Set up custom events
START_GAME_EVENT = pygame.USEREVENT + 1





# add music
pygame.mixer.init()
pygame.mixer.music.load('I AM.mp3')


# Define scoring values
PERFECT_SCORE = 3
GREAT_SCORE = 2
GOOD_SCORE = 1
MISS_SCORE = 0

# Define hit type counters
perfect_hits = 0
great_hits = 0
good_hits = 0
miss_hits = 0 

# Define hit range thresholds (adjust these values as needed)
PERFECT_HIT_THRESHOLD = 30  # Distance in pixels for a perfect hit
GREAT_HIT_THRESHOLD =50    # Distance in pixels for a great hit
GOOD_HIT_THRESHOLD = 75     # Distance in pixels for a good hit
MISS_HIT_THRESHOLD = 200    # Distance in pixels for a good hit
hit_count_font = pygame.font.SysFont("Courier New", 50)





# designing note patterns
x = 200
a= 54
b = x + a
c = b + 30
d = 30
#long
    # designing note patterns
note_pattern = [
       (x+115 + 5, 'long', 'a', 200), # intro
    (x+145 + 5 , 'long', 's', 200),
    (x+175 + 5, 'long', 'k', 200),
    (x+205 + 5, 'long', 'l', 200),
    
    (x+240 , 'regular', 'a', 1),
    (x+249 , 'regular', 's', 1),
    (x+258 , 'regular', 'k', 1),
    
    (x+267 , 'regular', 'l', 1),
    (x+276 , 'regular', 'k', 1),
    (x+285 , 'regular', 's', 1),

    (x+294 , 'regular', 'a', 1),
    (x+303 , 'regular', 's', 1),
    (x+312 , 'regular', 'k', 1),
    
     
    (x+321 , 'regular', 'l', 1),
    (x+330 , 'regular', 'k', 1),
   
    (x+340 , 'long', 'l', 150),
    (x+340 , 'long', 'a', 150),  #intro end


    (x+370, 'regular', 's', 1),   #다른   ## 15차이
    (x+388, 'regular', 'k', 1),
    
    (x+400, 'regular', 'a', 1),   #문을
    (x+418, 'regular', 'l', 1),

    (x+430, 'regular', 's', 1),   #열어
    (x+448, 'regular', 'k', 1),
    
    (x+460, 'regular', 'a', 1),   #//
    (x+478, 'regular', 'l', 1),
    

    (x+490, 'regular', 's', 1),   #따라갈
    (x+508, 'regular', 'k', 1),
    
    (x+520, 'regular', 'a', 1),   #필욘
    (x+538, 'regular', 'l', 1),

    (x+550, 'regular', 's', 1),   #없어
    (x+568, 'regular', 'k', 1),
    
    (x+580, 'regular', 'a', 1),   #//
    (x+598, 'regular', 'l', 1),
  
   
    (x+610, 'regular', 's', 1),  #넌 너의길로
    (x+628, 'regular', 'k', 1),
    
    (x+640, 'regular', 'a', 1), 
    (x+658, 'regular', 'l', 1),
    
    (x+670, 'regular', 's', 1), 
    (x+688, 'regular', 'k', 1),
    
    (x+700, 'regular', 'a', 1),
    (x+718, 'regular', 'l', 1),


    (x+730, 'regular', 's', 1), 
    (x+748, 'regular', 'k', 1),
    
    (x+760, 'regular', 'a', 1), # 난 나의길로
    (x+778, 'regular', 'l', 1),
    
    (x+790, 'regular', 's', 1), 
    (x+808, 'regular', 'k', 1),
    
    (x+820, 'regular', 'a', 1),
    (x+838, 'regular', 'l', 1),


    (x+850, 'regular', 's', 1), 
    (x+868, 'regular', 'k', 1),
    
    (x+880, 'regular', 'a', 1), 
    (x+898, 'regular', 'l', 1),
    
    (x+910, 'regular', 's', 1), #음
    (x+928, 'regular', 'k', 1),
    
    (x+940, 'regular', 'a', 1),
    (x+958, 'regular', 'l', 1),

   
    (x+970, 'regular', 's', 1),  #하루하루마다
    (x+988, 'regular', 'k', 1),
    
    (x+1000, 'regular', 'a', 1), 
    (x+1018, 'regular', 'l', 1),
    
    (x+1030, 'regular', 's', 1), 
    (x+1048, 'regular', 'k', 1),
    
    (x+1060, 'regular', 'a', 1),
    (x+1078, 'regular', 'l', 1),

    (x+1090, 'regular', 's', 1), #색이 달라진 느낌
    (x+1108, 'regular', 'k', 1),
    
    (x+1120, 'regular', 'a', 1), 
    (x+1138, 'regular', 'l', 1),
    
    (x+1150, 'regular', 's', 1), 
    (x+1168, 'regular', 'k', 1),
    
    (x+1180, 'regular', 'a', 1), #밝게 빛이나는
    (x+1198, 'regular', 'l', 1),

    
    (x+1210, 'regular', 'a', 1),
    (x+1220, 'regular', 's', 1),
    (x+1230, 'regular', 'k', 1), # 길을찾아
    (x+1240, 'regular', 'l', 1),

    #im on my way~
    (x+1258, 'regular', 'a', 1),
    (x+1282, 'regular', 's', 1),
    (x+1295, 'regular', 'k', 1), 
    (x+1312, 'long', 'l', 1000),

    (x+1365, 'regular', 's', 1),
    (x+1380, 'long', 'k', 1000),
    (x+1433, 'regular', 'a', 1), 
    (x+1448, 'long', 's', 1000),

     
    (x+1508,'regular', 'a', 1),
    (x+1520, 'regular', 's', 1),
    (x+1532, 'regular', 'k', 1), 
    (x+1544, 'regular', 'l', 1),


    #넌 그냥 믿으면 돼
    (x+1564,'regular', 'a', 1),
    (x+1582, 'regular', 's', 1),
    (x+1600, 'regular', 'k', 1), 
    (x+1621, 'regular', 'l', 1),
    (x+1639, 'regular', 'k', 1), 
    (x+1657, 'regular', 's', 1),
    (x+1675,'regular', 'a', 1),

    
    #im on my way~
    (x+1702+a, 'regular', 'a', 1),
    (x+1726+a, 'regular', 's', 1),
    (x+1739+a, 'regular', 'k', 1), 
    (x+1756+a, 'long', 'l', 1000),

    # 16, 52, 16
    (x+1803+a, 'regular', 's', 1),
    (x+1814+a, 'long', 'k', 1000),
    (x+1871+a, 'regular', 'a', 1), 
    (x+1882+a, 'long', 's', 1000),

     
    (x+1942+a,'regular', 'a', 1),
    (x+1954+a, 'regular', 's', 1),
    (x+1966+a, 'regular', 'k', 1), 
    (x+1978+a, 'regular', 'l', 1),

    #보이는 그대로야
    (b+1998,'regular', 'a', 1),
    (b+2018, 'regular', 's', 1),
    (b+2038, 'regular', 'k', 1), 
    (b+2058, 'regular', 'l', 1),
    (b+2078, 'regular', 'k', 1), 
    (b+2098, 'regular', 's', 1),
    (b+2118,'regular', 'a', 1),

    (b+2138,'regular', 'a', 1),
    (b+2163, 'regular', 's', 1),
    (b+2188, 'regular', 'k', 1), 
    (b+2213, 'regular', 'l', 1),
    
    #너는 누군가의 dreams come true
    (b+2238,'regular', 'a', 1),
    (b+2263+5, 'regular', 'k', 1),
    (b+2288+10, 'regular', 's', 1), 
    (b+2313+15, 'regular', 'l', 1),
    (b+2338+20,'regular', 'a', 1),
    (b+2363+25, 'regular', 's', 1),
    (b+2388+30, 'regular', 'k', 1), 
    (b+2413+35, 'regular', 'l', 1),

    #제일 좋은 어느날의 데자뷰
    (b+2438+40,'regular', 'a', 1),
    (b+2463+45, 'regular', 'k', 1),
    (b+2488+50, 'regular', 's', 1), 
    (b+2513+55, 'regular', 'l', 1),
    (b+2538+60,'regular', 'a', 1),
    (b+2563+65, 'regular', 's', 1),
    (b+2588+70, 'regular', 'k', 1), 
    (b+2688, 'regular', 'l', 1),


    #머물고픈 어딘가의 낯선 뷰
    (b+2718,'regular', 'a', 1),
    (b+2748, 'regular', 'k', 1),
    (b+2778, 'regular', 's', 1), 
    (b+2808, 'regular', 'l', 1),
    (b+2838,'regular', 'a', 1),
    (b+2868, 'regular', 's', 1),
    (b+2898, 'regular', 'k', 1), 
    (b+2928, 'regular', 'l', 1),


    # I will be far a way
    (b+2958, 'long', 'a', 800),
    (b+2988, 'long', 'l', 800),
    (b+3018, 'long', 's', 800),
    (b+3048, 'long', 'k', 800),
    (b+3078, 'long', 'l', 900),
    (b+3078, 'long', 'a', 900),


    # Thats my !
    (c+3110, 'regular', 's', 1),
    (c+3110, 'regular', 'k', 1),
    (c+3140, 'regular', 'a', 1),
    (c+3140, 'regular', 'l', 1),

    # life is 아름다운 
    (c+3175, 'regular', 'a', 1),
    (c+3200, 'regular', 's', 1),
   
    (c+3233, 'regular', 'l', 1),
    (c+3243, 'regular', 'k', 1),
    (c+3253, 'regular', 's', 1),
    (c+3263, 'regular', 'a', 1),
 
    

    #galaxy
    (c+3289, 'regular', 'a', 1),
    (c+3289, 'regular', 's', 1),
    
    (c+3319, 'regular', 's', 1),
    (c+3319, 'regular', 'k', 1),
    
    
    (c+3349, 'regular', 'k', 1),
    (c+3349, 'regular', 'l', 1),

    # be a writer
    (c+3373, 'long', 'a', 300),
    
    (c+3405, 'regular', 'l', 1),
    (c+3435, 'regular', 'k', 1),

    # 장르로는
    (c+3465, 'regular', 's', 1),
    (c+3495, 'regular', 'a', 1),
    
    # fantasy
    (c+3522, 'regular', 'k', 1),
    (c+3522, 'regular', 'l', 1),

    (c+3552, 'regular', 'k', 1),
    (c+3552, 'regular', 's', 1),
    
    (c+3582, 'regular', 's', 1),
    (c+3582, 'regular', 'a', 1),
    

    # 내일 내게 
   
    (c+3610, 'long', 'l', 300),
    (c+3650, 'regular', 's', 1),
    (c+3680, 'regular', 'a', 1),
    
    #열리는건
    (c+3710, 'regular', 'l', 1),
    (c+3740, 'regular', 'k', 1),

   

    # big big 스테이지 
    (c+3775, 'regular', 'l', 1),
    (c+3775, 'regular', 'k', 1),

    (c+3801, 'regular', 'k', 1),
    (c+3801, 'regular', 's', 1),

    (c+3831, 'regular', 's', 1),
    (c+3831, 'regular', 'a', 1),

    (c+3861, 'regular', 'a', 1),
    (c+3861, 'regular', 'l', 1),
  

    # so that is who I am
    (c+3891, 'regular', 's', 1),
    (c+3921, 'regular', 'a', 1),
    (c+3951, 'regular', 'k', 1),
    (c+3981, 'regular', 'l', 1),
    (c+4011, 'long', 'a', 1000),
    (c+4011, 'long', 'l', 1000),
    


     #어느 깊은 밤

    (c+4115, 'regular', 'k', 1),
    (c+4130, 'regular', 's', 1),
    
    (c+4145, 'long', 'a', 2500),
    (c+4180, 'regular', 'k', 1),
    (c+4230, 'regular', 'k', 1),
    
    
    (c+4261, 'long', 's', 2500),
    (c+4291, 'regular', 'k', 1),
    (c+4341, 'regular', 'k', 1),

    
     #길을 잃 어도
    (c+4381, 'long', 'l', 2500),
    (c+4413, 'regular', 's', 1),
    (c+4463, 'regular', 's', 1),
    (c+4491, 'long', 'k', 2500),
    (c+4533, 'regular', 'a', 1),
    (c+4583, 'regular', 'a', 1),


    #차라리 날아올라
    (c+4611, 'regular', 'a', 1),
    (c+4621, 'regular', 's', 1),
    (c+4631, 'regular', 'k', 1),
    (c+4641, 'regular', 'l', 1),

    # 그럼네가
    (c+4661, 'regular', 's', 1),
    (c+4671, 'regular', 'a', 1),
    (c+4681, 'regular', 'k', 1),
    (c+4691, 'regular', 'l', 1),

    #지나가는 대로 길이거든
    (c+4720, 'regular', 's', 1),
    (c+4720, 'regular', 'k', 1),
    (c+4734, 'regular', 's', 1),
    (c+4734, 'regular', 'k', 1),
    (c+4748, 'regular', 's', 1),
    (c+4748, 'regular', 'k', 1),
   
    (c+4762, 'regular', 's', 1),
    (c+4762, 'regular', 'k', 1),
    (c+4776, 'regular', 's', 1),
    (c+4776, 'regular', 'k', 1),
    (c+4790, 'regular', 's', 1),
    (c+4790, 'regular', 'k', 1),
   
    (c+4804, 'regular', 'a', 1),
    (c+4804, 'regular', 'l', 1),
    (c+4818, 'regular', 'a', 1),
    (c+4818, 'regular', 'l', 1),
    (c+4832, 'regular', 'a', 1),
    (c+4832, 'regular', 'l', 1),
    (c+4846, 'regular', 'a', 1),
    (c+4846, 'regular', 'l', 1),
   
  
    # 1,2,3 
    (c+4857, 'regular', 'l', 1),
    (c+4857, 'regular', 'a', 1),

    (c+4880, 'regular', 's', 1),
    (c+4880, 'regular', 'k', 1),

    (c+4900, 'regular', 's', 1),
    (c+4900, 'regular', 'k', 1),
    
    # 1,2,3
    (c+4920, 'regular', 'l', 1),
    (c+4920, 'regular', 'a', 1),

    (c+4940, 'regular', 's', 1),
    (c+4940, 'regular', 'k', 1),

    (c+4960, 'regular', 's', 1),
    (c+4960, 'regular', 'k', 1),

    # 1,2,3
    (c+4980, 'regular', 'l', 1),
    (c+4980, 'regular', 'a', 1),

    (c+5000, 'regular', 's', 1),
    (c+5000, 'regular', 'k', 1),

    (c+5020, 'regular', 's', 1),
    (c+5020, 'regular', 'k', 1),

    #Fly Up

    (c+5040, 'long', 'l', 4000),
    (c+5040, 'long', 'a', 4000),

    (c+5100, 'regular', 's', 1),
    (c+5100, 'regular', 'k', 1),

 
    # i hope you'd be someone's dream come true

    # 제일 좋은 어느날의 

    (c+5450, 'regular', 'a', 1),
    (c+5480, 'regular', 's', 1),
   
   # 25 간격
    (c+5510, 'regular', 'l', 1),
    (c+5540, 'regular', 'k', 1),
    
 
    # 데 자 뷰
    (c+5570, 'regular', 'a', 1),
    (c+5570, 'regular', 's', 1),
    
    (c+5598, 'regular', 's', 1),
    (c+5598, 'regular', 'k', 1),
    
    (c+5624, 'regular', 'k', 1),
    (c+5624, 'regular', 'l', 1),

    
    # 머물 고 픈 
    (c+5648, 'regular', 'l', 1),
    (c+5666, 'regular', 's', 1),
    
    (c+5684, 'regular', 'l', 1),
    (c+5714, 'regular', 'k', 1),
    
    #어딘 가의 
    (c+5744, 'regular', 'a', 1),
    (c+5774, 'regular', 's', 1),

     # 낯 선 뷰
    (c+5804, 'regular', 'l', 1),
    (c+5804, 'regular', 'k', 1),
    
    (c+5834, 'regular', 'a', 1),
    (c+5834, 'regular', 's', 1),
    
    (c+5864, 'regular', 'l', 1),
    (c+5864, 'regular', 'a', 1),

    (c+5894, 'regular', 's', 1),
    (c+5894, 'regular', 'k', 1),
    
    # I will be far a way #간격 30
    (b+5954, 'long', 'a', 700),
    (b+5984, 'long', 's', 700),
    (b+6014, 'long', 'k', 700),
    (b+6044, 'long', 'l', 700),
    (b+6074, 'long', 's', 800),
    (b+6074, 'long', 'k', 800),

        #간격 30
      # Thats my !
    (c+6104, 'regular', 'a', 1),
    (c+6104, 'regular', 'l', 1),
    (c+6134, 'regular', 's', 1),
    (c+6134, 'regular', 'k', 1),

    # life is 아름다운 
    (c+6164, 'regular', 'a', 1),
    (c+6194, 'regular', 's', 1),
   
    (c+6214, 'regular', 'l', 1),
    (c+6229, 'regular', 'k', 1),
    (c+6244, 'regular', 's', 1),
    (c+6259, 'regular', 'a', 1),
 
    

    #galaxy  # 26
    (c+6289, 'regular', 'a', 1),
    (c+6289, 'regular', 's', 1),
    
    (c+6319, 'regular', 's', 1),
    (c+6319, 'regular', 'k', 1),
    
 
    (c+6349, 'regular', 'k', 1),
    (c+6349, 'regular', 'l', 1),

    # be a writer # 32
    (c+6379, 'long', 'a', 300),
    (c+6411, 'regular', 'l', 1),
    (c+6441, 'regular', 'k', 1),
   
    # 장르로는
    (c+6471, 'regular', 's', 1),
    (c+6501, 'regular', 'a', 1),
    
    # fantasy
    (c+6531, 'regular', 'k', 1),
    (c+6531, 'regular', 'l', 1),

    (c+6561, 'regular', 'k', 1),
    (c+6561, 'regular', 's', 1),
    
    (c+6591, 'regular', 's', 1),
    (c+6591, 'regular', 'a', 1),
    

    # 내일 내게 
    (c+6621, 'long', 'l', 300),
    (c+6653, 'regular', 's', 1),
    (c+6683, 'regular', 'a', 1),
    
    #열리는건
    (c+6713, 'regular', 'l', 1),
    (c+6743,'regular', 'k', 1),

    # big big 스테이지 
    (c+6773, 'regular', 'l', 1),
    (c+6773, 'regular', 'k', 1),

    (c+6803, 'regular', 'k', 1),
    (c+6803, 'regular', 's', 1),

    (c+6833, 'regular', 's', 1),
    (c+6833, 'regular', 'a', 1),

    (c+6863, 'regular', 'a', 1),
    (c+6863, 'regular', 'l', 1),
  

    # so that is who I am
    (c+6893, 'long', 'k', 250),
    (c+6923, 'long', 's', 250),
    (c+6953, 'long', 'l', 250),
    (c+6983, 'long', 'a', 250),
    (c+7013, 'long', 's', 1000),
    (c+7013, 'long', 'k', 1000),
    


    
    
]



# Class Note
#--------------------------------------
class Note:
    def __init__(self, x, speed, color):
        self.x = x
        self.y = -200  # Start at the top
        self.speed = speed
        self.color = color
        self.width = w / 16
        self.height = h / 35
        self.y_range_one = (h/12)*9 - 120
        self.y_range_two = (h/12)*9 + 120

            
    def move(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_out_of_screen(self):
        return self.y > h
    
    # removes notes
    def note_remove(self):
        return self.y_range_two > self.y > self.y_range_one
            
    def is_at_position(self, x):
        return self.x == x    

#------------------------------------------


# New Class for Long Note 
# Inheriting the Class Note
#--------------------------------------
class LongNote(Note):
    def __init__(self, x, speed, color, length):
        super().__init__(x, speed, color)
        self.y = -200 - length
        self.length = length  # 
        self.initial_length = length # start at 0 and grow as the note falls

    def move(self):
        super().move()
        self.length = min(self.length + self.speed, self.initial_length)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))
    

    # introducing its own attribute ('length')
    def fade(self, amount):
        self.length -= amount + 40  # determines the amount of notes that are being faded away
        self.y += amount + 5
    
    # additional handling for removal and scoring within specific length
    def note_remove(self, fade_amount):
            #if either upper or lower boundary of note is between our range, it starts to fade.
        if self.y_range_two > self.y > self.y_range_one or \
           self.y_range_two > self.y + self.length > self.y_range_one:   #checking lower boundary
            
            #introducing its own attribuite('fade')
            self.fade(fade_amount)
            return self.length <=0  # means scoring should increase
        return False

#------------------------------------------



def remove_note_and_calculate_score(note):
    global score, perfect_hits, great_hits, good_hits, miss_hits # Use global variables

    bottom_line_y = (h/12)*9
    distance_from_bottom_line = abs(note.y - bottom_line_y)

    if distance_from_bottom_line <= PERFECT_HIT_THRESHOLD:
        score += PERFECT_SCORE
        perfect_hits += 1
    elif distance_from_bottom_line <= GREAT_HIT_THRESHOLD:
        score += GREAT_SCORE
        great_hits += 1
    elif distance_from_bottom_line <= GOOD_HIT_THRESHOLD:
        score += GOOD_SCORE
        good_hits += 1
    else:
        score = 0
        miss_hits += 1

     # Remove the note
    notes.remove(note)




# screen sizea
#--------------------------------
w = 1600
h = w *(9/16)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Rhythm Game")
#--------------------------------

# time and clock
# ------------------------------------
clock = pygame.time.Clock()
FPS = 60
gst = time.time()
Time = time.time() - gst
#--------------------------------------
"""""
pygame.mixer.init()  # Initialize the mixer module
pygame.mixer.music.load('path_to_your_music_file.mp3') 

pygame.mixer.music.play(-1)  # Start playing the music
"""


def show_intro_page(screen):
    intro_font = pygame.font.SysFont("Arial", 50)
    intro_text = intro_font.render("Welcome to Rhythm Game!", True, (255, 255, 255))
    instruction_text1 = intro_font.render("Press SPACEBAR to start the game.", True, (255, 255, 255))
    instruction_text2 = intro_font.render("Use keys A, S, K, L to hit the notes.", True, (255, 255, 255))

    screen.fill((0, 0, 0))  # Set the background color
    screen.blit(intro_text, (w // 4, h // 4))
    screen.blit(instruction_text1, (w // 4, h // 3))
    screen.blit(instruction_text2, (w // 4, h // 2))

    pygame.display.flip()




main = True
ingame = False
keys = [0,0,0,0]
keyset = [0,0,0,0]

maxframe = 60   #frame setting
fps = maxframe #frame per second

notes = []  # To keep track of all notes
note_spawn_rate = 59.9  # Spawn a note every 60 frames
frames_since_last_note = 0
note_positions = [w / 2 - w / 8 + i * (w / 16) for i in range(4)]  # Positions for each of the four columns
score = 0

# New variables to track key holds
keys_being_held = [False, False, False, False]
frame_count = 0
# Positions for keys: a, s, k, l
key_positions = {'a': note_positions[0], 's': note_positions[1], 'k': note_positions[2], 'l': note_positions[3]}


# Define score range colors
score_colors = {
    (0, 100): (0, 0, 0),      # Black for scores 0-100
    (101, 200): (255, 165, 0),  # Orange for scores 101-200
    # Add more score ranges and colors as needed
}
a = 0
b = 0
c = 0


last_spawn_time = time.time()

has_music_started = False

show_ending_page = False



while main:
    

    while not ingame:
        show_intro_page(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingame = False
                main = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ingame = True

    while ingame:
        song_duration = 121 # duration of the song in seconds
        if not has_music_started:
            pygame.mixer.music.play(-1)
            song_start_time =time.time() #record the time when the song starts
            #has_music_started = True
            Time = time.time() - gst

        


        frame_count += 1 
        


        ## -------------------------------------------

        

        #clear the screen first
        if (score == 0):
            a = 0
            b = 0
            c = 0


        elif (score < 100):
            a = min((a + (score/200)), 200)    
        elif (score < 150):
            #a = max((a - (score-100)), 0)
            a = max((a -  (score/200)), 200)
            b = min((b + (score/200)), 200)
            
        elif (score < 200):
            a = min((a + (score/200)), 200)
            b = max((b - (score/200)), 0)
          
            c = min((c + (score/200)), 200)

        else :
            a = max((a - (score/200)), 0)
            b = max((b + (score/200)), 0)   
            c = min((c - (score/200)), 200)

        screen.fill((a,b,c))


         
        # Render and display hit counts
        perfect_hit_text = hit_count_font.render(f"Perfect: {perfect_hits}", True, (255, 255, 255))
        great_hit_text = hit_count_font.render(f"Great: {great_hits}", True, (255, 255, 255))
        good_hit_text = hit_count_font.render(f"Good: {good_hits}", True, (255, 255, 255))
        miss_hit_text = hit_count_font.render(f"Miss: {miss_hits}", True, (255, 255, 255))
        # Position the hit count texts on the screen
        screen.blit(perfect_hit_text, (50, 150))
        screen.blit(great_hit_text, (50, 200))
        screen.blit(good_hit_text, (50, 250))
        screen.blit(miss_hit_text, (50, 300))
 
            

        # Update and draw notes
        for note in notes:
            note.move()
            note.draw(screen)
        
        # Note Spawning Logic
        for pattern in note_pattern:
            spawn_frame, note_type, key_char, *extra_params = pattern
            if frame_count == spawn_frame:

                note_position = key_positions[key_char] 
                color = (255, 255, 255) if key_char in ('a', 'l') else (50, 255, 255)  # Adjust colors as needed
                if note_type == 'regular':
                    notes.append(Note(note_position, 10, color))
                elif note_type == 'long':
                    length = extra_params[0] 
                    notes.append(LongNote(note_position, 10, color, length))
    
        # Clean up: remove notes out of screen or fully faded long notes

                  # Start the music when the first note spawns
                if not has_music_started:
                    pygame.mixer.music.play(-1)  # -1 means it will loop indefinitely
                    has_music_started = True
        


        # Remove notes that are out of screen
        notes = [note for note in notes if not note.is_out_of_screen()]

        fps = clock.get_fps()

        if fps == 0:
            fps = maxframe
        
        



        for event in pygame.event.get():                    #detect event

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    show_ending_page = True  # Set the flag to show the ending page

            if event.type == pygame.QUIT:                    #close window
                ingame = False
                main = False
           
            if event.type == START_GAME_EVENT:
                pygame.mixer.music.play()

           
            if event.type == pygame.KEYDOWN:                #KEYDOWN INPUT
                if event.key == pygame.K_a:
                    keyset[0] = 1
                    keys_being_held[0] = True
                    for note in notes:
                        if isinstance(note, LongNote):
                            if  note.note_remove(10):
                                remove_note_and_calculate_score(note)
                               
                                
                        else:
                            if note.note_remove():
                                remove_note_and_calculate_score(note)
                                

                if event.key == pygame.K_s:
                    keyset[1] = 1
                    keys_being_held[1] = True
                    for note in  notes:
                        if isinstance(note, LongNote):
                            if note.note_remove(10):
                               remove_note_and_calculate_score(note)
                                
                        else:
                            if note.note_remove():
                                remove_note_and_calculate_score(note)
                               

                if event.key == pygame.K_k:
                    keyset[2] = 1
                    keys_being_held[2] = True
                    for note in  notes:
                        if isinstance(note, LongNote):
                            if note.note_remove(10):
                                remove_note_and_calculate_score(note)
                                
                        else:
                            if note.note_remove():
                                remove_note_and_calculate_score(note)
                                

                if event.key == pygame.K_l:
                    keyset[3] = 1
                    keys_being_held[3] = True
                    for note in  notes:
                        if isinstance(note, LongNote):
                            if note.note_remove(10):
                                remove_note_and_calculate_score(note)
                                
                        else:
                            if note.note_remove():
                                remove_note_and_calculate_score(note)
                                

            if event.type == pygame.KEYUP:                #KEYUP INPUT
                if event.key == pygame.K_a:
                    keyset[0] = 0
                    keys_being_held[0] = False
                if event.key == pygame.K_s:
                    keyset[1] = 0
                    keys_being_held[1] = False
                if event.key == pygame.K_k:
                    keyset[2] = 0
                    keys_being_held[2] = False
                if event.key == pygame.K_l:
                    keyset[3] = 0
                    keys_being_held[3] = False

        if miss_hits > 10:
            show_ending_page = True

        if time.time() - song_start_time >= song_duration:
            show_ending_page = True

        if show_ending_page:
            pygame.mixer.music.pause()
            # Display the ending page
            ending_font = pygame.font.SysFont("Arial", 50)
            ending_text1 = ending_font.render("Game Over! Your Perfect Score: {}".format(perfect_hits), True, (255, 255, 255))
            ending_text2 = ending_font.render("Game Over! Your Great Score: {}".format(great_hits), True, (255, 255, 255))
            ending_text3 = ending_font.render("Game Over! Your Good Score: {}".format(good_hits), True, (255, 255, 255))
            instruction_text = ending_font.render("Press Q to quit.", True, (255, 255, 255))

            screen.fill((0, 0, 0))
            screen.blit(ending_text1, (w // 4, 200))
            screen.blit(ending_text2, (w // 4, 300))
            screen.blit(ending_text3, (w // 4, 400))
            screen.blit(instruction_text, (w // 4, 500))

            pygame.display.flip()

            # Reset game variables
            score = 0
            perfect_hits = 0
            great_hits = 0
            good_hits = 0
            miss_hits = 0
            notes = []
            show_ending_page = False
            ingame = False

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting_for_input = False
                        main = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            waiting_for_input = False
                            main = False
                        elif event.key == pygame.K_r:
                            waiting_for_input = False
                            ingame = True
                            has_music_started = False
                            show_intro_page = True  # Set to True to display the intro page

        
        for i, key_held in enumerate(keys_being_held):
            if key_held:
                for note in notes:
                    # Assuming you'll add a method to check whether the note is at the position of the key i
                    if note.is_at_position(note_positions[i]): 
                        if isinstance(note, LongNote):
                            if note.note_remove(10):  # Perhaps adjust the 10 as per your requirements
                                score += 1

            

        
        
        keys[0] += (keyset[0]- keys[0]) / (2* (maxframe / fps))
        keys[1] += (keyset[1]- keys[1]) / (2* (maxframe / fps))
        keys[2] += (keyset[2]- keys[2]) / (2* (maxframe / fps))
        keys[3] += (keyset[3]- keys[3]) / (2* (maxframe / fps))


        
        
        
    # INPUT EFFECT
    #--------------------------------------------------------------------------------------------
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (255 -((255/7)*i), 255 - ((255/7)*i),\
                255 - ((255/7)*i)),(w / 2 - w / 8 + w / 32 - (w / 32)*keys[0],\
                    (h/12)*9-(h/30)*keys[0]*i,w/16*keys[0],(h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (50 -((50/7)*i), 255 - ((255/7)*i),\
                255 - ((255/7)*i)),(w / 2 - w / 8 + 3*w / 32 - (w / 32)*keys[1],\
                    (h/12)*9-(h/30)*keys[1]*i,w/16*keys[1],(h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (50 -((50/7)*i), 255 - ((255/7)*i), \
                255 - ((255/7)*i)),(w / 2 - w / 8 + 5*w / 32 - (w / 32)*keys[2],\
                    (h/12)*9-(h/30)*keys[2]*i,w/16*keys[2],(h/35)/i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (255 -((255/7)*i), 255- ((255/7)*i), \
                255 - ((255/7)*i)),(w / 2 - w / 8 + 7*w / 32 - (w / 32)*keys[3],\
                    (h/12)*9-(h/30)*keys[3]*i,w/16*keys[3],(h/35)/i))
    #---------------------------------------------------------------------------------------------


    
        score_str = str(score)
        font_1 = pygame.font.SysFont("Courier New", 100)
        this_sentence = font_1.render(score_str, True, (255,255,255))
        
        #DESIGN
        #---------------------------------------------------------------------------------------------

        #sideline
        pygame.draw.rect(screen, (88,88,88),(w/ 2 - w / 8, -int(w/100), w/4, h + int(w/50)), int(w/100))
        
        #bottom line
        pygame.draw.rect(screen, (88,88,88),(w/ 2 - w / 8, (h/12)*9 , w/4, h/2), int(w/100))
        
        screen.blit(this_sentence,(50,50))

        pygame.display.flip()

        clock.tick(FPS)
        #---------------------------------------------------------------------------------------------