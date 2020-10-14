from tkinter import *
root = Tk()
root.geometry("1480x1400")

def add_button():
    print("q")
# Creating button 
b1 = Button(root, text = "Print now", fg = "red", command = add_button)
b1.pack(side =LEFT , anchor = "nw")


root.mainloop()
