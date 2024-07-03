from graphics import Window, Line, Point, Cell
from maze import Maze


def main():
    win = Window(800, 600)
    # c = Cell(50, 50, 100, 100, win)
    # c.has_left_wall = False
    # c.draw()
    #
    # c1 = Cell(125, 125, 200, 200, win)
    # c1.has_right_wall = False
    # c1.draw()
    #
    # c2 = Cell(225, 225, 250, 250, win)
    # c2.has_bottom_wall = False
    # c2.draw()
    # c2.draw_move(c1, True)
    #
    # c = Cell(300, 300, 500, 500, win)
    # c.has_top_wall = False
    # c.draw()
    Maze(10, 10, 5, 5, 50, 50, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
