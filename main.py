import os

from tkinter import *
from tkinter.font import Font


class App(Tk):
    def __init__(self):
        super().__init__()

        self.wm_iconbitmap('images/icon.ico')
        self.title('Selection color')
        self.resizable(0, 0)


        self.red = 0
        self.redD = 0
        self.green = 0
        self.greenD = 0
        self.blue = 0
        self.blueD = 0

        self.placement()

    def rgb_to_hex(self, r:int, g:int, b:int) -> str:
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def setRGB(self, color:int):
        if color == 1:
            self.red = int(self.redScal.get())
            if self.red - 30 < 0:
                self.redD = 0
            else:
                self.redD = self.red - 30
        if color == 2:
            self.green = int(self.greenScal.get())
            if self.green - 30 < 0:
                self.greenD = 0
            else:
                self.greenD = self.green - 30
        if color == 3:
            self.blue = int(self.blueScal.get())
            if self.blue - 30 < 0:
                self.blueD = 0
            else:
                self.blueD = self.blue - 30

        self.light = self.rgb_to_hex(self.red, self.green, self.blue)
        self.dark = self.rgb_to_hex(self.redD, self.greenD, self.blueD)

        self.canvas.create_rectangle(0, 0, 300, 150, outline=self.light, fill=self.light)
        self.canvas.create_rectangle(14, 14, 290, 140, outline=self.dark, fill=self.dark)

    def placement(self):

        def setR(a): self.setRGB(1)
        def setG(a): self.setRGB(2)
        def setB(a): self.setRGB(3)

        self.redScal = Scale(orient=HORIZONTAL, length=300, from_=0, to=255, tickinterval=255, resolution=1, command= setR, label='Red')
        self.greenScal = Scale(orient=HORIZONTAL, length=300, from_=0, to=255, tickinterval=255, resolution=1, command= setG, label='Green')
        self.blueScal = Scale(orient=HORIZONTAL, length=300, from_=0, to=255, tickinterval=255, resolution=1, command= setB, label='Blue')

        self.canvas = Canvas(self, width=300, height=150)

        startButton = Button(text='Start', command=self.start, width=11, height=3).grid(row=4, column=6)

        self.redScal.grid(row=2, column=1)
        self.greenScal.grid(row=3, column=1)
        self.blueScal.grid(row=4, column=1)

        self.canvas.grid(row=2, column=2, rowspan=2, columnspan=5)
        
    def start(self):
        with open('start.reg', 'w+') as file:
            file.write(f'Windows Registry Editor Version 5.00\n\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"Hilight"="{self.red} {self.green} {self.blue}"\n\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"HotTrackingColor"="{self.redD} {self.greenD} {self.blueD}"')

        os.system('start.reg')

if __name__ == '__main__':
    app = App()
    app.mainloop()
