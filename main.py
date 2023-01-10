import pygame
from apple_game import apple_game


pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
size = [1280, 720]

screen = pygame.display.set_mode(size)

# 배경 이미지 불러오기
button1 = pygame.image.load("./button1.png")
button1 = pygame.transform.scale(button1,(400, 70))
button2 = pygame.image.load("./button2.png")
button2 = pygame.transform.scale(button2,(400, 70))


background = pygame.image.load("./background.jpg")
background = pygame.transform.scale(background,(1280, 720))



screen.blit(background, (0, 0))  # 배경 그리기(background 가 표시되는 위치)
screen.blit(button1, (200, 450))
screen.blit(button2, (700, 450))

button = []
left = [700, 200]
for i in range(2):
    rect = pygame.Rect(button1.get_rect(left=left.pop(),top=450))
    button.append(rect)







def run():
    running = True # 게임이 진행중인지 확인하기
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    if button[0].collidepoint(event.pos):
                        pygame.display.set_mode(size = (600, 600))
                        apple_game.runGame()
                    if button[1].collidepoint(event.pos):
                        from CardGame import cardGame
    pygame.quit()
pygame.display.update() # 게임화면을 지속적으로 그리기(for문도는동안 계속)


# pygame 종료
run()