import tkinter as tk

# Function to update the expression in the display
def press(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button)

# Function to evaluate the expression
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Ini Kalkulator SIGMA")

# Create a display area
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

# Place buttons on the grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, height=3, width=9, command=calculate).grid(row=row, column=col, columnspan=2)
        col += 2
    else:
        tk.Button(window, text=button, height=3, width=5, command=lambda b=button: press(b)).grid(row=row, column=col)
        col += 1
    if col == 4:
        col = 0
        row += 1

# Add clear button
tk.Button(window, text='C', height=3, width=5, command=clear).grid(row=row, column=0)

# Start the GUI loop
window.mainloop()


