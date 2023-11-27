
# Program in Python to create a Snake Game 
  
from tkinter import *
import random 
  
# Initialising Dimensions of Game 
WIDTH = 500
HEIGHT = 500
SPEED = 200
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF"
BACKGROUND = "#000000"
PORTAL_IN = "#FF0000"
PORTAL_OUT = "#0000FF"
SNAKE_FAKE = "#00BB00"
  
# Class to design the snake 
class Snake: 
  
    def __init__(self, realS, dir): 
        self.realS = realS
        self.dir = dir
        self.body_size = BODY_SIZE 
        self.coordinates = [] 
        self.squares = [] 
        x = random.randint(0,  
                   (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
        y = random.randint(0,  
           (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        for i in range(0, BODY_SIZE):
            if realS:
                self.coordinates.append([0, 0])
            else:
                self.coordinates.append([x,y])
  
        for x, y in self.coordinates:
            if realS:
                square = canvas.create_rectangle( 
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE,  
                          fill=SNAKE, tag="snake")
            else:
                square = canvas.create_rectangle( 
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE,  
                          fill=SNAKE_FAKE, tag="snake")
            self.squares.append(square)
  
# Class to design the food 
class Food: 
  
    def __init__(self): 
  
        x = random.randint(0,  
                   (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
        y = random.randint(0,  
                   (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
  
        self.coordinates = [x, y] 
  
        canvas.create_oval(x, y, x + SPACE_SIZE, y +
                           SPACE_SIZE, fill=FOOD, tag="food") 

class Portal:
    def __init__(self):
        global score
        self.x1 = random.randint(0,  
                   (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
        self.y1 = random.randint(0,  
                   (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
        self.x2 = random.randint(0,  
                   (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
        self.y2 = random.randint(0,  
                   (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
        self.timeWarp = random.randint(1, 2*(score+1))-score
        canvas.create_rectangle( 
                self.x1, self.y1, self.x1 + SPACE_SIZE, self.y1 + SPACE_SIZE,  
                      fill=PORTAL_IN, tag="portal")
        canvas.create_rectangle( 
                self.x2, self.y2, self.x2 + SPACE_SIZE, self.y2 + SPACE_SIZE,  
                      fill=PORTAL_OUT, tag="portal") 
portalEx = False
# Function to check the next move of snake

def move():
    global snakeList
    j = 0
    while j < len(snakeList):
        i = snakeList[j]
        x, y = i.coordinates[0]
        if i.dir == "up": 
            y -= SPACE_SIZE 
        elif i.dir == "down": 
            y += SPACE_SIZE 
        elif i.dir == "left": 
            x -= SPACE_SIZE 
        elif i.dir == "right": 
            x += SPACE_SIZE
        
        i.coordinates.insert(0, (x, y)) 
        square = canvas.create_rectangle( 
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_FAKE) 
        i.squares.insert(0, square)
        
        del i.coordinates[-1] 
        canvas.delete(i.squares[-1]) 
        del i.squares[-1] 
        
        if check_collisions(i):
            snakeList.pop(j)
            j-=1
        j+=1

def next_turn(snake, food, p): 
    global portalEx
    global score
    global snakeList
    move()
    if portalEx == False:
        if random.randint(0, 100) > 50:
            p = Portal()   
            portalEx = True

    x, y = snake.coordinates[0] 
    if portalEx:
        if snake.coordinates[-1][0] == p.x1 and snake.coordinates[-1][1] == p.y1:
            canvas.delete("portal")
            portalEx = False
            score += p.timeWarp
            if p.timeWarp < 0:
                snakeList.append(Snake(False, ["up", "down", "left", "right"][random.randint(0, 3)]))
            label.config(text="Points:{}".format(score)) 
        if x == p.x1 and y == p.y1:
            if direction == "up": 
                y = p.y2 - SPACE_SIZE
                x = p.x2
            elif direction == "down": 
                y = p.y2 + SPACE_SIZE 
                x = p.x2
            elif direction == "left": 
                x = p.x2 - SPACE_SIZE 
                y= p.y2
            elif direction == "right": 
                x = p.x2 + SPACE_SIZE 
                y = p.y2
        else:
            if direction == "up": 
                y -= SPACE_SIZE 
            elif direction == "down": 
                y += SPACE_SIZE 
            elif direction == "left": 
                x -= SPACE_SIZE 
            elif direction == "right": 
                x += SPACE_SIZE 
    else:
        if direction == "up": 
            y -= SPACE_SIZE 
        elif direction == "down": 
            y += SPACE_SIZE 
        elif direction == "left": 
            x -= SPACE_SIZE 
        elif direction == "right": 
            x += SPACE_SIZE 
  
    snake.coordinates.insert(0, (x, y)) 
  
    square = canvas.create_rectangle( 
        x, y, x + SPACE_SIZE, 
                  y + SPACE_SIZE, fill=SNAKE) 
  
    snake.squares.insert(0, square) 
  
    if x == food.coordinates[0] and y == food.coordinates[1]: 
  
        score += 1
  
        label.config(text="Points:{}".format(score)) 
  
        canvas.delete("food") 
  
        food = Food() 

    else: 
  
        del snake.coordinates[-1] 
  
        canvas.delete(snake.squares[-1]) 
  
        del snake.squares[-1] 
    if check_collisions(snake): 
        game_over() 
  
    else: 
        window.after(SPEED, next_turn, snake, food, p)
  
# Function to control direction of snake 
def change_direction(new_direction): 
  
    global direction 
  
    if new_direction == 'left': 
        if direction != 'right': 
            direction = new_direction 
    elif new_direction == 'right': 
        if direction != 'left': 
            direction = new_direction 
    elif new_direction == 'up': 
        if direction != 'down': 
            direction = new_direction 
    elif new_direction == 'down': 
        if direction != 'up': 
            direction = new_direction 
  
# function to check snake's collision and position 
def check_collisions(snake): 
  
    x, y = snake.coordinates[0] 
  
    if x < 0 or x >= WIDTH: 
        return True
    elif y < 0 or y >= HEIGHT: 
        return True
  
    for body_part in snake.coordinates[1:]: 
        if x == body_part[0] and y == body_part[1]: 
            return True
  
    return False
  
# Function to control everything 
def game_over(): 
  
    canvas.delete(ALL) 
    canvas.create_text(canvas.winfo_width()/2,  
                       canvas.winfo_height()/2, 
                       font=('consolas', 70),  
                       text="GAME OVER", fill="red",  
                       tag="gameover") 
  
# Giving title to the gaming window 
  
  
window = Tk() 
window.title("Snake game ") 
  
  
score = 0
direction = 'down'
  
# Display of Points Scored in Game 
  
label = Label(window, text="Points:{}".format(score),  
              font=('consolas', 20)) 
label.pack() 
  
canvas = Canvas(window, bg=BACKGROUND,  
                height=HEIGHT, width=WIDTH) 
canvas.pack() 
  
window.update() 
  
window_width = window.winfo_width() 
window_height = window.winfo_height() 
screen_width = window.winfo_screenwidth() 
screen_height = window.winfo_screenheight() 
  
x = int((screen_width/2) - (window_width/2)) 
y = int((screen_height/2) - (window_height/2)) 
  
window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
  
window.bind('<Left>',  
            lambda event: change_direction('left')) 
window.bind('<Right>',  
            lambda event: change_direction('right')) 
window.bind('<Up>',  
            lambda event: change_direction('up')) 
window.bind('<Down>',  
            lambda event: change_direction('down')) 
  
snake = Snake(True, ":(") 
food = Food() 
p = 0
snakeList = [] 
next_turn(snake, food, p) 
window.mainloop() 
  
print('Hii')