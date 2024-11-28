import pygame
import random

#視窗設定
pygame.init()
screen= pygame.display.set_mode((1600,900))
gamestart = False
running = True
gameend = False
selected = False

green = (0,200,0)
white = (0,0,0)
color1 = [green,white,white]
color2 = [green,white,white]
counts = 0
combo = 0
circleRadius = 60
timelast = 15

pos = (0,0)
pygame.display.set_caption("Click the circle!")
#圓圈函數
class circle:
    def __init__(self,x,y,radius):
        self.pos = (x, y)
        self.xmargin = (x - radius, x + radius)
        self.ymargin = (y - radius, y + radius)
        self.radius = radius
        
#第一次隨機位置
x = random.randint(120,900)
y = random.randint(100,650)
#滑鼠在圈圈內
def within(x,floor,ceil):
    return (floor <= x <= ceil)

#開始畫面
while running:
    pygame.time.Clock().tick(20)
    screen.fill((255,255,255))

    #開頭字
    my_font = pygame.font.SysFont('Comic Sans MS', 60)
    text_surface = my_font.render("Click the circle!", False, (0, 0, 0))
    screen.blit(text_surface, (100,100))
    my_font = pygame.font.SysFont('Comic Sans MS', 40)
    text_surface = my_font.render("Your Goal is to click as many circles as you can!", False, (0, 0, 0))
    screen.blit(text_surface, (100,200))
    #開始按鈕
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(100,300,200,100),3) 
    screen.blit(my_font.render("Start", False, (0, 0, 0)), (150,320))
    #退出按鈕
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(350,300,200,100),3)
    screen.blit(my_font.render("Quit", False, (0, 0, 0)), (400,320))
    #學號
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen.blit(my_font.render("", False, (0, 0, 0)), (1400,800))
    #時間長度(字)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1000,500,100,80),3)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1150,500,100,80),3)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1300,500,100,80),3)
    screen.blit(my_font.render("Time", False, white), (1000,450))
    screen.blit(my_font.render("15s", False, color1[0]), (1025,520))
    screen.blit(my_font.render("30s", False, color1[1]), (1175,520))
    screen.blit(my_font.render("60s", False, color1[2]), (1325,520))
    #難度-圈大小(字)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1000,650,130,80),3)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1150,650,140,80),3)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1300,650,130,80),3)
    screen.blit(my_font.render("Difficulty", False, white), (1000,600))
    screen.blit(my_font.render("Easy", False, color2[0]), (1025,670))
    screen.blit(my_font.render("Normal", False, color2[1]), (1175,670))
    screen.blit(my_font.render("Hard", False, color2[2]), (1325,670))

    #偵測按鍵
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            pos = pygame.mouse.get_pos()
            if (within(pos[0],100,300) and within(pos[1],300,400)):
                gamestart = True
                running = False
            elif (within(pos[0],350,550) and within(pos[1],300,400)):
                running = False
            #時間
            elif (within(pos[0],1000,1100) and within(pos[1],500,580)):
                color1[0] = green
                color1[1] = white
                color1[2] = white
                timelast = 15
            elif (within(pos[0],1150,1250) and within(pos[1],500,580)):
                color1[0] = white
                color1[1] = green
                color1[2] = white
                timelast = 30
            elif (within(pos[0],1300,1400) and within(pos[1],500,580)):
                color1[0] = white
                color1[1] = white
                color1[2] = green
                timelast = 60
            #難度
            elif (within(pos[0],1000,1130) and within(pos[1],650,730)):
                color2[0] = green
                color2[1] = white
                color2[2] = white
                circleRadius = 60
            elif (within(pos[0],1150,1290) and within(pos[1],650,730)):
                color2[0] = white
                color2[1] = green
                color2[2] = white
                circleRadius = 45
            elif (within(pos[0],1300,1430) and within(pos[1],650,730)):
                color2[0] = white
                color2[1] = white
                color2[2] = green
                circleRadius = 30

    pygame.display.update()         
   
timetick = 0
second = timelast
time_goal = 0
#遊戲執行中
while gamestart:
    pygame.time.Clock().tick(100)
    main_circle = circle(x, y ,circleRadius)
    
    if gameend == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestart = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (
                    event.button == 1 and
                    within(pos[0],main_circle.xmargin[0],main_circle.xmargin[1]) and
                    within(pos[1],main_circle.ymargin[0],main_circle.ymargin[1])
                    ):
                        selected = True
                        counts+=1
                        print(counts)
                        x = random.randint(20,28)*random.randint(10,50)
                        y = random.randint(10,35)*random.randint(20,20)
                #跳過按鈕        
                elif event.button == 1 and (within(pos[0],25,50) and within(pos[1],850,875)):
                    second = 0
                    gameend = True
            
            else: selected = False
        timetick+=1
        if timetick == 100:
            second-=1
            timetick =0
        if second == 0:
            gameend = True
    
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1250,20,300,40),3)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(1250,20,second*(300/timelast),40))
    screen.blit(my_font.render("Combo: "+str(counts), False, (0, 0, 0)), (40,20))
    
    if(selected==False):
        pygame.draw.circle(screen, (0,0,0), main_circle.pos, main_circle.radius , 3)
        screen.blit(my_font.render(str(counts), False, (0, 0, 0)), (x-11,y-22))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(25,850,25,25),3) 
#結算畫面
    if(gameend == True):
        #gane over
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(400,200,640,368))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(400,200,640,368),3)
        my_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_surface = my_font.render("Game Over", False, (0, 0, 0))
        screen.blit(text_surface, (450,250))
        #分數
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render("Score:"+str(counts), False, (0, 0, 0))
        screen.blit(text_surface, (450,350))
        #蟲是
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(450,400,250,100),3)
        my_font = pygame.font.SysFont('Comic Sans MS', 38)
        text_surface = my_font.render("Try Again", False, (0, 0, 0))
        screen.blit(text_surface, (470,420))
        #離開
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(750,400,250,100),3)
        my_font = pygame.font.SysFont('Comic Sans MS', 38)
        text_surface = my_font.render("Quit", False, (0, 0, 0))
        screen.blit(text_surface, (770,420))
        #偵測按鍵
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1 and (within(pos[0],450,700) and within(pos[1],400,500)):
                    timetick = 0
                    second = timelast
                    counts = 0
                    gamestart = True
                    running = False
                    gameend = False
                elif event.button == 1 and (within(pos[0],750,1000) and within(pos[1],400,500)):
                    gamestart = False
                    running = False
                    gameend = False
    pygame.display.update()
pygame.quit()