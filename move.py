import curses


def main(scr):
    curses.curs_set(0)
    scr.clear()
    my, mx = scr.getmaxyx()
    x = int(mx/2)
    y = my - int(my/2)

    while True:
        scr.clear()
        scr.addch(y, x, chr(0x263A))
        key = scr.getch()
        if key in [ord('q'), ord('Q')]:
            break
        if key == curses.KEY_LEFT:
            x = x - 1
        elif key == curses.KEY_RIGHT:
            x = x + 1
        elif key == curses.KEY_UP:
            y = y - 1
        elif key == curses.KEY_DOWN:
            y = y + 1

        x = max(0,  x)
        x = min(mx-1, x)
        y = max(0,  y)
        y = min(my-1, y)


if __name__ == '__main__':
    curses.wrapper(main)