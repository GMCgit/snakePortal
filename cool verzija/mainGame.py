from tkinter import *
import random
from hi import window2
from swfws import Swfws
from pingpong import pingPong
root = Tk()
class snakeGame:
    def __init__(self, root, sI):
        self.root = root
        self.mainloop(sI)
    def mainloop(self, sI):
        self.root.destroy()
        self.root = Tk() 
        
        global score
        score+=sI
        
        # Constants
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
        
        class Snake: 
            def __init__(self, dir = "down"): 
                self.dir = dir
                self.body_size = BODY_SIZE 
                self.coordinates = [] 
                self.squares = [] 
                x = random.randint(0, (int(WIDTH / SPACE_SIZE))-1) * SPACE_SIZE 
                y = random.randint(0, (int(HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE
                for i in range(0, BODY_SIZE+score):
                    self.coordinates.append([0, 0])

                for x, y in self.coordinates:
                    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE, tag="snake")
                    self.squares.append(square)
        class Food:
            def __init__(self): 
                x = random.randint(0, int(WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
                y = random.randint(0, int(HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
                self.coordinates = [x, y] 
                canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD, tag="food") 

        class Portal:
            def __init__(self):
                global score
                self.x1 = random.randint(1, int(WIDTH / SPACE_SIZE)-2) * SPACE_SIZE 
                self.y1 = random.randint(1, int(HEIGHT / SPACE_SIZE) - 2) * SPACE_SIZE 
                self.x2 = random.randint(1, int(WIDTH / SPACE_SIZE)-2) * SPACE_SIZE 
                self.y2 = random.randint(1, int(HEIGHT / SPACE_SIZE) - 2) * SPACE_SIZE
                if random.randint(1, 100) > 5:
                    self.trans = True
                else:
                    self.trans = False
                canvas.create_rectangle(self.x1, self.y1, self.x1 + SPACE_SIZE, self.y1 + SPACE_SIZE, fill=PORTAL_IN, tag="portal")
                canvas.create_rectangle(self.x2, self.y2, self.x2 + SPACE_SIZE, self.y2 + SPACE_SIZE, fill=PORTAL_OUT, tag="portal") 
        
        def next_turn(snake, food, p): 
            global portalEx
            global score
            global snakeList
            global direction
            if portalEx == False:
                if random.randint(0, 100) > 50:
                    p = Portal()   
                    portalEx = True
            x, y = snake.coordinates[0] 
            if portalEx:
                if snake.coordinates[-1][0] == p.x1 and snake.coordinates[-1][1] == p.y1:
                    canvas.delete("portal")
                    portalEx = False
                    if p.trans:
                        newWindow = 0
                        if random.randint(0, 100) < 50:
                            newWindow = Swfws(self.root)
                        else:
                            newWindow = pingPong(self.root)
                        direction = 'down'
                        a = snakeGame(Tk(), newWindow.sI)
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
            square = canvas.create_rectangle( x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE) 
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
                self.root.after(SPEED, next_turn, snake, food, p)
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
        def game_over(): 
            canvas.delete(ALL) 
            canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")        
        #init
        
        self.root.title("Snake game") 
        label = Label(self.root, text="Points:{}".format(score), font=('consolas', 20)) 
        label.pack() 
        self.root.resizable(False, False)
        canvas = Canvas(self.root, bg=BACKGROUND, height=HEIGHT, width=WIDTH) 
        canvas.pack() 
        self.root.update() 
        window_width = self.root.winfo_width() 
        window_height = self.root.winfo_height() 
        screen_width = self.root.winfo_screenwidth() 
        screen_height = self.root.winfo_screenheight() 

        x = int((screen_width/2) - (window_width/2)) 
        y = int((screen_height/2) - (window_height/2)) 

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}") 

        self.root.bind('<Left>', lambda event: change_direction('left')) 
        self.root.bind('<Right>', lambda event: change_direction('right')) 
        self.root.bind('<Up>', lambda event: change_direction('up')) 
        self.root.bind('<Down>', lambda event: change_direction('down')) 

        if score+BODY_SIZE < 1:
            game_over()
        
        snake = Snake(direction)
        food = Food() 
        next_turn(snake, food, p) 
        self.root.mainloop() 
portalEx = False
score = 0
direction = 'down' 
p = 0
a = snakeGame(root, 0)