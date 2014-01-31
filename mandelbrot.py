import curses
import itertools


def main(scr):
    curses.start_color()
    for i in range(1, 16):
        curses.init_pair(i, i, i)

    while True:
        my, mx = scr.getmaxyx()
        for y, x in itertools.product(range(my-1), range(0, mx-1, 2)):
            c = complex(-2.0 + 3.0 * int(x / 2) / int(mx / 2), -1.5 + 3.0 * y / my)
            z = complex(0.0, 0.0)
            for col in range(16):
                z = z * z + c
                if abs(z) >= 2.0:
                    break
            scr.addch(y, x, chr(0x02588), curses.color_pair(col))
            scr.addch(y, x + 1, chr(0x02588), curses.color_pair(col))

        if scr.getch() != curses.KEY_RESIZE:
            break


if __name__ == '__main__':
    curses.wrapper(main)