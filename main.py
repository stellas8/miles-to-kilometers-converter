from tkinter import *

# Function to calculate miles to kilometres
def calculate():
    user_input_value = user_input.get()
    km_value = round(int(user_input_value) * 1.609, 2)
    km_calculated_label = Label(text=km_value, font=("Arial", 18, "bold"))
    km_calculated_label.grid(column=1, row=1)

# Window setup
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=25, pady=25)

# User entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# creating labels
miles_label = Label(text="Miles", font=("Arial", 18, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to", font=("Arial", 18, "bold"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 18, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# creating button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

window.mainloop()
