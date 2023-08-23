import turtle, random, winsound, time, math

wn = turtle.Screen()
wn.title("으악 떨어진다")
wn.bgpic("/img/bgpicture.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("/img/player_right_life.gif")
wn.register_shape("/img/player_left_life.gif")
wn.register_shape("/img/player_right.gif")
wn.register_shape("/img/player_left.gif")
wn.register_shape("/img/good.gif")
wn.register_shape("/img/bad.gif")


# 점수 추가
score = 0
life = 3
high_score = 0

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

for _ in range(10):
    good=turtle.Turtle()
    good.speed = random.randint(3, 5)
    good.shape("/img/good.gif")
    good.color("blue")
    good.penup()
    # 1번째 문제상황(아군)
    x = random.randint(-380, 380)
    y = random.randint(300, 500)
    good.goto(x, y)
    goods.append(good)
    
    
    
# bads
bads = []

for _ in range(10):
    bad=turtle.Turtle()
    bad.speed = random.randint(3, 5)
    bad.shape("/img/bad.gif")
    bad.color("red")
    bad.penup()
    # 1번째 문제상황(적군)
    x = random.randint(-380, 380)
    y = random.randint(300, 500)
    bad.goto(x, y)
    bads.append(bad)


# 점수
pen=turtle.Turtle()
pen.ht()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 260)
font1 = ("courier", 24, "normal")
pen.write(f"Score: {(score)} life:{(life)} high_score: {(high_score)}", align="center", font = font1)


# game이 끝났을 때
gameover=turtle.Turtle()
gameover.ht()
gameover.speed(0)
gameover.shape("square")
gameover.color("red")
gameover.penup()
gameover.goto(0, 100)
font2 = ("courier", 100, "normal")

count=turtle.Turtle()
count.ht()
count.speed(0)
count.shape("square")
count.color("red")
count.penup()
count.goto(0, -200)
font2 = ("courier", 100, "normal")


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
        # 2번째 문제상황(아군)
        good.dx=math.cos(0.025*good.ycor())
        good.dy=-1
        good.setx(good.xcor()+good.dx)
        good.sety(good.ycor()+good.dy)
        # good.sety(good.ycor() - 3)


        # 3번째 문제상황(아군)
        if good.xcor() >= 370:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            good.goto(x, y)
            
        if good.xcor() <= -370:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            good.goto(x, y)
            """
            good.setx(-370)
            good.dx=math.sin(0.025*good.ycor())
            """
            
        # 벽에 가면 제자리로
        if good.ycor() < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            good.goto(x, y)


        # player와 good들이 만났을 때 랜덤자리로 다시 떨어지게
        if good.distance(player) < 35:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            good.goto(x, y)
            winsound.PlaySound("/sound/good.wav", winsound.SND_ASYNC)
            

            # 점수
            score += 10
            # 6번째 문제상황
            if high_score < score:
               high_score = score 
            pen.clear()
            pen.write(f"Score: {(score)} life:{(life)} high_score: {(high_score)}", align="center", font = font1)

    
    # bad들 상하로 움직이게 하는 부분
    for bad in bads:
        # 2번째 문제상황(적군)
        bad.dx=math.cos(0.025*bad.ycor())
        bad.dy=-1
        bad.setx(bad.xcor()+bad.dx)
        bad.sety(bad.ycor()+bad.dy)

        # 3번째 문제상황(적군)
        if bad.xcor() >= 370:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            bad.goto(x, y)
        if bad.xcor() <= -370:
            x = random.randint(-380, 380)
            y = random.randint(300, 500)
            bad.goto(x, y)
        # 벽에 가면 제자리로
        if bad.ycor() < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)

        # player와 bad들이 만났을 때 랜덤자리로 다시 떨어지게
        if bad.distance(player) < 35:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)
            winsound.PlaySound("/sound/bad.wav", winsound.SND_ASYNC)
            if player.direction == "right":
                player.direction = "right"
                player.shape("/img/player_right_life.gif")
            else:
                player.shape("/img/player_left_life.gif")
            
            # 점수 및 생명
            life -= 1
            pen.clear()
            pen.write(f"Score: {(score)} life:{(life)} high_score: {(high_score)}", align="center", font = font1)

        # 4번째 문제상황
        if player.xcor() >= 370:
            player.direction = "left"
            player.shape("/img/player_left.gif")
        if player.xcor() <= -370:
            player.direction = "right"   
            player.shape("/img/player_right.gif")

    # 5번째 문제상황      
    if life == 0:
        
        gameover.write("GAME OVER", align="center", font = font2)
        count.write("3", align="center", font = font2)
        winsound.PlaySound("/sound/count.wav", winsound.SND_ASYNC)
        time.sleep(1)
        count.clear()
        count.write("2", align="center", font = font2)
        winsound.PlaySound("/sound/count.wav", winsound.SND_ASYNC)
        time.sleep(1)
        count.clear()
        count.write("1", align="center", font = font2)
        winsound.PlaySound("/sound/count.wav", winsound.SND_ASYNC)
        time.sleep(1)  
        count.clear()
        
        life = 3
        score = 0
        pen.clear()
        pen.write(f"Score: {(score)} life:{(life)} high_score: {(high_score)}", align="center", font = font1)

        for good in goods:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)
            
        for bad in bads:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)
        player.goto(0, -250)
        gameover.clear()


        
wn.mainloop()
