import turtle as t
import random
import time
import re


def find_card(x,y):  # 마우스 클릭지점에 따라서 어떤 카드 선택했는지 계산하는 함수
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx


def score_update(m):  # 점수판 
    score_pen.clear()
    score_pen.write(f"{m}  {score}점/ {attempt}번 시도", False, "center", ("", 15))

def result(m):
        t.goto(0, -60)
        t.write(m, False, "center", ("", 30, "bold"))

def play(x, y):  # 메인함수
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score
    global pic_num

    if attempt == 12:  # 시도 횟수가 12번 넘어갈 시 실패(클릭 수로 따지면 24회)
        result("Game Over")
        t.bye()

    else:
        click_num += 1
        card_idx = find_card(x, y)
        turtles[card_idx].shape(img_list[card_idx])

        if click_num == 1:
            first_pick = card_idx
        elif click_num == 2:
            second_pick = card_idx
            click_num = 0
            attempt += 1
            
            if pic_num[first_pick] == pic_num[second_pick]-8 or pic_num[first_pick]-8 == pic_num[second_pick]:
                score += 1
                score_update("정답")
                if score == 8:
                    result("성공")
                    t.bye()
            else:
                score_update("오답")
                turtles[first_pick].shape(default_img)
                turtles[second_pick].shape(default_img)

scr = t.Screen()
scr.setup(700, 700)
scr.bgpic("./elements/background.gif")
t.up()
t.ht()
t.goto(0, 280)
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))

score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0, 230)

turtles = []  # 좌표 설치
pos_x = [-240, -80, 80, 240]
pos_y = [-245, -110, 25, 160]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("light green")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "./elements/default_img.gif"  # 가림막 불러오기
t.addshape(default_img)

img_list = []  # 이미지 불러오기
for i in range(16):
    img = f"elements/{i}.gif"
    t.addshape(img)
    img_list.append(img)

random.shuffle(img_list)  # 이미지 섞고, 좌표에 설치하기
pic_num = []

for i in range(16):
    pic_num += re.findall(r'\d+', img_list[i])
    turtles[i].shape(img_list[i])
pic_num = list(map(int, pic_num))
time.sleep(3)  # 3초 후

for i in range(16):
    turtles[i].shape(default_img)  # 가림막 소환

click_num = 0  # 변수 초기화
score = 0
attempt = 0
first_pick = ""
second_pick = ""

t.onscreenclick(play)  # 클릭 감지될 때마다 Play 함수 실행
t.done()