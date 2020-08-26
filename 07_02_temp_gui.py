#07_02_temp_gui.py

from guizero import *

app = App(title="Temp Converter", layout="grid", width=300, height=100)
Text(app, text="degrees C", grid=[0,0])
degCfield = TextBox(app, grid=[1,0], width="fill")

Text(app, text="degrees F", grid=[0,1])
degFfield = Text(app, grid=[1,1])

button = PushButton(app, text="Convert", grid=[0,2])

app.display()