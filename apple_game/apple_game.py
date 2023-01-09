import pygame  # 1. pygame 선언
import random

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

bgm = pygame.mixer.Sound('Girasol-Quincas-Moreira.wav')
man_to_apple = pygame.mixer.Sound('Pop.wav')
size = [600, 600]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    bgm.play(loops=-1)
    back_image = pygame.image.load('resource/backgr.jpg')
    back_image = pygame.transform.scale(back_image, (600, 600))
    apple_image = pygame.image.load('resource/apple.png')
    apple_image = pygame.transform.scale(apple_image, (50, 50))
    apples = []

    for i in range(3):
        rect = pygame.Rect(apple_image.get_rect())
        rect.left = random.randint(100, size[0]-100)
        rect.top = -100
        dy = random.randint(3, 9)  #빠르기
        apples.append({'rect': rect, 'dy': dy})

    person_image = pygame.image.load('resource/person.png')
    person_image = pygame.transform.scale(person_image, (90, 160))
    person = pygame.Rect(person_image.get_rect())
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0


    global done
    while not done:
        clock.tick(30)
        screen.blit(back_image, (0, 0))

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

        for apple in apples:
            if apple['rect'].colliderect(person):
                apples.remove(apple)
                rect = pygame.Rect(apple_image.get_rect())
                rect.left = random.randint(100, size[0]-100)
                rect.top = -100
                dy = random.randint(3, 9)
                man_to_apple.play()
                apples.append({'rect': rect, 'dy': dy})

            screen.blit(apple_image, apple['rect'])

        for apple in apples:
            apple['rect'].top += apple['dy']
            if apple['rect'].top > size[1]:
                apples.remove(apple)
                rect = pygame.Rect(apple_image.get_rect())
                rect.left = random.randint(100, size[0]-100)
                rect.top = -100
                dy = random.randint(3, 9)
                apples.append({'rect': rect, 'dy': dy})
                done = True

        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)

        pygame.display.update()


runGame()
pygame.quit()
