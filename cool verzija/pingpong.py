from tkinter import *
from math import sin
from math import cos
import math
import time
from random import randint
class pingPong:
    def __init__(self, root):
        self.sI = 0
        self.maingame(root)
    def maingame(self, root):
        root.destroy()
        root = Tk()

        WIDTH = 800
        HEIGHT = 500
        SPEED = 5
        BACKGROUND = "#000000"
        BALL_C = "#FF0000"
        score = Label(root,font=('consolas', 20), text="0:0" )
        score.pack()
        canvas = Canvas(root, bg=BACKGROUND, height=HEIGHT, width=WIDTH) 
        canvas.pack()
        #x,y -> coords, s -> speed in pixels, a -> angle 
        ball = {
            "x": WIDTH/2,
            "y": HEIGHT/2,
            "r": 10,
            "s": 4,
            "a": randint(16, 75)
        }
        
        class Player:
            def __init__(self, x):
                self.x = x
                self.y = HEIGHT/2
                self.w = 15
                self.h = 90
                self.c = "white"
                self.s = 5
                self.p = 0
            def draw(self):
                canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill = self.c, tags="player")
            def PID(self):
                #Predict, Intense eye contact, Destroy yourself because wtf
                ball2 = ball.copy()
                while ball2["x"] < self.x-10 and (90>ball2["a"] or ball2["a"]>270):
                    ball2["x"] += int(ball2["s"]*cos(ball2["a"]*3.14/180))
                    ball2["y"] -= int(ball2["s"]*sin(ball2["a"]*3.14/180))

                    if ball2["y"]-ball2["r"] < 10 or ball2["y"]+ball2["r"] > HEIGHT-10:
                        ball2["y"] += int(ball2["s"]*sin(ball2["a"]*3.14/180))
                        ball2["a"] = 360-ball2["a"]
                    if collision(player1.x, player1.y, player1.w, player1.h, ball2["x"], ball2["y"], ball2["r"]) or ball2["x"] < 0:
                        ball["x"] -= int(ball2["s"]*cos(ball2["a"]*3.14/180))
                        ball2["a"]=180-ball["a"]
                if 90>ball2["a"] or ball2["a"]>270:
                    if self.y+self.h-10 > ball2["y"] and self.y+10 > ball2["y"]:
                        move(self, True, False)
                    elif self.y+10 < ball2["y"] and self.y+self.h-10 < ball2["y"]:
                        move(self, False, True)
                    
        def collision(rleft, rtop, width, height,
              center_x, center_y, radius):
            # Detect collision between a rectangle and circle
            rright, rbottom = rleft + width, rtop + height

            cleft, ctop     = center_x-radius, center_y-radius
            cright, cbottom = center_x+radius, center_y+radius

            if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
                return False 
            for x in (rleft, rleft+width):
                for y in (rtop, rtop+height):
                    if math.hypot(x-center_x, y-center_y) <= radius:
                        return True
            if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
                return True
            return False
        def fixBall():
            while ball["a"] < 0:
                ball["a"]+=360
            while ball["a"] > 360:
                ball["a"]-=360
        def loop():
            move(player1, upTracker.is_pressed(), downTracker.is_pressed())
            player2.PID()
            ball["x"] += int(ball["s"]*cos(ball["a"]*3.14/180))
            ball["y"] -= int(ball["s"]*sin(ball["a"]*3.14/180))
            
            if ball["y"]-ball["r"] < 10 or ball["y"]+ball["r"] > HEIGHT-10:
                ball["y"] += int(ball["s"]*sin(ball["a"]*3.14/180))
                ball["a"] = 360-ball["a"]
                fixBall()
            
            if collision(player1.x, player1.y, player1.w, player1.h, ball["x"], ball["y"], ball["r"]):
                ball["x"] -= int(ball["s"]*cos(ball["a"]*3.14/180))
                
                if upTracker.is_pressed():
                    sN = ball["s"]+2
                    ball["a"]=180-ball["a"]-randint(10, 30)
                elif downTracker.is_pressed():
                    sN = ball["s"]+2
                    ball["a"]=180-ball["a"]+randint(10,30)
                else:
                    sN = ball["s"]
                    ball["a"]=180-ball["a"]
                ball["s"] = sN
                fixBall()
            
            if collision(player2.x, player2.y, player2.w, player2.h, ball["x"], ball["y"], ball["r"]):
                ball["x"] -= int(ball["s"]*cos(ball["a"]*3.14/180))
                sN = ball["s"]
                ball["a"]=180-ball["a"]*sN/ball["s"]
                fixBall()
            
            
            canvas.delete("BALL")
            canvas.create_oval(ball["x"]-ball["r"], ball["y"]-ball["r"], ball["x"]+ball["r"], ball["y"]+ball["r"], fill=BALL_C, tags="BALL")
            
            def reset():
                score.config(text=str(player1.p)+":"+str(player2.p))
                ball["x"] = WIDTH/2
                ball["y"] = HEIGHT/2
                ball["a"] = randint(0, 75)
                ball["s"] = 5+player1.p+player2.p
                if player1.p > 5 or player2.p > 5:
                    root.destroy()
                    self.sI = abs(player1.p-player2.p)
                
            
            if ball["x"] < 10:
                player2.p+=1
                reset()
            elif ball["x"] > WIDTH-10:
                player1.p+=1
                reset()
            
            canvas.delete("player")
            player1.draw()
            player2.draw()
            
            root.after(SPEED, loop)
        
        def move(obj, up, down):
            if up:
                if obj.y - obj.s > 10:
                    obj.y -= obj.s
            if down:
                if obj.y+obj.h+obj.s < HEIGHT-10:
                    obj.y+=obj.s
        
        root.title("Ping pong") 
        root.update() 
        window_width = root.winfo_width() 
        window_height = root.winfo_height() 
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = int((screen_width/2) - (window_width)) 
        y = int((screen_height/2) - (window_height))
        #root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        root.resizable(False, False)
        
        canvas.create_rectangle(0, 0, 10, HEIGHT, fill="orange", tags="WALL")
        canvas.create_rectangle(0, 0, WIDTH, 10, fill="orange", tags="WALL")
        canvas.create_rectangle(0, HEIGHT-10, WIDTH, HEIGHT, fill="orange", tags="WALL")
        canvas.create_rectangle(WIDTH-10, 0, WIDTH, HEIGHT, fill="orange", tags="WALL")
        
        class KeyTracker():
            key = ''
            last_press_time = 0
            last_release_time = 0

            def track(self, key):
                self.key = key

            def is_pressed(self):
                return time.time() - self.last_press_time < .1

            def report_key_press(self, event):
                if event.keysym == self.key:
                    #if not self.is_pressed():
                    #    on_key_press(event)
                    self.last_press_time = time.time()
        
        player1 = Player(30)
        player2 = Player(WIDTH-50)
        player2.s = 3
        upTracker = KeyTracker()
        upTracker.track("Up")
        downTracker = KeyTracker()
        downTracker.track("Down")
        
        def keyMapper(e):
            upTracker.report_key_press(e)
            downTracker.report_key_press(e)
        
        root.bind('<KeyPress>', lambda e: keyMapper(e))
        root.bind('<KeyRelease>', lambda e: keyMapper(e))
        
        canvas.create_oval(WIDTH/2-10, HEIGHT/2-10, WIDTH/2+10, HEIGHT/2+10, fill=BALL_C, tags="BALL")
        loop()
        root.mainloop()
#a = pingPong(Tk())           