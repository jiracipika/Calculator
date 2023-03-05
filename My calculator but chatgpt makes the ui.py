from cmath import sqrt
import math
import tkinter as tk

def calculate():
    choice = operation.get()
    if choice != '^':
        number_1 = float(entry1.get())
        number_2 = float(entry2.get())

    # add
    if choice == "+":
        result = number_1 + number_2
    # subtract
    elif choice == "-":
        result = number_1 - number_2
    # multiplication
    elif choice == "*":
        result = number_1 * number_2
    # division
    elif choice == "/":
        result = number_1 / number_2
    # percent
    elif choice == "%":
        result = number_1 % number_2
    # square root
    elif choice == "^":
        num = float(entry1.get())
        if num < 0:
            result = "Cannot take square root of a negative number!"
        else:
            result = sqrt(num)

    output_label.config(text=result)

# Create the GUI window
window = tk.Tk()
window.title("Calculator")

# Create an entry field to input first number
entry1 = tk.Entry(window, width=35, borderwidth=5)
entry1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry field to input second number
entry2 = tk.Entry(window, width=35, borderwidth=5)
entry2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a dropdown for the operation choice
operation_choices = ['+', '-', '*', '/', '%', '^']
operation = tk.StringVar()
operation.set('+')
operation_dropdown = tk.OptionMenu(window, operation, *operation_choices)
operation_dropdown.grid(row=2, column=0, padx=10, pady=10)

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1, padx=10, pady=10)

# Create a label to display the output
output_label = tk.Label(window, text="")
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
