from tkinter import *

root = Tk()

# hexadecimal colour box
hexbox = Entry(root, width=20, bg="white", fg="black")
hexbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
hexbox.insert(0,"#00000")

hexbox.pack()


root.mainloop()

