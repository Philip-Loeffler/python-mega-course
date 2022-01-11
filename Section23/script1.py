from tkinter import * 

window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles = float(e1.value.get()) * 1.6
    t1.insert(END, miles)
# passing window lets the b1 button know to be in that window
b1=Button(window, text="Execute", command=km_to_miles)
# pack method puts widgets in window
# b1.pack()

b1.grid(row=0, column=0, rowspan=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)
 
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()