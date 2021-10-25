import time
from tkinter import Label, Tk

# Define title and size of the clock
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("550x175")
app_window.resizable(1, 1)

# Define the clock style
text_font = ("Sans Serif", 96, 'bold')
background = '#2522CA'
foreground = '#ffffff'
border_width = 25

# Define the clock label
clock_label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
clock_label.grid(row=0, column=1)

def clock():
    # Get the current time
    time_string = time.strftime("%H:%M:%S")
    clock_label.config(text=time_string)
    clock_label.after(200, clock)


clock()
app_window.mainloop()
