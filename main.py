from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        root = Tk()
        root.title = "Maze Solver"
        canvas = Canvas()
        canvas.pack()
        running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

