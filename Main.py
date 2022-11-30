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
startimg = pg.image.load(os.path.join(current_path,"startimg.jpg"))
startimg2 = pg.image.load(os.path.join(current_path,"startimg2.jpg"))
quit = pg.image.load(os.path.join(current_path,"quitimg.jpg"))
quit2 = pg.image.load(os.path.join(current_path,"quitimg2.jpg"))
police_back = pg.image.load(os.path.join(current_path, "policewin.png"))
thief_back = pg.image.load(os.path.join(current_path, "thiefwin.png"))
font = pg.font.SysFont("malgungothic", 30, True, True)
text1 = font.render("도둑 차례 입니다.", True, white)
text2 = font.render("경찰 차례 입니다.", True, white)
start_text1 = font.render("도둑은 시작 위치를 정해주세요.", True, white)
start_text2 = font.render("경찰은 시작 위치를 정해주세요.", True, white)
win_police = font.render("경찰이 이겼습니다.", True, white)
win_thief = font.render("도둑이 이겼습니다.", True, white)

clock = pg.time.Clock()

Point_list=[[404,180],[356, 320],[453, 320],[308, 460],[500, 460],[260,600],[548,600],[836,180],
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
                                    ourScreen.blit(img1,(mouse_pos[0]-50, mouse_pos[1]-50))
                                    #copy_pos = mouse_pos
                                    control = False
                                else:
                                    ourScreen.blit(text2,(50,50))
                                    ourScreen.blit(text_turn, (900, 50))
                                    ourScreen.blit(img1,(mouse_pos[0]-50, mouse_pos[1]-50))
                                    ourScreen.blit(img2,(copy_pos[0]-50, copy_pos[1]-50))
                                    #copy_pos = mouse_pos
                                    control = False
                            else: #경찰턴
                                Game_Screen()
                                if count != 0:
                                    ourScreen.blit(text1,(50,50))
                                ourScreen.blit(img1,(copy_pos[0]-50, copy_pos[1]-50))
                                ourScreen.blit(img2,(mouse_pos[0]-50, mouse_pos[1]-50))
                                control = True
                                count += 1
                                if count >= 10:
                                    text_turn = font.render('마지막 턴 입니다.', True, white)
                                else:
                                    text_turn = font.render('{}턴 째 입니다.'.format(count), True, white)
                                ourScreen.blit(text_turn, (900, 50))
                                if count == 1:
                                    ourScreen.blit(text_turn, (900, 50))
                                    ourScreen.blit(text1,(50,50))
                            pg.display.update()
                            if mouse_pos[0] + 60 > copy_pos[0] > mouse_pos[0] - 20 and mouse_pos[1] + 60 > copy_pos[1] > mouse_pos[1] - 20:
                                con = False
                                return True
                            elif count > 10:
                                con = False
                                return False
                            copy_pos = mouse_pos
                            if count == 0:
                                ourScreen.blit(start_text2, (50, 50))
            
            if event.type==pg.QUIT:
                sys.exit()
            pg.display.flip()

def Game_Screen():
    White=(255,255,255)
    ourScreen.fill(black)        
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

img2 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/namu.jpg')
img2 = pg.transform.scale(img2, (100, 100))

pg.draw.rect(ourScreen, white, [100, 100, 100, 100])

con = True
def gamescreen():
    Game_Screen()
    ourScreen.blit(start_text1, (50, 50))
    win = True
    win = playgame(win)
    result(win)


def mainmenu():
    menu=True
    while menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        backscreen = ourScreen.blit(background,(0,0))
        #titletext =screen.blit(titlename,(130,120))
        startButton = Button(startimg,830,370,120,50,startimg2,830,370,gamescreen)
        quitButton = Button(quit,820,470,120,50,quit2,820,470,quitgame)
        pg.display.update()

def result(win):
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
            startButton = Button(startimg,830,370,120,50,startimg2,830,370,mainmenu)
            quitButton = Button(quit,820,470,120,50,quit2,820,470,quitgame)
            pg.display.flip()

mainmenu()

#음악넣기
#결과창에 버튼 바꾸기 정도?
#한칸씩움직이는거