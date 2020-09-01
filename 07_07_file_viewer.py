#07_07_file_viewer

from guizero import *

def ask():
    filename = select_file(title="Choose a text file", filetypes=[["*.md", "*.txt"]])
    if not filename:
        print("No file selected")
    else:
        read_file(filename)

def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close()	
    text_area.value = text

app = App(width=600, height=200)
text_area = TextBox(app, width="fill", height=10, multiline=True, scrollbar=True)
button = PushButton(app, text="Open", command=ask)
app.display()