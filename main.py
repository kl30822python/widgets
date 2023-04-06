import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#create canvas with tkinter
#create  image in tkinter with canvas

def createImageOfTkinterUsingPIL():
    pass


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self)
        flowerImage1 = Image.open("./images/Weather-UI-Icon-Kit.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        canvas = tk.Canvas(topFrame, width=744, height=365)
        canvas.pack()
        canvas.create_image(0,0,image=self.flowerPhoto1,anchor='nw')
        canvas.create_text(510,40,text='Weather_UI_Icon_Kit', fill='brown', font=('verdana', 16),anchor='nw')
        topFrame.pack()
        

def main():
    window = Window()
    window.title("Widgets")
    window.mainloop()

if __name__=="__main__":
    main()

