from tkinter import *
import config

def guiInit():
    global root
    root = Tk()
    root.title('Wallet')
    root.geometry("600x400")
    guiViewBudget()
    root.mainloop()

def guiViewBudget():
    frameTitle = Frame(root)

    Label(root,
          text='Budżet',
          font=('Helvetica', 30),
          bd=0,
          bg='#32a852').pack(padx=0, pady=0)
    frameTitle.pack(side=TOP, fill=X)

    frameCategories = Frame(root)
    for index, item in enumerate(config.categoryNames):
        Label(root,
              text=item[0],
              font=('Helvetica', 10),
              bd=0,
              bg='#32a852').pack(padx=0, pady=0, side=LEFT)
    frameCategories.pack(side=TOP, fill=X)