from tkinter import *
from logic import determinant
from logic import roots 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.title("Quadratic Equation Solver")
root.geometry("550x400")

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
    label2.config(text="The Determinant is :")
    label3.config(text="The Roots are :")
    plt.close('all')
    #if graph_win:
        #graph_win.destroy()

def equal_click():
    global x
    global y
    global z
    x = float(a.get("1.0", "end"))
    y = float(b.get("1.0", "end"))
    z = float(c.get("1.0", "end"))
    d = determinant.det(x, y, z)
    r = roots.root(x, y, z)

    label2.config(text="The Determinant is : " + str(d))
    label3.config(text="The Roots are : " + str(r))

def show_graph():
    #global graph_lbl
    #global graph_btn
    #global graph_win
    #graph_win = Toplevel()
    #graph_win.geometry("500x400")
    plot_quadratic_eq(x, y, z)
    plt.legend()
    plt.grid(True)  # Add grid lines
    plt.show()
    #graph_lbl = Label(graph_win, text="Graph Below").pack()
    #graph_btn = Button(graph_win, text="Close", command=graph_win.destroy).pack()

def plot_quadratic_eq(a, b, c):
    x = list(range(-10, 11))
    y = [a * i**2 + b * i + c for i in x]
    
    # Plot the quadratic curve
    plt.plot(x, y, linestyle='-', color='red')
    
    # Add horizontal (y = 0) and vertical (x = 0) lines
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

# Defining the Frames
frame0 = LabelFrame(root, padx=10, pady=10)
frame1 = LabelFrame(root, padx=10, pady=10)
frame2 = LabelFrame(root, padx=10, pady=10)
frame3 = LabelFrame(root, padx=10, pady=10)

a = Text(frame1, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)
b = Text(frame1, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)
c = Text(frame1, width=5, height=1, bd=2, relief=FLAT, padx=10, pady=10)

# Defining the Labels
label1 = Label(frame0, text="Enter the Coefficients of x\u00b2, x, and the constant respectively")
label2 = Label(frame2, text="The Determinant is :")
label3 = Label(frame2, text="The Roots are :")

# Defining the Empty Labels
empty0 = Label(root, text=" ")
empty1 = Label(root, text=" ")
empty2 = Label(root, text=" ")
empty3 = Label(root, text=" ")
empty4 = Label(root, text=" ")
empty5 = Label(root, text=" ")

empty10 = Label(frame1, text=" ")
empty11 = Label(frame1, text=" ")
empty12 = Label(frame1, text=" ")
empty13 = Label(frame1, text=" ")

# Defining the Buttons
calculate_roots = Button(root, text="Calculate Roots", command=equal_click)

exit_button = Button(frame3, text="Exit", command=root.quit)
clear_button = Button(frame3, text="Clear", command=clear_labels)

graph = Button(frame3, text="Graph", command=show_graph)

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
#empty0.pack()
empty1.pack()

label1.pack()
frame0.pack()

a.grid(row=0, column=1)
b.grid(row=0, column=3)
c.grid(row=0, column=5)

empty10.grid(row=0, column=0)
empty11.grid(row=0, column=2)
empty12.grid(row=0, column=4)
empty13.grid(row=0, column=6)
frame1.pack(pady=10)

#empty2.pack()

calculate_roots.pack()

#empty3.pack()

label2.pack()
label3.pack()
frame2.pack(pady=25)

#empty4.pack()
exit_button.grid(row=1, column=2, padx=10)
clear_button.grid(row=1, column=3, padx=10)
graph.grid(row=1, column=4, padx=10)
frame3.pack()

empty5.pack()

root.mainloop()