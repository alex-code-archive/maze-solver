from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    c = Cell(50, 50, 100, 100, win)
    c.has_left_wall = False
    c.draw()

    c = Cell(125, 125, 200, 200, win)
    c.has_right_wall = False
    c.draw()

    c = Cell(225, 225, 250, 250, win)
    c.has_bottom_wall = False
    c.draw()

    c = Cell(300, 300, 500, 500, win)
    c.has_top_wall = False
    c.draw()
    print("made it")
    win.wait_for_close()


if __name__ == "__main__":
    main()
