import pyautogui
import tkinter as tk
from pynput import mouse


class Picker: 

    def __init__(self):
        self.win = tk.Tk()
        self.color_label = None
        self.color = None
        self.hex = None


    def show(self):
        self.win.deiconify()

    def hidden(self):
        self.win.withdraw()

    def listener(self):
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()

    def hex_color(self, color):
        self.hex = "#{0:02x}{1:02x}{2:02x}".format(color[0],color[1],color[2])

    def get_color(self, x, y):
        shot = pyautogui.screenshot()
        self.color = shot.getpixel((x,y))
        self.hex_color(self.color)   
        print(f"color: {self.color}, hex: {self.hex}")  

    def update_color(self):
        self.color_label["text"] = f"Hex: {self.hex}, RGB: {self.color}"
        self.color_label["background"] = self.hex

    def on_click(self, x, y, button, pressed):
        print('{0} action {1} at {2}'.format(button, 'Pressed' if pressed else 'Released', (x,y)))
        self.get_color(x, y)
        self.update_color()
        if not pressed:
            self.show()
            return False
    
    def begin_pick(self):
        self.hidden()
        self.listener()


    def copy_hex(self):
        self.win.clipboard_clear()
        self.win.clipboard_append(self.hex)
    
    def copy_rgb(self):
        self.win.clipboard_clear()
        self.win.clipboard_append(self.color)

    def build(self):
        self.win.title("color picker")
        self.win.geometry("250x300")
        #self.win.resizable(width=False, height=False)
        frame1 = tk.Frame(master=self.win)
        self.color_label = tk.Label(master=frame1,text="Hex:  Color:",pady=40)
        self.color_label.grid(row=0,column=0)
        frame1.grid(row=0, column=0)

        frame2 = tk.Frame(master=self.win)
        btn = tk.Button(master=frame2, text="pick color", command=self.begin_pick)
        btn.grid(row=0,column=0)
        btn1 = tk.Button(master=frame2, text="copy hex", command=self.copy_hex)
        btn1.grid(row=1,column=0)
        btn2 = tk.Button(master=frame2, text="copy RGB", command=self.copy_rgb)
        btn2.grid(row=2,column=0)

        frame2.grid(row=1, column=0)

        self.win.mainloop()



if __name__ == "__main__":
    pick = Picker()
    pick.build()
