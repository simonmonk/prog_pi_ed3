#07_05_drawing.py

from guizero import *

app = App(width=400, height=200)
drawing = Drawing(app, width="fill", height="fill")
drawing.rectangle(20, 20, 300, 100, color="blue")
drawing.oval(30, 50, 290, 190, color='#ff2277')
drawing.line(0, 0, 400, 200, color='black', width=5)
drawing.text(20, 100, "Hello World", color="green", font="Times", size=48)
app.display()
