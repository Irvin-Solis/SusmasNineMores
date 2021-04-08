from tkinter import Tk, Label, PhotoImage

import numpy as np
import time
import os


app = Tk()
app.title("Nine Mens Morris")
app.geometry("625x650")

#coin flip
frames = [PhotoImage(file='/Users/Irvin Daniel/Desktop/coin_flip.gif',format = 'gif -index %i' %(i)) for i in range(52)]

probability = .50

def coin_flip(p):
    result = np.random.binomial(1,p)
    return "Heads" if result else "Tails" # if 1 heads, else tails

def update(ind):
    frame = frames[ind]
    ind += 1
    print(ind)
    if ind > 51:
        r = coin_flip(probability)
        result = Label(app, text=r, font=("Arial", 50))
        result.place(x=240, y=420)
        return
    label.configure(image=frame)
    app.after(50, update, ind)


label = Label(app)
label.pack()
app.after(0, update, 0)  


app.mainloop()

#class Board:
#    def __init__(self, app):

#        background = PhotoImage(file = "/Users/Irvin Daniel/Desktop/chovynz-Nine-Men-s-Morris.png")

#        turn = Label(app, text="Your Turn!", font=("Arial", 25))
#        turn.place(x = 1, y = 1)

#        board = Label(app, image = background)
#        board.place(x = 10, y = 45)

#        frame1 = Frame(app)
#        frame1.pack(pady = 20 )

#        app.mainloop()

# class coinflip:
#     def _init(self):
        
#         frames = [photoimage(file='/users/irvin daniel/desktop/coin_flip.gif',format = 'gif -index %i' %(i)) for i in range(52)]
        
#         probability = .5
        
#         def coin_flip(p):
#             result = np.random.binomial(1,p)
#             return "heads" if result else "tails" # if 1 heads, else tails
        
#         def update(ind):
#             frame = frames[ind]
#             ind += 1
#             print(ind)
#             if ind > 51:
#                 r = coin_flip(probability)
#                 result = label(app, text=r, font=("arial", 25))
#                 result.place(x=265, y=210)
#                 return
#             label.configure(image=frame)
#             app.after(50, update, ind)
        
#         label = label(app)
#         label.pack()
#         app.after(0, update, 0)

        