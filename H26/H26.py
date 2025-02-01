import pgzrun as pg
import random as r

WIDTH = 600
HEIGTH = 600

score = 0
strawberriesPS = 0
goldenPlants = False
goldenHarvest = False
plants = 0

goldbg = Actor ("goldbg.jpeg")
goldbg.pos = (1000, 1000)

strawberry = Actor ("strawberry.png")
strawberry.pos = (300, 250)

strawberryPlant = Actor ("plant.png")
strawberryPlant.pos = (50, 50)

goldenStrawberry = Actor ("gold.png")
goldenStrawberry.pos = (50, 550)

def draw ():
    global score
    global strawberriesPS
    global goldenPlants
    global goldenHarvest
    global plants
    screen.blit ("bg.jpeg", (0, 0))
    goldbg.draw ()
    strawberry.draw ()
    strawberryPlant.draw ()
    goldenStrawberry.draw ()
    screen.draw.text ("$" + str(score), midtop = (300, 400))
    if goldenHarvest:
        text = "strawberries/s: " + str(strawberriesPS) + " x2 (" + str(strawberriesPS*2) + ")"
    else:
        text = "strawberries/s: " + str(strawberriesPS)
    screen.draw.text (str(text), midtop = (300, 450))
    screen.draw.text ("Strawberry plant | 1/s | $10 | owned: " + str(plants), midtop = (300, 50))
    screen.draw.text ("Golden strawberry | 2x/s | $100 | owned: " + str(goldenPlants), midtop = (300, 550))

def on_mouse_down (pos):
    global score
    global strawberriesPS
    global goldenPlants
    global plants
    if strawberry.collidepoint (pos):
        score += 1
    if strawberryPlant.collidepoint (pos):
        if score >= 10:
            score -= 10
            strawberriesPS += 1
            plants += 1
    if goldenStrawberry.collidepoint (pos):
        if score >= 100:
            score -= 100
            goldenPlants = True
            clock.schedule (goldHarvestFarm, 5)

def updatePerSec ():
    global score
    global strawberriesPS
    global goldenHarvest
    if goldenHarvest:
        score += strawberriesPS * 2
    else:
        score += strawberriesPS
    clock.schedule (updatePerSec, 1)

clock.schedule (updatePerSec, 1)

def goldHarvestFarm ():
    global goldenHarvest
    if goldenHarvest == False:
        goldenHarvest = True
        goldbg.pos = (300, 300)
        clock.schedule (goldHarvestFarm, r.randint (3, 7))
    else:
        goldenHarvest = False
        goldbg.pos = (1000, 1000)
        clock.schedule (goldHarvestFarm, r.randint (8, 16))

pg.go ()