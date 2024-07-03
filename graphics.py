from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas()
        self.canvas.pack()
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
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = window

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(left_wall)

        if self.has_right_wall:
            right_wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(right_wall)

        if self.has_top_wall:
            top_wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(top_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        from_cell_center_x = (self.x1 + self.x2) / 2
        from_cell_center_y = (self.y1 + self.y2) / 2
        to_cell_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) / 2
        color = "black"
        if not undo:
            color = "red"
        Line(
            Point(from_cell_center_x, from_cell_center_y),
            Point(to_cell_center_x, to_cell_center_y),
        ).draw(self.win.canvas, color)
