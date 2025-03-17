import pgzrun as pg

TITLE = "Quiz"

WIDTH = 800
HEIGHT = 600

marqueeBox = Rect (10, 10, 780, 100)
timerBox = Rect (690, 120, 100, 100)
questionBox = Rect (10, 120, 670, 100)
answerBox1 = Rect (10, 230, 385, 175)
answerBox2 = Rect (715, 85, 75, 75)
answerBox3 = Rect (10, 85, 75, 75)
answerBox4 = Rect (715, 85, 75, 75)
skipBox = Rect (715, 170, 75, 175)

def draw ():
    screen.fill ("black")
    screen.draw.filled_rect (marqueeBox, "gray")
    screen.draw.filled_rect (timerBox, "purple")
    screen.draw.filled_rect (questionBox, "blue")
    screen.draw.filled_rect (answerBox1, "light blue")
    #screen.draw.filled_rect (answerBox2, "light blue")
    #screen.draw.filled_rect (answerBox3, "light blue")
    #screen.draw.filled_rect (answerBox4, "light blue")
    #screen.draw.filled_rect (skipBox, "light blue")

pg.go ()