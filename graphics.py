from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(left_wall)
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(left_wall, "white")

        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(right_wall)
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(right_wall, "white")

        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(top_wall)
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        if self.win is None or self.x1 is None or self.y1 is None:
            return
        from_cell_center_x = (self.x1 + self.x2) / 2
        from_cell_center_y = (self.y1 + self.y2) / 2
        to_cell_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) / 2
        color = "black"
        if not undo:
            color = "red"
        line = Line(
            Point(from_cell_center_x, from_cell_center_y),
            Point(to_cell_center_x, to_cell_center_y),
        )
        self.win.draw_line(line, color)
