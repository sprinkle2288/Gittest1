from tkinter import*
def button_clicked():
    print("����!")

root = Tk()
button1 = Button(root)
button1 ["text"] = "������"
button1.pack()
button2 = Button(root, bg="red",
                 text="������ ����",
                 command=button_clicked)
button2.pack()
root.mainloop()