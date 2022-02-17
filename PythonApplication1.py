from tkinter import*
def button_clicked():
    print("Клац!")

root = Tk()
button1 = Button(root)
button1 ["text"] = "Печать"
button1.pack()
button2 = Button(root, bg="red",
                 text="Кликни меня",
                 command=button_clicked)
button2.pack()
root.mainloop()