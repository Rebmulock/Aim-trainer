import tkinter as tk
import random as rd

cnv = tk.Canvas(height = 1000, width = 1000)
cnv.pack()

x = rd.randint(40,960)
y = rd.randint(80,960)
points = 0

score = tk.Label(text = points, font = ('Helvetica', 20))
score.place(x = 500, y = 40)

def emoji():
    global emote
    emote = cnv.create_oval(x - 40, y - 40, x + 40, y + 40, width = 5, fill = 'yellow')

def Delete():
    cnv.delete(emote)

def animate():
    global score
    t = 0

    score.config(text = points)
    
    for i in range(2):
        cnv.after(t, emoji)
        cnv.after(t + 200, Delete)
        t += 300

def end():
    cnv.quit()

def pos(event):
    global x, y, points

    a = event.x
    b = event.y
    x_pos = (x - a)**2
    y_pos = (y - b)**2

    if points >= 9 or points <= -9:
        if points == 9:
            points += 1
            score.config(text = points)
            points += 1

        if points == -9:
            points -= 1
            score.config(text = points)
            points -= 1

        cnv.unbind_all('<Button-1>')

        if points > 10 or points < -10:
            cnv.after(200, cnv.destroy())

    else:
        if x_pos + y_pos <= 40**2:
            points += 1

        else:
            points -= 1

        animate()

    x = rd.randint(40,960)
    y = rd.randint(160,960)

animate()

cnv.bind('<Button-1>', pos)

cnv.mainloop()