import tkinter as tk

# Function to update the input field
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("error")
        expression = ""

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.resizable(0, 0)

expression = ""
input_text = tk.StringVar()

# Create input field
input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Internal padding for the entry field

# Create the buttons frame
buttons_frame = tk.Frame(window, width=400, height=450, bg="grey")
buttons_frame.pack()

# First row
clear = tk.Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=button_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

# Second row
seven = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("7")).grid(row=1, column=0, padx=1, pady=1)
eight = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("8")).grid(row=1, column=1, padx=1, pady=1)
nine = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("9")).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third row
four = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("4")).grid(row=2, column=0, padx=1, pady=1)
five = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("5")).grid(row=2, column=1, padx=1, pady=1)
six = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("6")).grid(row=2, column=2, padx=1, pady=1)
subtract = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("1")).grid(row=3, column=0, padx=1, pady=1)
two = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("2")).grid(row=3, column=1, padx=1, pady=1)
three = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("3")).grid(row=3, column=2, padx=1, pady=1)
add = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth row
zero = tk.Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=button_equal).grid(row=4, column=3, padx=1, pady=1)

# Start the main event loop
window.mainloop()
