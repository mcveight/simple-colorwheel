from tkinter import *
from wheel import wheel as guiWheel


root = Tk()
root.title("swc 0.01b")

# hexadecimal colour box
hexbox = Entry(root, width=8, bg="white", fg="black")
hexbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
hexbox.insert(0,"#00000")



root.mainloop()

