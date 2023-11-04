from tkinter import *
from logic import determinant
from logic import roots 

def clear_placeholder(event, widget, placeholder_text):
    if widget.get("1.0", "end-1c") == placeholder_text:
        widget.delete("1.0", "end-1c")
        widget.config(fg="black")

def restore_placeholder(widget, placeholder_text):
    if not widget.get("1.0", "end-1c"):
        widget.insert("1.0", placeholder_text)
        widget.config(fg="gray")

def clear_labels():
    a.delete("1.0", "end")
    b.delete("1.0", "end")
    c.delete("1.0", "end")
    
    # Restore placeholders
    restore_placeholder(a, placeholder_text_a)
    restore_placeholder(b, placeholder_text_b)
    restore_placeholder(c, placeholder_text_c)

    # Restore original label text
    label2.config(text="The Determinant is : ")
    label3.config(text="The Roots are : ")

def equal_click():
    x = int(a.get("1.0", "end"))
    y = int(b.get("1.0", "end"))
    z = int(c.get("1.0", "end"))
    d = determinant.det(x, y, z)
    r = roots.root(x, y, z)

    label2.config(text="The Determinant is : " + str(d))
    label3.config(text="The Roots are : " + str(r))

root = Tk()
root.title("Quadratic Equation Solver")

a = Text(root, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)
b = Text(root, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)
c = Text(root, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)

# Defining the Labels
label1 = Label(root, text="Enter the Coefficients of x\u00b2, x, and the constant respectively")
label2 = Label(root, text="The Determinant is :")
label3 = Label(root, text="The Roots are :")

# Defining the Empty Labels
empty0 = Label(root, text=" ")
empty1 = Label(root, text=" ")
empty2 = Label(root, text=" ")
empty3 = Label(root, text=" ")
empty4 = Label(root, text=" ")
empty5 = Label(root, text=" ")

empty10 = Label(root, text="    ")
empty11 = Label(root, text=" ")
empty12 = Label(root, text=" ")
empty13 = Label(root, text="    ")

# Defining the Buttons
calculate_roots = Button(root, text="Calculate Roots", command=equal_click)

clear_button = Button(root, text="Clear", command=clear_labels)

# Placeholder for x square
placeholder_text_a = "x²"
a.insert("1.0", placeholder_text_a)
a.config(fg="gray")
a.bind("<FocusIn>", lambda event, widget=a, placeholder=placeholder_text_a: clear_placeholder(event, widget, placeholder))

# Placeholder for x
placeholder_text_b = "x"
b.insert("1.0", placeholder_text_b)
b.config(fg="gray")
b.bind("<FocusIn>", lambda event, widget=b, placeholder=placeholder_text_b: clear_placeholder(event, widget, placeholder))

# Placeholder for constant
placeholder_text_c = "Constant"
c.insert("1.0", placeholder_text_c)
c.config(fg="gray")
c.bind("<FocusIn>", lambda event, widget=c, placeholder=placeholder_text_c: clear_placeholder(event, widget, placeholder))


# Assembling the GUI
empty0.grid(row=0, column=0)

label1.grid(row=1, column=1, columnspan=5)

empty1.grid(row=2, column=0, columnspan=3)

a.grid(row=3, column=1)
b.grid(row=3, column=3)
c.grid(row=3, column=5)

empty10.grid(row=3, column=0)
empty11.grid(row=3, column=2)
empty12.grid(row=3, column=4)
empty13.grid(row=3, column=6)

empty2.grid(row=4, column=0)

calculate_roots.grid(row=5, column=2, columnspan=3)

empty3.grid(row=6, column=0)

label2.grid(row=7, column=2, columnspan=3)
label3.grid(row=8, column=2, columnspan=3)

empty4.grid(row=9, column=0)

clear_button.grid(row=10, column=2, columnspan=3)

empty5.grid(row=11, column=0)

root.mainloop()