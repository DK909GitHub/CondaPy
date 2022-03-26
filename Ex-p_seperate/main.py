#Libs
from appJar import gui
from CondaPy.CondaPy import enc
from pyperclip import copy
#programs
def press(button):
    if button == "EXIT":
        app.stop()
    if button == "Submit":
        app.setLabel("x",str(enc(app.getEntry("Encrypt"),199)))
        copy(app.getLabel("x"))
def b_exit():
    app.setSticky("ne")
    app.setExpand("both")
    app.addButton("EXIT",press)
def b_title():
    app.setSticky("nn")
    app.addImage("Python","images/Product-Python.png",0,)
    app.addLabel("x","This is where encrypted text will go")
def b_Encrypt():
    app.addLabelEntry("Encrypt")
    app.addButton("Submit",press)
#App Start up
with gui("App","1920x1080") as app:
    #setup
    app.setBg("#222626")
    app.setFont(size=16)
    app.setButtonFont(size=14)
    app.setFg("White",override=False)
    app.setFullscreen()
    #buttons
    b_exit()
    b_title()
    b_Encrypt()


#starts Gui
app.go()