#07_04_kitchen_sink.py

from guizero import *

app = App(title="Kitchen Sink", layout="grid", width=400, height=400)

# Row 0
Text(app, text="Label", grid=[0,0])
TextBox(app, grid=[1,0])
PushButton(app, text="Button", grid=[2,0])

# Row 1
CheckBox(app, text="Checkbox", grid=[0,1])
ListBox(app, items=["red", "green", "blue"], grid=[1,1])
Combo(app, options=["red", "green", "blue"], grid=[2,1])

# Row 2
ButtonGroup(app, options=["portrait", "landscape"], selected="portrait", grid=[0,2])
Slider(app, start=0, end=10, grid=[1,2])
Picture(app, image="prog_pi_ed3/test.png", width=100, height=100, grid=[2,2])

app.display()