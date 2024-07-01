from graphics import Window, Line, Point


def main():
    point_1 = Point(30, 40)
    point_2 = Point(50, 80)
    line1 = Line(point_1, point_2)

    win = Window(800, 600)

    win.draw_line(line1, "green")
    win.wait_for_close()


if __name__ == "__main__":
    main()
