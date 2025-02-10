import pgzrun as pg
import random as r

WIDTH = 600
HEIGHT = 600

satellites = []
satellite1 = ""
satellite2 = ""

def create_satellites ():
    for sat in range (0, 8, 1):
        sat = Actor ("satellite.png")
        sat.pos = (r.randint (50, 550), r.randint (50, 550))
        satellites.append (sat)

def draw ():
    screen.blit ("bg.png", (0, 0))
    sate_num = 1
    for sate in satellites:
        sate.draw ()
        screen.draw.text (str(sate_num), (sate.pos[0], sate.pos[1]+20))
        sate_num += 1

create_satellites ()

def on_mouse_click (pos):
    global satellite1
    global satellite2
    global satellites
    for satel in satellites:
        if satel.collidepoint(pos):
            print ("test")
            if satellite1 == "":
                satellite1 = satel
                print (satellite1)

pg.go ()