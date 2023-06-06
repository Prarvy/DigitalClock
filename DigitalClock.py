from tkinter import Label, Tk
import time
import datetime as dt


class DigitalClock(Tk):

    def __init__(self):
        super().__init__()
        self.title("D I G I T A L   C L O C K")
        self.geometry("450x220")
        self.configure(background="black")
        self.iconbitmap("clock.ico")

        self.text_font = ("Arial", 80, "bold")
        self.small_font = ("Arial", 20, "bold")
        self.foreground = "green"
        self.background = "black"
        self.border_width = 10

        self.label = Label(self, font=self.text_font, bg=self.background, fg=self.foreground, bd=self.border_width)
        self.label.grid(row=0, column=1)
        self.label2 = Label(self, font=self.small_font, text=dt.datetime.now().strftime("%B | %Y-%m-%d | %A").upper(),
                            bg=self.background, fg='yellow', bd=20)
        self.label2.grid(row=1, column=1)

        self.update_time()

    def update_time(self):
        time_live = time.strftime("%H:%M:%S")
        self.label.config(text=time_live)
        self.label.after(1000, self.update_time)


if __name__ == "__main__":
    digital_clock = DigitalClock()
    digital_clock.mainloop()
