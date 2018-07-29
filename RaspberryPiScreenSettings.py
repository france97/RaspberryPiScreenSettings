#!/usr/bin/python3

from tkinter import * #Tk, Label, Button, Scale

class MyFirstGUI:
    def __init__(self, master):
        default_brightness = self.read_brightness()
        
        self.master = master
        master.title("Raspberry Pi Screen Settings")

        self.label = Label(master, text="Raspberry Pi Screen Settings")
        self.label.grid(row=0)
        
        self.scale = Scale(master, from_=0, to=255, length=400, tickinterval=25, orient=HORIZONTAL, command=self.change_brightness)
        self.scale.set(default_brightness)
        self.scale.grid(row=2)

        self.greet_button = Button(master, text="Conferma", command=self.save_button)
        self.greet_button.grid(row=3, column=0)

        self.close_button = Button(master, text="Annulla", command=self.close_button)
        self.close_button.grid(row=3, column=1)

    def read_brightness(self):
        try:
            file = open("/sys/class/backlight/rpi_backlight/brightness", "r")
            value = file.read()
            file.close()
        except:
            value = 150
            
        if value == "" or value is None:
            value = 150
            
        return value

    def modify_brightness_value(self, newValue):
        try:
            file = open("/sys/class/backlight/rpi_backlight/brightness", "w")
            value = file.write(str(newValue))
            file.close()
        except:
            print("Error")
    
    def change_brightness(self, value):
        self.modify_brightness_value(self.scale.get())

    def save_button(self):
        self.modify_brightness_value(self.scale.get())
        print("Greetings!")
        self.master.quit()

    def close_button(self):
        self.modify_brightness_value(self.default_brightness)
        print("pause")
        self.master.quit()
        
if __name__ == "__main__":
    print("hello world")
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
