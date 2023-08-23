import turtle, random, winsound

wn = turtle.Screen()
wn.title("으악 떨어진다")
wn.bgpic("/img/bgpicture.gif")
wn.setup(width=800, height=600)
wn.tracer(10)

wn.register_shape("/img/player_right.gif")
wn.register_shape("/img/player_left.gif")
wn.register_shape("/img/good.gif")
wn.register_shape("/img/bad.gif")


# 점수 추가
score = 0
life = 3


# 사용자 추가
# player
player=turtle.Turtle()
player.speed(1)
player.shape("/img/player_right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"


# goods
goods = []

for _ in range(5):
    good=turtle.Turtle()
    good.speed = random.randint(3, 5)
    good.shape("/img/good.gif")
    good.color("blue")
    good.penup()
    good.goto(100, 250)
    goods.append(good)

# bads
bads = []

for _ in range(5):
    bad=turtle.Turtle()
    bad.speed = random.randint(3, 5)
    bad.shape("/img/bad.gif")
    bad.color("red")
    bad.penup()
    bad.goto(-100, 250)
    bads.append(bad)


# 점수
pen=turtle.Turtle()
pen.ht()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("courier", 24, "normal")
pen.write(f"Score: {(score)} life:{(life)}", align="center", font = font)


# 방향 가리키기
def go_left():
    player.direction = "left"
    player.shape("/img/player_left.gif")
    
def go_right():
    player.direction = "right"
    player.shape("/img/player_right.gif")


# 키보드와 연결
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



# 메인 게임
while True:
    wn.update()

    # player 좌우로 움직이게 하는 부분
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x) 


    # good들 상하로 움직이게 하는 부분
    for good in goods:
        y = good.ycor()
        y -= good.speed
        good.sety(y)

        # 벽에 가면 제자리로
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)


        # player와 good들이 만났을 때 제자리
        if good.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)
            winsound.PlaySound("/sound/good.wav", winsound.SND_ASYNC)
            
            # 점수
            score += 10
            
            pen.clear()
            pen.write(f"Score: {(score)} life:{(life)}", align="center", font = font)


    # bad들 상하로 움직이게 하는 부분
    for bad in bads:
        y = bad.ycor()
        y -= bad.speed
        bad.sety(y)

        # 벽에 가면 제자리로
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)

        # player와 bad들이 만났을 때 제자리
        if bad.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)
            winsound.PlaySound("/sound/bad.wav", winsound.SND_ASYNC)
            # 점수 및 생명
            score -= 10
            life -= 1
            pen.clear()
            pen.write(f"Score: {(score)} life:{(life)}", align="center", font = font)



wn.mainloop()
