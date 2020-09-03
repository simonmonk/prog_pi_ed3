#07_08_file_viewer_menu.py

from guizero import *

def ask_file():
    filename = select_file(title="Choose a text file", filetypes=[["*.md", "*.txt"]])
    if not filename:
        print("No file selected")
    else:
        read_file(filename)

def save_file():
    print("not implemented")

def find():
    print("not implemented")

def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close()	
    text_area.value = text

app = App(width=600, height=200)
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["Open", ask_file], ["Save", save_file], ["Quit", app.destroy]],
                      [ ["Find", find]]
                  ])
text_area = TextBox(app, width="fill", height=10, multiline=True, scrollbar=True)
app.display()