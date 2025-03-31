import pgzrun as pg

TITLE = "Quiz"

WIDTH = 800
HEIGHT = 600

marqueeBox = Rect (10, 10, 780, 100)
timerBox = Rect (690, 120, 100, 100)
questionBox = Rect (10, 120, 670, 100)
answerBox1 = Rect (10, 230, 330, 175)
answerBox2 = Rect (350, 230, 330, 175)
answerBox3 = Rect (10, 415, 330, 175)
answerBox4 = Rect (350, 415, 330, 175)
skipBox = Rect (690, 230, 100, 360)

questionNum = 0
questionCount = 0
time = 15
correct = 0

isGameOver = False

questions = []
answerBoxes = [answerBox1, answerBox2, answerBox3, answerBox4]

def draw ():
    marqueeTxt = "Welcome to quiz master!"
    screen.fill ("black")
    screen.draw.filled_rect (marqueeBox, "white")
    screen.draw.filled_rect (timerBox, "purple")
    screen.draw.filled_rect (questionBox, "blue")
    screen.draw.filled_rect (answerBox1, "light blue")
    screen.draw.filled_rect (answerBox2, "light blue")
    screen.draw.filled_rect (answerBox3, "light blue")
    screen.draw.filled_rect (answerBox4, "light blue")
    screen.draw.filled_rect (skipBox, "red")
    screen.draw.textbox (marqueeTxt, marqueeBox, color = "black")
    screen.draw.textbox (question[0].strip(), questionBox, color = "white")
    screen.draw.textbox (str(time), timerBox)
    screen.draw.textbox ("skip", skipBox, color = "dark red", angle = 270)
    index = 1
    for answerBox in answerBoxes:
        screen.draw.textbox (question[index].strip(), answerBox, color = "black")
        index += 1

def gameOver ():
    global question, time, isGameOver
    question = [f"Game over! You got {correct} questions correctly", "", "", "", "", 5]
    time = 15
    isGameOver = True

def marquee ():
    marqueeBox.x -= 2
    if marqueeBox.right < 0:
        marqueeBox.left = 800

def readFile ():
    global questions, questionCount
    file = open ("Quiz.txt", "r")
    for qst in file:
        questions.append (qst)
        questionCount += 1
    file.close ()

def nextQst ():
    global questionNum
    questionNum += 1
    return questions.pop (0).split (",")

def timer ():
    global time
    global gameOver
    time -= 1
    if time == 0:
        gameOver = True
    clock.schedule (timer, 1)

def on_mouse_down (pos):
    global time, question
    index = 1
    for box in answerBoxes:
        if box.collidepoint (pos):
            print (int(question[5]))
            print (index)
            if index == int(question[5]):
                question = nextQst ()
                time = 15
            else:
                gameOver ()
            index += 1
    if skipBox.collidepoint (pos):
        skip ()

def CorrectAnswer ():
    global correct, question, time, questions
    correct += 1
    if questions:
        question = nextQst ()
        time = 15
    else:
        gameOver ()

def skip ():
    global question, time, questions
    if questions and not(isGameOver):
        question = nextQst ()
        time = 15
    else:
        gameOver ()

def update ():
    marquee ()

readFile ()
question = nextQst ()

clock.schedule (timer, 1)

pg.go ()