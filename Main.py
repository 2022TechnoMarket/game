import sys
import os
import cv2
import pygame as pg 
from google_images_download import google_images_download

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
imagepath = 'C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/'.format(keyword)
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

img1 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/downloads/{}/{}'.format(keyword, files[0]))
img1 = pg.transform.scale(img1,(100,100))

img2 = pg.image.load('C:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/namu.jpg')
img2 = pg.transform.scale(img2, (100, 100))

pos_x = 200
pos_y = 300

white = (255,255,255)
black = (0,0,0)
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

Game_Screen()

control = True

mouse_pos = [0,0]
copy_pos = [0,0]

while True:                 
    for event in pg.event.get():    
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.get_rel()  
            mouse_pos=pg.mouse.get_pos()
            if control:
                Game_Screen()
                ourScreen.blit(img1,(mouse_pos[0] -50, mouse_pos[1]-50))
                ourScreen.blit(img2,(copy_pos[0]-50, copy_pos[1]-50))
                copy_pos = mouse_pos
                control = False
            else:
                Game_Screen()
                ourScreen.blit(img1,(copy_pos[0]-50, copy_pos[1]-50))
                ourScreen.blit(img2,(mouse_pos[0]-50, mouse_pos[1]-50))
                copy_pos = mouse_pos
                control = True
            pg.display.update()
        if event.type==pg.QUIT:
            sys.exit()
        pg.display.flip()

