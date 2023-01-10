import pygame  # 1. pygame 선언
from pygame.locals import *
import random

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

bgm = pygame.mixer.Sound('../Zoo-Kindergarden/resource/Girasol-Quincas-Moreira.wav')
man_to_apple = pygame.mixer.Sound('../Zoo-Kindergarden/resource/Pop.wav')
size = [600, 600]
screen = pygame.display.set_mode(size)
score = 0

done = 0
clock = pygame.time.Clock()

def runGame():
    bgm.play(loops=-1)
    back_image = pygame.image.load('../Zoo-Kindergarden/resource/backgr.jpg')
    back_image = pygame.transform.scale(back_image, (600, 600))
    apple_image = pygame.image.load('../Zoo-Kindergarden/resource/apple.png')
    apple_image = pygame.transform.scale(apple_image, (50, 50))
    apples = []

    for i in range(3):
        rect = pygame.Rect(apple_image.get_rect())
        rect.left = random.randint(100, size[0]-100)
        rect.top = -100
        dy = random.randint(3, 9)  #빠르기
        apples.append({'rect': rect, 'dy': dy})

    person_image = pygame.image.load('../Zoo-Kindergarden/resource/person.png')
    person_image = pygame.transform.scale(person_image, (90, 160))
    person = pygame.Rect(person_image.get_rect())
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0


    global done
    while not done:
        global score

        clock.tick(30)
        screen.blit(back_image, (0, 0))

        fontObj = pygame.font.Font(None, 32)
        textSurfaceObj = fontObj.render('Score : ' + str(score), True, (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect();
        textRectObj.center = (70, 30)
        screen.blit(textSurfaceObj, textRectObj)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -10
                elif event.key == pygame.K_RIGHT:
                    person_dx = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

        for idx in range(len(apples)):
            if apples[idx]['rect'].colliderect(person):
                apples.remove(apples[idx])
                rect = pygame.Rect(apple_image.get_rect())
                rect.left = random.randint(100, size[0]-100)
                rect.top = -100
                dy = random.randint(3, 9)
                man_to_apple.play()
                score += 1
                if score >= 20:
                    done = 2
                apples.append({'rect': rect, 'dy': dy})

            screen.blit(apple_image, apples[idx]['rect'])

        for idx in range(len(apples)):
            apples[idx]['rect'].top += apples[idx]['dy']
            if apples[idx]['rect'].top > size[1]:
                apples.remove(apples[idx])
                rect = pygame.Rect(apple_image.get_rect())
                rect.left = random.randint(100, size[0]-100)
                rect.top = -100
                dy = random.randint(3, 9)
                apples.append({'rect': rect, 'dy': dy})
                done = 1

        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)

        pygame.display.update()

    if done == 1:
        gover_image = pygame.image.load('../Zoo-Kindergarden/resource/game_over.png')
        gover_image = pygame.transform.scale(gover_image, (300, 300))
        screen.blit(gover_image, [150,150])
    elif done == 2:
        gclr_image = pygame.image.load('../Zoo-Kindergarden/resource/game_clear.png')
        gclr_image = pygame.transform.scale(gclr_image, (300, 300))
        screen.blit(gclr_image, [150,150])
    pygame.display.update()
    clock.tick(1)


runGame()
pygame.quit()