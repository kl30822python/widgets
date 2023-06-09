import tkinter as tk
from parts import TopFrame, MediumFrame, BottomFrame


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        topFrame = TopFrame(self, borderwidth=0)        
        topFrame.pack()
        mediumFrame = MediumFrame(self,borderwidth=0)
        mediumFrame.pack(fill=tk.X)
        bottomFrame = BottomFrame(self)
        bottomFrame.pack(fill=tk.X)

    def radioButtonEventOfMediumFrame(self,radioButtonValue):
        print(radioButtonValue)

    def listBoxEventOfBottomFrame(self, listBoxValue):
        print(listBoxValue)

    def comboBoxEventOfBottomFrame(self,comboValue):
        print(comboValue)

        



def main():
    window = Window()
    window.title("Widgets")
    window.mainloop()

if __name__ == "__main__":
    main()