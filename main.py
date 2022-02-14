# tkinter is useful for building GUIs in Python

import tkinter

window = tkinter.Tk()
window.title("FeetMeter")
window.minsize(width=500, height=300)


def button0_clicked():
    user_input = int(input.get())
    meters = float(user_input  / 3.281)
    prompt.config(text=f"{user_input} feet is {meters:.3f} meters")


def revert():
    prompt.config(text="How many feet do you have?")


# Label
label = tkinter.Label(text="Converter: Feet to Meters", font=("Arial", 24, "italic"))
label.grid(column=0, row=0)  # automatically centers component on the screen

prompt = tkinter.Label(text="How many feet do you have?", font=("Arial, 15"))
prompt.config(pady=25)
prompt.grid(column=0, row=1)

# Button
button0 = tkinter.Button(text="Calculate!", command=button0_clicked)
button0.grid(column=1, row=2)

button1 = tkinter.Button(text="Revert", command=revert)
button1.grid(column=2, row=2)

# Entry
input = tkinter.Entry(width=20)
input.grid(column=0, row=2)

window.mainloop()  # always appears at the end of the program
