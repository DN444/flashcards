import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
current={}
learn={}
try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/bengali_words.csv")
    learn=original_data.to_dict(orient="records")
else:
    learn=data.to_dict(orient="records")

def next_card():
    global current,flip_timer
    window.after_cancel(flip_timer)
    current=random.choice(learn)
    canvas.itemconfig(card_title,text="Bengali",fill="black")
    canvas.itemconfig(card_word,text=current["Bengali"],fill="black")
    canvas.itemconfig(card_background,image=front_card)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current["English"],fill="white")
    canvas.itemconfig(card_background,image=back_card)

def is_known():
    learn.remove(current)
    data=pd.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card=PhotoImage(file="images/card_front.png")
back_card=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_card)
card_title=canvas.create_text(400,150,font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="images/right.png") 
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)


next_card()
window.mainloop()