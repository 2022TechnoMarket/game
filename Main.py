import sys
import os
import cv2
import pygame as pg 
import time
from google_images_download import google_images_download
from PIL import Image

keyword = input("검색하고 싶은 것:") #검색하고 싶은 객체
limit = 2

def googleImageCrawling(keyword, limit):
      response = google_images_download.googleimagesdownload()
      arguments = {"keywords" : keyword, "limit" : limit, 
                     "print_urls" : True, "chromedriver" : "./chromedriver"}
      paths = response.download(arguments)
      print(paths)

googleImageCrawling(keyword, limit)

pg.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

width = 1240
height = 780
ourScreen = pg.display.set_mode((width, height))
pg.display.set_caption('추억의 게임! 경찰과 도둑') 
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pg.image.load(os.path.join(current_path,"background.jpg"))
game_background = pg.image.load(os.path.join(current_path,"game_back_image.png"))

startimg = pg.image.load(os.path.join(current_path,"startimg.jpg"))
startimg2 = pg.image.load(os.path.join(current_path,"startimg2.jpg"))
startimg = pg.transform.scale(startimg, (170, 80))
startimg2 = pg.transform.scale(startimg2, (170, 80))
quit = pg.image.load(os.path.join(current_path,"quitimg.jpg"))
quit2 = pg.image.load(os.path.join(current_path,"quitimg2.jpg"))
quit = pg.transform.scale(quit, (170, 80))
quit2 = pg.transform.scale(quit2, (170, 80))

police_back = pg.image.load(os.path.join(current_path, "policewin.png"))
thief_back = pg.image.load(os.path.join(current_path, "thiefwin.png"))
quit_img= pg.image.load(os.path.join(current_path, "quit_image.png"))
menu_img= pg.image.load(os.path.join(current_path, "menu_image.png"))
intro_img= pg.image.load(os.path.join(current_path, "intro_img.png"))
arrow_img= pg.image.load(os.path.join(current_path, "arrow_img.png"))
arrow_img = pg.transform.scale(arrow_img, (100, 100))
font = pg.font.SysFont("malgungothic", 30, True, True)
text1 = font.render("도둑 차례 입니다.", False, white)
text2 = font.render("경찰 차례 입니다.", True, white)
start_text1 = font.render("도둑은 시작 위치를 정해주세요.", True, white)
start_text2 = font.render("경찰은 시작 위치를 정해주세요.", True, white)
win_police = font.render("경찰이 이겼습니다.", True, white)
win_thief = font.render("도둑이 이겼습니다.", True, white)
end_music = pg.mixer.Sound("C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/gameover_music.mp3")
menu_music = pg.mixer.Sound("C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/menu_music.mp3")
game_music = pg.mixer.Sound("C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/game_music.mp3")
police_win_music = pg.mixer.Sound('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/police_win_music.mp3')
thief_win_music = pg.mixer.Sound('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/thief_win_music.mp3')
clock = pg.time.Clock()

Point_list=[[404,180],[356, 320],[453, 320],[308, 460],[500, 460],[260,600],[548,600],[836,180],
[788, 320],[884, 320],[740,460],[930,460],[693, 600],[980, 600]]

copy_list = [[404,180],[356, 320],[453, 320],[308, 460],[500, 460],[260,600],[548,600],[836,180],
[788, 320],[884, 320],[740,460],[930,460],[693, 600],[980, 600]]
#Button 클래스 생성
class Button:
     def __init__(self, img_in,x,y,width,height,img_act,x_act,y_act,action=None):
        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if x+width > mouse[0] >x and y+height >mouse[1]>y:
            ourScreen.blit(img_act,(x_act,y_act))
            if click[0] and action !=None:
                time.sleep(0.1)

                action()

        else:
            ourScreen.blit(img_in,(x,y))

def playgame(win):
    mouse_pos = [0,0]
    copy_pos = [0,0]
    con = True
    control = True
    count = 0
    while con:       
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.mouse.get_rel()  
                mouse_pos=pg.mouse.get_pos()
                x=mouse_pos[0]
                y=mouse_pos[1]
                for i in range(0,14):
                    if(x<=Point_list[i][0]+20 and x>=Point_list[i][0]-20):
                        if(y<=Point_list[i][1]+20 and y>=Point_list[i][1]-20):
                            if control: #도둑턴
                                Game_Screen()
                                if count == 0:
                                    ourScreen.blit(img1,(Point_list[i][0] -50, Point_list[i][1]-50))
                                    #copy_pos = mouse_pos
                                    control = False
                                else:
                                    ourScreen.blit(text2,(150,100))
                                    ourScreen.blit(text_turn, (800, 100))
                                    ourScreen.blit(img1,(Point_list[i][0] -50, Point_list[i][1]-50))
                                    ourScreen.blit(img2,(copy_pos[0]-50, copy_pos[1]-50))
                                    #copy_pos = mouse_pos
                                    control = False
                            else: #경찰턴
                                Game_Screen()
                                if count != 0:
                                    ourScreen.blit(text1,(150,100))
                                ourScreen.blit(img1,(copy_pos[0]-50, copy_pos[1]-50))
                                ourScreen.blit(img2,(Point_list[i][0] -50, Point_list[i][1]-50))
                                control = True
                                count += 1
                                if count >= 10:
                                    text_turn = font.render('마지막 턴 입니다.', True, white)
                                else:
                                    text_turn = font.render('{}턴 째 입니다.'.format(count), True, white)
                                ourScreen.blit(text_turn, (800, 100))
                                if count == 1:
                                    ourScreen.blit(text_turn, (800, 100))
                                    ourScreen.blit(text1,(150,100))
                            pg.display.update()
                            if mouse_pos[0] + 60 > copy_pos[0] > mouse_pos[0] - 20 and mouse_pos[1] + 60 > copy_pos[1] > mouse_pos[1] - 20:
                                con = False
                                return True
                            elif count > 10:
                                con = False
                                return False
                            copy_pos[0] = Point_list[i][0]
                            copy_pos[1] = Point_list[i][1]
                            if count == 0:
                                ourScreen.blit(start_text2, (150, 100))
            
            if event.type==pg.QUIT:
                sys.exit()
            pg.display.flip()

def Game_Screen():
    White=(255,255,255)
    ourScreen.blit(game_background, (0,0))       
    pg.draw.line(ourScreen,White,[260,600],[980,600],5)
    pg.draw.line(ourScreen,White,[308,460],[930,460],5)
    pg.draw.line(ourScreen,White,[356,320],[882,320],5)
    pg.draw.line(ourScreen,White,[500,530],[400,480],5)
    pg.draw.line(ourScreen,White,[500,530],[400,530],5)
    pg.draw.line(ourScreen,White,[500,530],[400,580],5)
    pg.draw.line(ourScreen,White,[740,530],[840,530],5)
    pg.draw.line(ourScreen,White,[740,530],[840,480],5)
    pg.draw.line(ourScreen,White,[740,530],[840,580],5)
    pg.draw.polygon(ourScreen,White,[[404,180],[260,600],[548,600]],5)
    pg.draw.polygon(ourScreen,White,[[836,180],[692,600],[980,600]],5)
    pg.draw.circle(ourScreen,White,[460,430],10,4)
    pg.draw.circle(ourScreen,White,[780,430],10,4)

def quitgame():
    pg.quit()
    sys.exit()

x = int(limit)
#imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)
#download_image_path = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)
if os.path.isdir('C:/Users/trans/downloads/{}/'.format(keyword)):
    imagepath = 'C:/Users/trans/downloads/{}/'.format(keyword)
    download_image_path = 'C:/Users/trans/downloads/{}/'.format(keyword)
elif os.path.isdir('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/'.format(keyword)):
    imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/'.format(keyword)
    download_image_path = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/'.format(keyword)
elif os.path.isdir('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)):
    imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)
    download_image_path = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)

os.chdir(imagepath)
files = os.listdir(imagepath)
jpg = []

for file in files:
    if '.jpg' or '.png' in file:
        f = cv2.imread(file)
        jpg.append(f)
        
file_number = 0
try:
    img1 = pg.image.load(download_image_path + '{}'.format(files[file_number]))
except:
    file_number = 1
    img1 = pg.image.load(download_image_path + '{}'.format(files[file_number]))

print(file_number)
print(files)

finish = False

clock = pg.time.Clock()

img1 = pg.transform.scale(img1, (100, 100))

img2 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/police_icon.jpg')
img2 = pg.transform.scale(img2, (100, 100))

pg.draw.rect(ourScreen, white, [100, 100, 100, 100])

con = True
def introscreen():
    start = True
    while start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        ourScreen.blit(intro_img, (0, 0))
        NexttButton = Button(arrow_img,900,600,100,100,arrow_img,900,580,gamescreen)
        pg.display.update()


def gamescreen():
    menu_music.stop()
    game_music.set_volume(0.3)
    game_music.play(-1)
    Game_Screen()
    ourScreen.blit(start_text1, (150, 100))
    win = True
    win = playgame(win)
    game_music.stop()
    result(win)


def mainmenu():
    end_music.stop()
    menu_music.set_volume(0.4)
    menu_music.play(-1)
    menu=True
    while menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        backscreen = ourScreen.blit(background,(0,0))
        startButton = Button(startimg,830,370,120,50,startimg2,830,370,introscreen)
        quitButton = Button(quit,830,470,120,50,quit2,830,470,quitgame)
        pg.display.update()

def result(win):
    end_music.set_volume(0.3)
    end_music.play(loops = 0)
    while True:         
        for event in pg.event.get():
            ourScreen.fill(black) 
            if win:
                ourScreen.blit(police_back, (0,0))
                ourScreen.blit(win_police,(50,50))
            else:
                ourScreen.blit(thief_back, (0,0))
                ourScreen.blit(win_thief, (50,50))
            if event.type==pg.QUIT:
                sys.exit()
            startButton = Button(menu_img,300,650,210,100,menu_img,300,630,mainmenu)
            quitButton = Button(quit_img,820,650,210,100,quit_img,820,630,quitgame)
            pg.display.flip()

mainmenu()

#음악넣기
#결과창에 버튼 바꾸기 정도?
#한칸씩움직이는거