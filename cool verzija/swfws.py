from tkinter import *
from random import randint
class Swfws:
    def __init__(self, root):
        self.root = root
        self.sI = 0
        self.mainLoop(self.root)
    def mainLoop(self, root):
        root.destroy()
        root = Tk()
        root.resizable(False, False)
        WIDTH = 500
        HEIGHT = 500
        SPEED = 200
        SPACE_SIZE = 20
        BACKGROUND = "#FFFFFF"
        MIN_LENGHT = 3
        PLAYER = "#FF0000"

        root.title("Slightly wrong facts with Stamac") 
        canvas = Canvas(root, bg=BACKGROUND, height=100, width=WIDTH) 
        canvas.place(x = 0, y = 0) 
        root.update() 
        window_width = root.winfo_width() 
        window_height = root.winfo_height() 
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = int((screen_width/2) - (window_width/2)) 
        y = int((screen_height/2) - (window_height/2))
        root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}") 

        recenice = {
            3: [("trokut je tijelo", 2)],
            4: [("merkur je najtopliji planet", 0)],
        }
        stats = {
            "level": 0,
            "pos": 0,
            "cor": 0,
            "words": [],
            "player": canvas.create_rectangle(WIDTH/6-15, 50, WIDTH/6+15, 100, fill=PLAYER)
        }
        def gameSetUp():
            swFact = recenice[stats["level"]+MIN_LENGHT][randint(0, len(recenice[stats["level"]+MIN_LENGHT])-1)]
            s = swFact[0].split()
            stats["cor"] = swFact[1]
            for i in range(len(s)):
                a = Label(root, bg=["#E1EFCA", "#ECCAFF", "#A99ABD", "#E5D0E3", "#E0E3F4", "#C0D8C0"][randint(0, 5)], text = s[i], height=3, width = int(WIDTH/(6*len(s)))-7+len(s), border = 2)
                a.place(x = WIDTH/len(s)*i, y = 100)
                stats["words"].append(a)
            if stats["level"] < len(recenice)-1:
                swFact2 = recenice[stats["level"]+MIN_LENGHT+1][randint(0, len(recenice[stats["level"]+MIN_LENGHT+1])-1)]
                s = swFact2[0].split()
                for i in range(len(s)):
                    a = Label(root, bg=["#E1EFCA", "#ECCAFF", "#A99ABD", "#E5D0E3", "#E0E3F4", "#C0D8C0"][randint(0, 5)], text = s[i], height=3, width = int(WIDTH/(6*len(s)))-7+len(s), border = 2)
                    a.place(x = WIDTH/len(s)*i, y = 300)
                    stats["words"].append(a)
        def move(dir):
            if dir == "left":
                stats["pos"] = max(0, stats["pos"]-1)
            elif dir == "right":
                stats["pos"] = min(stats["level"]+MIN_LENGHT-1, stats["pos"]+1)
            else:
                if stats["pos"] == stats["cor"]:
                    stats["level"]+=1
                    self.sI += 1
                    if stats["level"] > len(recenice)-1:
                        root.destroy()
                    for i in stats["words"]:
                        i.destroy()
                    stats["words"] = []
                    gameSetUp()
                else:
                    self.sI -= 1
            canvas.delete(stats["player"])
            stats["player"] = canvas.create_rectangle(WIDTH/6+WIDTH/3*stats["pos"]-15, 50, WIDTH/6+WIDTH/3*stats["pos"]+15, 100, fill=PLAYER)
        gameSetUp()
        root.bind('<Left>', lambda event: move('left')) 
        root.bind('<Right>', lambda event: move('right'))
        root.bind('<Down>', lambda event: move('down'))
        root.mainloop()
#a = Swfws(Tk())