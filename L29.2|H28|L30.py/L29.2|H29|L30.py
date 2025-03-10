import pgzrun as pg
import random as r

WIDTH = 600
HEIGHT = 600

itemCount = 1
generate = True
lose = False
win = False
speed = 1
y = 50
first = True

paperBag = Actor("paperbag.png")
paperBag.pos = (300, 300)

plasticBag = Actor("plasticbag.png")
plasticBag.pos = (300, 300)

waterBottle = Actor("waterbottle.png")
waterBottle.pos = (300, 300)

chips = Actor("chips.png")
chips.pos = (300, 300)

battery = Actor("battery.png")
battery.pos = (300, 300)

item = [plasticBag, waterBottle, chips, battery]
cart = []

def draw ():
    global generate
    global win
    global lose
    screen.clear ()
    if win:
        screen.blit ("reduc.png", (0, 0))
        screen.draw.text ("you win", fontsize = 100, color = "dark green", midtop = (300, 100))
    elif lose:
        screen.blit ("reduc.png", (0, 0))
        screen.draw.text ("you lose", fontsize = 100, color = "red", midtop = (300, 100))
    else:
        screen.blit ("bg.png", (-315, -90))
        if itemCount == 1:
            screen.draw.text ("click the paper bag to begin", fontsize = 50, color = "black", midtop = (300, 275))
        itemDraw ()
        generate = False

def itemDraw ():
    global cart
    global speed
    global lose
    global generate
    global y
    global first
    if generate:
        cart = []
        for x in range (0, itemCount, 1):
            cart.append (item[r.randint(0,3)])
        if paperBag not in cart:
            cart [r.randint(0,itemCount-1)] = paperBag
    i = 255 - itemCount / 2 * 75
    if not(first):
        for x in cart:
            if generate:
                y = 50
            i += 75
            x.pos = (i, y)
            x.draw ()
        if y >= 550:
            lose = True
        y += speed
    else:
        for x in cart:
            i += 75
            x.pos = (i, 100)
            x.draw ()

def speedUp ():
    global speed
    speed += 0.075
    clock.schedule (speedUp, 0.1)

def on_mouse_down (pos):
    global itemCount
    global generate
    global win
    global lose
    global first
    if paperBag.collidepoint (pos):
        if itemCount == 8:
            win = True
        else:
            itemCount += 1
        generate = True
        if first:
            first = False
            clock.schedule (speedUp, 0.1)
    else:
        for x in item:
            collide = False
            if x.collidepoint (pos):
                lose = True
                collide = True
            if not(collide):
                lose = True

def update ():
    pass

pg.go ()