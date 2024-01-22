from tkinter import*
from random import randint

class kemEl:
    def __init__(self, root):
        self.sI = 0
        self.mainloop(root)
    def mainloop(self, root):
        root.destroy()
        prozor=Tk()
        prozor.title('Kemijski elementi')
        prozor.geometry('350x300')
        prozor.config(background='cyan')
        prozor.resizable(False, False)
        variable1=IntVar()
        variable2=IntVar()
        Elementi = [("tekući kisik", "zapaljivi prah"), ("amonijev nitrat", "ulje"), ("amonijev nitrat", "TNT"),("amonijev nitrat","aluminij"),("HMX", " bizmutoksid klorat")]
        score=[0]

        radio1 = Radiobutton(prozor, variable=variable1, value=1)
        radio2 = Radiobutton(prozor, variable=variable1, value=2)
        radio3 = Radiobutton(prozor, variable=variable1, value=3)
        radio1.place(x = 50, y=50)
        radio2.place(x = 50, y=100)
        radio3.place(x = 50, y=150)

        radio4 = Radiobutton(prozor, variable=variable2, value=1)
        radio5 = Radiobutton(prozor, variable=variable2, value=2)
        radio6 = Radiobutton(prozor, variable=variable2, value=3)
        radio4.place(x = 200, y=50)
        radio5.place(x = 200, y=100)
        radio6.place(x = 200, y=150)

        def provjera():
            if variable1.get()==tocni_br[0] and variable2.get()==tocni_br[1]:
                score[0]+=1
                score_label.config(text='Broj točnih odgovora je: '+ str(score[0]))
                if score[0]<5:
                    setup()
                else:
                    prozor.destroy()
        def setup():
            rjesenje = Elementi[randint(0, len(Elementi)-1)]
            a=randint(0,2)
            b=randint(0,2)
            A = stupacA[a]
            B = stupacB[b]
            tocni_br[0] = a+1
            tocni_br[1] = b+1
            A.config(text=str(rjesenje[0]))
            B.config(text=str(rjesenje[1]))

            c=[0,1,2]
            c.remove(a)
            d=[0,1,2]
            d.remove(b)

            Elementi2=[]
            for i in Elementi:
                if i[0]  != rjesenje[0] and i[1] != rjesenje[1]:
                    Elementi2.append(i)
            e=randint(0,len(Elementi2)-1)
            f_l=[]
            for i in range (len(Elementi2)):
                f_l.append(i)
            f_l.remove(e)
            f=f_l[randint(0,len(f_l)-1)]
            e=Elementi2[e]
            f=Elementi2[f]

            C=stupacA[c[0]]
            C.config(text=e[0])
            C=stupacA[c[1]]
            C.config(text=e[1])

            D=stupacB[d[0]]
            D.config(text=f[0])
            D=stupacB[d[1]]
            D.config(text=f[1])

        stupacA = [radio1, radio2, radio3]
        stupacB = [radio4, radio5, radio6]
        tocni_br=[0,0]
        gumb = Button(prozor, text = "unos", command = provjera)
        setup()
        gumb.place(x = 125, y = 200)
        score_label = Label(prozor, text='Broj točnih odgovora je: '+ str(score[0]))
        score_label.place(x = 75, y=250)
        prozor.update()
        
        prozor.mainloop()
        self.sI = score[0]
a=kemEl(Tk())