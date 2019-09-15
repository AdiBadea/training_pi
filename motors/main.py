import curses

screen = curses.initscr()
# curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord("q"):
            break
        elif char == curses.KEY_UP:
            print("UP")

finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()