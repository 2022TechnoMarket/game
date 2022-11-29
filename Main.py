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


pos_x = 200
pos_y = 300

white = (255,255,255)
black = (0,0,0)
def Game_Screen():
    White=(255,255,255)            
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

while True:                  
    for event in pg.event.get():    
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.get_rel()  
            mouse_pos=pg.mouse.get_pos()
            ourScreen.blit(img1,(mouse_pos[0], mouse_pos[1]))
            pg.display.update()
        if event.type==pg.QUIT:
            sys.exit()
        pg.display.flip()

# while True:
#     clock.tick(60)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             sys.exit()

#     key_event = pg.key.get_pressed()
#     if key_event[pg.K_LEFT]:
#         pos_x -= 1

#     if key_event[pygame.K_RIGHT]:
#         pos_x += 1

#     if key_event[pygame.K_UP]:
#         pos_y -= 1

#     if key_event[pygame.K_DOWN]:
#         pos_y += 1

#     screen.fill(black)
#     screen.blit(img1,(pos_x, pos_y))
#     pg.display.update()



# from selenium import webdriver
# from bs4 import BeautifulSoup as soups

# def search_selenium(search_name, search_path, search_limit) :
#     search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
#     browser = webdriver.Chrome('c:/chromedriver.exe')
#     browser.get(search_url)
    
#     image_count = len(browser.find_elements_by_tag_name("img"))
    
#     print("로드된 이미지 개수 : ", image_count)

#     browser.implicitly_wait(2)

#     for i in range( search_limit ) :
#         image = browser.find_elements_by_tag_name("img")[i]
#         image.screenshot("c:/Users/trans/Desktop/ALLFILES/Programs/Python/techno/" + str(i) + ".png")

#     browser.close()

# if __name__ == "__main__" :

#     search_name = input("검색하고 싶은 키워드 : ")
#     search_limit = int(input("원하는 이미지 수집 개수 : "))
#     search_path = "Your Path"
#     # search_maybe(search_name, search_limit, search_path)
#     search_selenium(search_name, search_path, search_limit)