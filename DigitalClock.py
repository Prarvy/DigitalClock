import tkinter as tk
import datetime as dt
import time


# Create a tkinter window
window = tk.Tk()
window.title('D I G I T A L   C L O C K')
window.iconbitmap("clock.ico")

# Define the font style
big_font = ("Arial Bold", 60)
dot_font = ("Calibri", 80)
meridian_font = ("Arial Bold", 25)
month_date_day_font = ("Yu Gothic Bold", 15)
clock_format_font = ("Yu Gothic", 13)

# Load the image
bg_image = tk.PhotoImage(file="bg.png")

# Load the first image
switch_on_image = tk.PhotoImage(file="s_on.png")

# Load the second image
switch_off_image = tk.PhotoImage(file="s_off.png")

# Create a canvas
canvas = tk.Canvas(window, width=450, height=200)
canvas.pack()

# Display the image on the canvas
canvas.create_image(225, 125, anchor=tk.CENTER, image=bg_image)

# Display the initial image on the canvas
switch_image = canvas.create_image(150, 170, anchor=tk.CENTER, image=switch_on_image)

# Keep track of the current image
current_image = switch_on_image


# Define the callback function for the click event of switch
def switch_click(event):
    global time_format
    global current_image
    if time_format == "12 H":
        time_format = "24 H"
    else:
        time_format = "12 H"
    if current_image == switch_on_image:
        # Change to the Switch OFF image
        canvas.itemconfig(switch_image, image=switch_off_image)
        current_image = switch_off_image
    else:
        # Change back to the Switch ON image
        canvas.itemconfig(switch_image, image=switch_on_image)
        current_image = switch_on_image


# Bind the callback function to the click event of switch
canvas.tag_bind(switch_image, "<Button-1>", switch_click)

# Create canvas texts for hours, minutes, seconds, colons, am/pm, date, and clock format
hour_text = canvas.create_text(100, 70, text="", font=big_font, fill="#00e013", anchor=tk.CENTER)
colon1_text = canvas.create_text(155, 60, text=":", font=dot_font, fill="#a3a3a3", anchor=tk.CENTER)
minute_text = canvas.create_text(215, 70, text="", font=big_font, fill="#ff8800", anchor=tk.CENTER)
colon2_text = canvas.create_text(275, 60, text=":", font=dot_font, fill="#a3a3a3", anchor=tk.CENTER)
second_text = canvas.create_text(335, 70, text="", font=big_font, fill="#00d9ff", anchor=tk.CENTER)
meridian_text = canvas.create_text(410, 85, text="", font=meridian_font, fill="#00cf12", anchor=tk.CENTER)
month_date_day_text = canvas.create_text(225, 130, text="", font=month_date_day_font, fill="#c7c7c7", anchor=tk.CENTER)
clock_format = canvas.create_text(265, 171, text="12 HOUR FORMAT", font=clock_format_font, fill="#ababab",
                                  anchor=tk.CENTER)


# Define the timer function
def start_timer():
    current_mm_ss = time.strftime("%M:%S")
    minute, second = current_mm_ss.split(":")
    canvas.itemconfig(minute_text, text=minute)
    canvas.itemconfig(second_text, text=second)
    canvas.itemconfig(month_date_day_text, text=dt.datetime.now().strftime("%B  |  %Y-%m-%d  |  %A").upper())

    if time_format == "12 H":
        canvas.itemconfig(hour_text, text=time.strftime("%I"))
        am_pm = time.strftime("%p")
        canvas.itemconfig(meridian_text, text=am_pm)
    else:
        canvas.itemconfig(hour_text, text=time.strftime("%H"))
        canvas.itemconfig(meridian_text, text="")

    window.after(100, start_timer)


# Initialize time format to 12-hour
time_format = "12 H"

# Start the timer
start_timer()

# Start the tkinter event loop
window.mainloop()
