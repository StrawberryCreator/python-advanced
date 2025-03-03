import pgzrun as pg
import random as r

WIDTH = 600
HEIGHT = 600

itemCount = 1
generate = True
lose = False
win = False

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
        if generate:
            itemDraw ()
            generate = False


def itemDraw ():
    cart = []
    for x in range (0, itemCount, 1):
        cart.append (item[r.randint(0,3)])
    if paperBag not in cart:
        cart [r.randint(0,itemCount-1)] = paperBag
    i = 255 - itemCount / 2 * 75
    for x in cart:
        i += 75
        x.pos = (i, 100)
        x.draw ()

def on_mouse_down (pos):
    global itemCount
    global generate
    global win
    global lose
    if paperBag.collidepoint (pos):
        if itemCount == 8:
            win = True
        else:
            itemCount += 1
        generate = True
    else:
        for x in item:
            collide = False
            if x.collidepoint (pos):
                lose = True
                collide = True
            if not(collide):
                lose = True

pg.go ()