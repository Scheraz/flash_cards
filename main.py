from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

#--------------------------- Read CSV-----------------------#
try:
    d = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn = d.to_dict(orient="records")
current_card = random.choice(to_learn)

#--------------------------- Generate Random Word -----------#

def card_flip():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def next_card():
    global window_timer, current_card
    window.after_cancel(window_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill= "black")
    canvas.itemconfig(card_text, text = current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    window_timer = window.after(3000, card_flip)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window_timer = window.after(3000, card_flip)





#--------------------------- UI Components ------------------#

canvas = Canvas(width=800, height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel",30, "italic"))
card_text = canvas.create_text(400, 270, text="", font=("Ariel",35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
next_card()
#--------------------------- Buttons -----------------------#

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong,command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()

