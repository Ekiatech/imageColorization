

from tkinter import *
from turtle import color
from PIL import Image, ImageTk
app = Tk()
app.geometry('400x400')

coordonatesBlue = []
color = ['red']

colors = ['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'saddle brown', 'white', 'yellow']

def get_x_y(event):
    global x, y
    x, y = event.x, event.y
    print(x, y)

def draw(event, color):
    global x, y
    print(color)
    canvas.create_line((x, y, event.x, event.y), fill=color[0])
    x, y = event.x, event.y

def viewChangeColor(color):
    canvas.itemconfig(rectangle, fill = color)

def change_color(color):
    color[0] = 'blue'
    viewChangeColor(color)

def test(event):
    canvas.itemconfig(rectangle, fill = 'purple')


canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)

rectangle = canvas.create_rectangle(100,100,200,200, fill = color)

canvas.bind("<Button-1>", get_x_y)
canvas.bind("<B1-Motion>", lambda event : draw(event, color))

buttonBlueu = Button(canvas, text = "Changer pour bleu", bg = 'black', fg = 'blue', command = lambda:change_color(color))
buttonBlueu.pack(fill = X)

def test(event, color):
    color = colors[liste.curselection()[0]]
    viewChangeColor(color)

fenetre = Tk()
 
liste = Listbox(fenetre, selectborderwidth = 5)
liste.pack()
 
for i in range(0, len(colors)):
    liste.insert(END, '')
    liste.itemconfig(i , bg = colors[i], selectbackground = colors[i])
 
liste.bind("<<ListboxSelect>>", lambda event: test(event, color))

app.mainloop()
