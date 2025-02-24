import pgzrun as pg
import random as r

WIDTH = 600
HEIGHT = 600

itemCount = 1

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

item = [plasticBag, waterBottle, chips, battery, paperBag]

def draw ():
    paperBag.draw ()
    plasticBag.draw ()
    waterBottle.draw ()
    chips.draw ()
    battery.draw ()
    screen.clear ()
    screen.blit ("bg.png", (-300, -75))
    screen.draw.text ("click the paper bag to begin")
    itemDraw ()

def itemDraw ():
    cart = []
    for x in range (0, itemCount, 1):
        cart.append (item[r.randint(0,3)])
    if paperBag not in cart:
        cart [r.randint(0,itemCount-1)] = paperBag
    i = 250 - itemCount / 2 * 100
    for x in cart:
        i += 100
        x.pos = (i, 100)
        x.draw ()


pg.go ()

#item[r.randint(0,4)].draw ()