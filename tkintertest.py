import tkinter as tk
import pyautogui as pg

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.custom_button = tk.Button(self)
        self.custom_button["text"] = "PyAutoGUI Power!"
        self.custom_button["fg"]="blue"
        self.custom_button["command"] = self.open_chrome
        self.custom_button.pack(side="left")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def open_chrome(self):
        pg.hotkey('winleft')
        pg.typewrite('chrome\n',0.2)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
