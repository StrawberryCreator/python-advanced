import pgzrun as pg
import random as r

WIDTH = 500
HEIGHT = 500

score = 0
time = 0
gameOver = False

pikachu = Actor ("pikachu.png")
pikachu.pos = (450, 250)

ash = Actor ("ash.png")
ash.pos = (50, 250)

def time1 ():
    global time
    global gameOver
    time += 1
    if time == 20:
        gameOver = True
    else:
        clock.schedule (time1, 1)

clock.schedule (time1, 1)

def draw ():
    global time
    global score
    screen.blit ("bg.jpeg", (0, 0))
    pikachu.draw ()
    ash.draw ()
    screen.draw.text ("score: " + str(score), topleft = (0, 0))
    screen.draw.text ("time left : " + str(20 - time), topright = (500, 0))
    if gameOver:
        screen.fill ("black")
        screen.draw.text ("GAME OVER score: " + str(score), midtop = (250, 250))

def update ():
    global score
    if keyboard.left:
        ash.x -= 5
    elif keyboard.right:
        ash.x += 5
    elif keyboard.up:
        ash.y -= 5
    elif keyboard.down:
        ash.y += 5
    if ash.colliderect (pikachu):
        pikachu.pos = (r.randint(50, 450), r.randint(50, 450))
        score += 1

pg.go ()