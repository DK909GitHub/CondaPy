#libs
from Libaries.appJar import gui
from Libaries.CondaPy import dec
from Libaries.CondaPy import enc
from Libaries.pyperclip import copy
#programs
def press(button):
    if button == "EXIT":
        app.stop()
    elif button == "Encrypt":
        app.setLabel("x",str(enc(app.getEntry("Input"),199)))
        copy(app.getLabel("x"))
    elif button == "Decrypt":
        app.setLabel("x",str(dec(app.getEntry("Input"),199)))
        copy(app.getLabel("x"))

def b_title():
    app.setSticky("nn")
    app.addImage("Python","Images/Product-Python.png",0,0)
    app.addLabel("x","This is where output goes.",15,0)


def b_exit():
    app.setSticky("ne")
    app.setExpand("both")
    app.addButton("EXIT",press,0,0)


def b_enc_dec():
    app.addLabelEntry("Input",16,0)
    app.setSticky("")
    app.addButton("Encrypt",press,20,0)
    app.addButton("Decrypt",press,21,0)
    


#App Start up
with gui("App","1920x1080") as app:
    #setup
    app.setBg("#222626")
    app.setFont(size=16)
    app.setButtonFont(size=14)
    app.setFg("White",override=False)
    app.setFullscreen()
    b_exit()
    b_title()
    b_enc_dec()