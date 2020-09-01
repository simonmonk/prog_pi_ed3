#07_06_yes_no.py

from guizero import *

def ask():
    if yesno("Question", "Yes or No?"):
        info("Result", "You clicked Yes")
    else:
        warn("Result", "You clicked No")

app = App()
button = PushButton(app, text="Click Me", command=ask)
app.display()