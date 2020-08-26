#07_03_temp_final.py

from guizero import *
from converters import ScaleAndOffsetConverter

c_to_f_conv = ScaleAndOffsetConverter('C', 'F', 1.8, 32)

def convert():
    c = float(degCfield.value)
    degFfield.value = str(c_to_f_conv.convert(c))

app = App(title="Temp Converter", layout="grid", width=300, height=100)
Text(app, text="degrees C", grid=[0,0])
degCfield = TextBox(app, grid=[1,0], width="fill")

Text(app, text="degrees F", grid=[0,1])
degFfield = Text(app, grid=[1,1])

button = PushButton(app, text="Convert", grid=[0,2], command=convert)

app.display()