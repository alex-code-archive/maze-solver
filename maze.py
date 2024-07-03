from graphics import Window, Line, Point, Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows + 1):
            self.cells.append([])
            for j in range(self.num_cols + 1):
                cell = Cell(
                    self.x1,
                    self.y1,
                    self.x1 + j * self.cell_size_x,
                    self.y1 + i * self.cell_size_y,
                    self.win,
                )
                self.cells[i].append(cell)
                self._draw_cell(i, j)
                self._animate()

    def _draw_cell(self, i, j):
        cell = self.cells[i][j]
        cell.draw()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)
