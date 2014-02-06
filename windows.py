"""Display changing random windows of different patterns.

Press 'q' to exit, any other key to create a new window.
"""

import curses
import itertools
import random
import time


def main(stdscr):
    curses.curs_set(False)
    curses.start_color()
    for i in range(1, 16):
        curses.init_pair(i, i, 0)

    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(True)

    winy, winx = stdscr.getmaxyx()
    scr1 = make_win(winy, winx)
    fn = random.choice([noise, mandel])

    while True:
        key = stdscr.getch()
        if key in (ord('Q'), ord('q')):
            break
        elif key == curses.KEY_RESIZE:
            winy, winx = stdscr.getmaxyx()
        elif key != curses.ERR:
            scr1.clear()
            scr1.refresh()
            scr1 = make_win(winy, winx)
            fn = random.choice([noise, mandel, pattern()])

        time.sleep(0.05)
        fn(scr1)
        scr1.refresh()


def make_win(winy, winx):
    x1 = random.randint(0, winx - 10)
    y1 = random.randint(0, winy - 10)
    x2 = random.randint(x1 + 10, winx)
    y2 = random.randint(y1 + 10, winy)
    return curses.newwin(y2 - y1, x2 - x1, y1, x1)


def noise(scr):
    my, mx = scr.getmaxyx()
    scr.clear()
    for y, x in itertools.product(range(my-1), range(0, mx-1, 2)):
        if random.random() > 0.65:
            scr.addch(y, x, chr(0x2588))


def mandel(scr):
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


class pattern():

    def __init__(self):
        self.n = 0

    def __call__(self, scr):
        my, mx = scr.getmaxyx()
        for y, x in itertools.product(range(my-1), range(0, mx-1)):
            i = x + y + self.n
            scr.addch(y, x, ord('a') + (i % 26), curses.color_pair(i % 8))
        self.n += 1


if __name__ == '__main__':
    curses.wrapper(main)
