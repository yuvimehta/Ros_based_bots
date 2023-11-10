import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.geometry('300x400')  # Adjust the window size to accommodate four sliders
root.resizable(False, False)
root.title('Slider Demo')

# Create a list to hold the DoubleVar variables for the sliders
current_values = [tk.DoubleVar() for _ in range(4)]

# Function to get the current value as a formatted string
def get_current_value(index):
    return '{:.2f}'.format(current_values[index].get())

# Function to handle slider changes
def slider_changed(index, event):
    value_labels[index].configure(text=get_current_value(index))
    update_values_list()

# Create labels for the sliders and add them to the grid
slider_labels = [ttk.Label(root, text=f'Slider {i+1}:') for i in range(4)]
for i, label in enumerate(slider_labels):
    label.grid(column=0, row=i, sticky='w')

# Create sliders and add them to the grid
sliders = [ttk.Scale(root, from_=0, to=100, orient='horizontal', variable=current_values[i]) for i in range(4)]
for i, slider in enumerate(sliders):
    slider.grid(column=1, row=i, sticky='we')
    # Bind the slider change event to the slider_changed function with the index
    slider.bind('<Motion>', lambda event, i=i: slider_changed(i, event))

# Create labels to display the current values
value_labels = [ttk.Label(root, text=get_current_value(i)) for i in range(4)]
for i, label in enumerate(value_labels):
    label.grid(row=i, column=2, sticky='w')

# Create a list to store the slider values
slider_values_list = []

# Function to update the slider values list
def update_values_list():
    slider_values_list.clear()
    for i in range(4):
        slider_values_list.append(current_values[i].get())
    print("Slider Values:", slider_values_list)

# Button to trigger printing the slider values
print_button = ttk.Button(root, text="Print Values", command=update_values_list)
print_button.grid(row=4, columnspan=3)

root.mainloop()
