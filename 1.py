from urllib.request import urlretrieve
from urllib.parse import quote_plus    
from bs4 import BeautifulSoup as BS    
from selenium import webdriver

keyword = input("Image Name : ")
i_URL = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk00OQamJ34t56QSInnMzwcC5gC344w:1594968011157&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXs-7t1tPqAhVF7GEKHfM4DqsQ_AUoAXoECBoQAw&biw=1536&bih=754'

driver=webdriver.Chrome('C://chromedriver.exe') #크롬 드라이버
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(i_URL)

html = driver.page_source
soup = BS(html,features="html.parser")

img = soup.select('img')

i_list = []
count = 1

print("Searching...")
for i in img:
   try:
      i_list.append(i.attrs["src"])
   except KeyError:
      i_list.append(i.attrs["data-src"])

print("Downloading...")
for i in i_list:
   urlretrieve(i,"download/"+keyword+str(count)+".jpg")
   count+=1

driver.close()
print("FINISH")

# import sys
# import pygame
# from pygame.locals import *
# 
# ## pygame 기능 사용을 시작하는 명령어 ##
# pygame.init()
# ## 초당 프레임 단위 설정 ##
# 
# screen_width = 640 #가로 크기
# screen_height = 480 #세로 크기
# screen = pygame.display.set_mode((screen_width, screen_height))
# 
# #화면 타이틀 설정
# pygame.display.set_caption("HwanE Game")
# 
# running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
# while running:
#     for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
#         if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
#             running = False
# 
# 
# #pygame 종료
# pygame.quit()

# import pygame
# import sys
# 
# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480
# 
# white = (255, 255, 255)
# black = (0, 0, 0)
# 
# pygame.init()
# pygame.display.set_caption("Simple PyGame Example")
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 
# pos_x = 200
# pos_y = 200
# 
# clock = pygame.time.Clock()
# while True:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
# 
#     key_event = pygame.key.get_pressed()
#     if key_event[pygame.K_LEFT]:
#         pos_x -= 2
# 
#     if key_event[pygame.K_RIGHT]:
#         pos_x += 2
# 
#     if key_event[pygame.K_UP]:
#         pos_y -= 2
# 
#     if key_event[pygame.K_DOWN]:
#         pos_y += 2
# 
#     screen.fill(black)
#     pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
#     pygame.display.update()