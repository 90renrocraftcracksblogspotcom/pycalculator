#Gui for Py calculator

import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = variable.get()
        
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Select operation:").grid(row=2, column=0)
variable = tk.StringVar(root)
variable.set("Add")
tk.OptionMenu(root, variable, "Add", "Subtract", "Multiply", "Divide").grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()