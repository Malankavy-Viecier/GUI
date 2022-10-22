from tkinter import*

def setwindow(root):
    root.title("PROGRAM WINDOW")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

def handlerButton(event=False):
    global en1
    global en2
    global result
    if event:
        print(event)
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text="Sum: " + r)
    except ValueError:
        if not en1.get() or not en2.get():
            result.config(text="You did not enter anything!")
        else:
            result.config(text="Enter a number! That was not a number!")

root = Tk()
setwindow(root)

header = Label(root, text="Sum", font="Tahoma 20")
en1 = Entry(root, font="Tahoma 20")
en2 = Entry(root, font="Tahoma 20")

button = Button(root, text="Sum", font="Tahoma 20", command=handlerButton)
result = Label(root, font="Tahoma 20")

en1.bind("<Return>", handlerButton)
en2.bind("<Return>", handlerButton)

header.place(relx=0.5, rely=0.01, anchor="n")
en1.place(relx=0.5, rely=0.1, anchor="n")
en2.place(relx=0.5, rely=0.2, anchor="n")
button.place(relx=0.5, rely=0.3, anchor="n")
result.place(relx=0.5, rely=0.4, anchor="n")

root.mainloop()