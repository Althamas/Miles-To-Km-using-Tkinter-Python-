from tkinter import *

tk = Tk()
tk.title("KM to Miles")
tk.minsize(height=30, width=50)
tk.config(padx=100, pady=100)

entry_1 = Entry()
entry_1.focus()
entry_1.grid(column=2, row=2)

label_1 = Label(text="Miles")
label_1.grid(column=3, row=2)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=3)

entry_2 = Entry()
entry_2.grid(column=2, row=3)

label_3 = Label(text="KM")
label_3.grid(column=3, row=3)


def convert():
    entry_2.delete(0, 50)
    m = int(entry_1.get())
    km = str(m * 1.60934)
    entry_2.insert(2, km)


button_1 = Button(text="Convert", command=convert)
button_1.grid(column=2, row=4)

tk.mainloop()
