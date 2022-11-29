import sys
import os
import cv2
import pygame as pg 
from google_images_download import google_images_download
from PIL import Image

def googleImageCrawling(keyword, limit):
      
      response = google_images_download.googleimagesdownload()

      arguments = {"keywords" : keyword, "limit" : limit, 
                     "print_urls" : True, "chromedriver" : "./chromedeirver", "format" : "jpg"}
      paths = response.download(arguments)
      #img[i] = pygame.image.load(paths)
      print(paths)
      

keyword = input("검색하고 싶은 것:")
limit = 1

googleImageCrawling(keyword, limit)

x = int(limit)
imagepath = 'C:/Users/trans/downloads/{}/'.format(keyword)
#imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/'.format(keyword)
#imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/'.format(keyword)
os.chdir(imagepath)
files = os.listdir(imagepath)

jpg = []

for file in files:
    if '.jpg' in file:
        f = cv2.imread(file)
        jpg.append(f)

print(files)

width = 1240
height = 780

pg.display.set_caption('추억의 게임! 경찰과 도둑') 
finish = False

pg.init()
ourScreen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
img1 = pg.image.load('C:/Users/trans/downloads/{}/{}'.format(keyword, files[0]))
#img1 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/{}'.format(keyword, files[0]))
#img1 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/dist/Main/downloads/{}/{}'.format(keyword, files[0]))
img1 = pg.transform.scale(img1, (100, 100))


img2 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/namu.jpg')
img2 = pg.transform.scale(img2, (100, 100))

pos_x = 200
pos_y = 300

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

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




mouse_pos = [0,0]
copy_pos = [0,0]

pg.draw.rect(ourScreen, white, [100, 100, 100, 100])

con = True
while con:         
    for event in pg.event.get(): 
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.get_rel()  
            mouse_pos=pg.mouse.get_pos()
            if 200 > mouse_pos[0] > 100 and 200 > mouse_pos[1] > 100:
                pg.draw.rect(ourScreen, red, [100, 100, 100, 100])
                pg.display.update()
                con = False
        if event.type==pg.QUIT:
            sys.exit()
        pg.display.flip()

Point_list=[[404,180],[356, 320],[453, 320],[308, 460],[500, 460],[260,600],[548,600],[836,180],
[788, 320],[884, 320],[740,460],[930,460],[693, 600],[980, 600]]
Game_Screen()
font = pg.font.SysFont("malgungothic", 30, True, True)
text1 = font.render("도둑 차례 입니다.", True, white)
text2 = font.render("경찰 차례 입니다.", True, white)
start_text1 = font.render("도둑은 시작 위치를 정해주세요.", True, white)
start_text2 = font.render("경찰은 시작 위치를 정해주세요.", True, white)

ourScreen.blit(start_text1, (50, 50))

con = True
police_win = False
count = 0
control = True

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
                                print(count)
                                print(copy_pos)
                                print(mouse_pos)
                        else: #경찰턴
                            Game_Screen()
                            print(count)
                            if count != 0:
                                ourScreen.blit(text1,(50,50))
                            ourScreen.blit(img1,(copy_pos[0]-50, copy_pos[1]-50))
                            ourScreen.blit(img2,(mouse_pos[0]-50, mouse_pos[1]-50))
                            print(copy_pos)
                            print(mouse_pos)
                            control = True
                            count += 1
                            if count == 10:
                                text_turn = font.render('마지막 턴 입니다.', True, white)
                            else:
                                text_turn = font.render('{}턴 째 입니다.'.format(count), True, white)
                            ourScreen.blit(text_turn, (900, 50))
                            if count == 1:
                                ourScreen.blit(text_turn, (900, 50))
                                ourScreen.blit(text1,(50,50))
                        pg.display.update()
            if mouse_pos[0] + 80 > copy_pos[0] > mouse_pos[0] - 30 and mouse_pos[1] + 80 > copy_pos[1] > mouse_pos[1] - 30:
                con = False
                police_win = True
            if count > 10:
                con = False
                police_win = False
            copy_pos = mouse_pos
            if count == 0:
                ourScreen.blit(start_text2, (50, 50))
            print(count)
           
        if event.type==pg.QUIT:
            sys.exit()
        pg.display.flip()


win_police = font.render("경찰이 이겼습니다.", True, white)
win_thief = font.render("도둑이 이겼습니다.", True, white)

while True:         
    for event in pg.event.get(): 
        ourScreen.fill(black)   
        if police_win:
            ourScreen.blit(win_police,(50,50))
        else:
            ourScreen.blit(win_thief, (50,50))
        if event.type==pg.QUIT:
            sys.exit()
        pg.display.flip()
