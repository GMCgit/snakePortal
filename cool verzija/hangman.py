from tkinter import *
from random import randint

class Hangman:
    def __init__(self, root):
        self.root = root
        self.sI = 0
        self.mainloop(root)
    def mainloop(self, root):
        root.destroy()
        root = Tk()
        root.geometry("400x600+100+100")
        words =[("kompjuter", "kompjuter je zao", "kompjuter je uzasno zao"),
                ("covjek","covjek nije stvoren za poraze","ali covjek nije stvoren za poraze covjek moze biti unisten ali ne i pobjeden"),
                ("istina","samo ce istina ostati","sve ce proci samo ce istina ostati"),
                ("cilj","priblizavamo cilju","problemi se povecavaju sto se blize priblizavamo cilju"),
                ("rizik","rizik je donositi odluke","rizik je donositi odluke u nesigurnom okruzenju ne donositi ih takoder je rizik"),
                ("vrijeme","sve u svoje vrijeme"),
                ("dobro","tko cini dobro","tko cini dobro od njega se jos vise dobra ocekuje"),
                ("ljubav","ljubav je ozbiljna mentalna bolest"),
                ("sutjeti","ljudi koji umiju sutjeti","dobro i korisno znaju govoriti ljudi koji umiju sutjeti"),
                ("svanuce","dok god ima mraka ima i svanuca"),
                ("bijes","cuvaj se bijesa strpljiva covjeka")]
        stats = {
            "curr": "",
            "ans": [],
            "health": 100,
            "gravity": 10,
            "level": 0,
            "index": 0
        }
        stats["index"]=randint(0, len(words)-1)
        ansLabel = Label(root, font = ("Comic Sans MS", 18), wraplength = 300)
        ansLabel.place(x = 50, y = 300)
        scoreLabel = Label(root, font = ("Comic Sans MS", 18), text="Score: 0")
        scoreLabel.place(x = 150, y = 50)
        healthLabel = Label(root, font=("Comic Sans MS", 18), text="Health: 100")
        healthLabel.place(x=150, y=100)
        gravityLabel = Label(root, font=("Comic Sans MS", 18), text="Gravity: 10")
        gravityLabel.place(x=150, y=150)
        def setup():
            stats["ans"] = []
            temp = words[stats["index"]][stats["level"]]
            stats["curr"] = temp
            for i in temp:
                if i == " ":
                    stats["ans"].append(" ")
                else:
                    stats["ans"].append("_")
            ansLabel.config(text = " ".join(stats["ans"]))

        def enterKey(e):
            key = e.keysym
            found = False
            for i in range(len(stats["curr"])):
                if stats["curr"][i] == key:
                    stats["ans"][i] = key
                    found = True
            if not found:
                stats["health"]-=abs(stats["gravity"])
                if stats["health"] < 1:
                    root.destroy()
                stats["gravity"]+=1
            ansLabel.config(text=" ".join(stats["ans"]))
            if "".join(stats["ans"]) == stats["curr"]:
                self.sI += 1
                stats["level"]+=1
                if stats["level"] > len(words[stats["index"]])-1:
                    root.destroy()
                stats["gravity"] -= 5
                setup()
            scoreLabel.config(text = "Score: " +str(self.sI))
            healthLabel.config(text = "Health: "+str(stats["health"]))
            gravityLabel.config(text= "Gravity: "+str(stats["gravity"]))
        root.bind("<KeyPress>", lambda e: enterKey(e))

        setup()
        root.mainloop()
        print(self.sI)

#a = Hangman(Tk())