import curses
import itertools


def main(scr):
    curses.curs_set(False)

    curses.start_color()
    for i in range(1, 16):
        curses.init_pair(i, i, curses.COLOR_BLACK)

    scry, scrx = scr.getmaxyx()
    pady = scry * 2
    padx = scrx * 2

    pad = curses.newpad(pady, padx)
    pad.nodelay(True)
    mandel(pad)

    oy = 1
    ox = 0

    while True:
        pad.refresh(oy, ox, 0, 0, scry-1, scrx-1)
        key = pad.getch()
        if key in (ord('q'), ord('Q')):
            break
        elif key in (ord('w'), curses.KEY_UP):
            oy = max(oy - 1, 0)
        elif key in (ord('s'), curses.KEY_DOWN):
            oy = min(oy + 1, pady - scry - 1)
        elif key in (ord('a'), curses.KEY_LEFT):
            ox = max(ox - 2, 0)
        elif key in (ord('d'), curses.KEY_RIGHT):
            ox = min(ox + 2, padx - scrx)
        elif key == curses.KEY_RESIZE:
            scry, scrx = scr.getmaxyx()


def mandel(scr):
    my, mx = scr.getmaxyx()
    for y, x in itertools.product(range(my-1), range(0, mx-1, 2)):
        c = complex(-2.0 + 3.0 * int(x / 2) / int(mx / 2), -1.5 + 3.0 * y / my)
        z = complex(0.0, 0.0)
        for col in range(32):
            z = z * z + c
            if abs(z) >= 2.0:
                break
        scr.addch(y, x, chr(0x02588), curses.color_pair(col))
        scr.addch(y, x + 1, chr(0x02588), curses.color_pair(col))


if __name__ == '__main__':
    curses.wrapper(main)
