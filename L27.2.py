import pgzrun as pg
import random as r
import time as t

WIDTH = 600
HEIGHT = 600

satellites = []
lines = []

nextSatellite = 0
numOfSatellites = 8

startTime = 0
endTime = 0
totalTime = 0

def draw ():
    global totalTime
    screen.blit ("bg.png", (0, 0))
    sat_num = 1
    for sat in satellites:
        sat.draw ()
        screen.draw.text (str(sat_num), (sat.pos[0], sat.pos[1]+20))
        sat_num += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (255,0,0))
    
    if nextSatellite < numOfSatellites :
        totalTime = t.time() - startTime
        screen.draw.text (str(round(totalTime,2)), (15,15), fontsize = 28)
    else:
        screen.draw.text (str(round(totalTime,2)), (15,15), fontsize = 28)

def create_satellites () :
    global startTime
    for i in range (numOfSatellites) :
        sat = Actor ("satellite.png")
        sat.pos = r.randint (50, 550), r.randint(50, 550)
        satellites.append(sat)
    startTime = t.time ()

def on_mouse_down (pos) :
    global nextSatellite, lines
    if nextSatellite < numOfSatellites :
        if satellites [nextSatellite].collidepoint(pos) :
            if nextSatellite:
                lines.append((satellites[nextSatellite-1].pos, satellites[nextSatellite].pos))
            nextSatellite += 1
        else:
            lines = []
            nextSatellite = 0

def update ():
    pass

create_satellites ()

pg.go ()