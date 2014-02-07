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

    scrs = []
    fns  = []

    winy, winx = stdscr.getmaxyx()
    scrs.append(make_win(winy, winx))
    fns.append(random.choice([noise, mandel]))

    while True:
        key = stdscr.getch()
        if key in (ord('Q'), ord('q')):
            break
        elif key == curses.KEY_RESIZE:
            winy, winx = stdscr.getmaxyx()
        elif key != curses.ERR:
            if len(scrs) > 2:
                scr = scrs.pop(0)
                scr.clear()
                scr.noutrefresh()
                fns.pop(0)

            scrs.append(make_win(winy, winx))
            fns.append(random.choice([noise, mandel, pattern]))

        time.sleep(0.05)
        for scr, fn in zip(scrs, fns):
            fn(scr)

        curses.doupdate()


def fn(f):
    def wrapper(scr):
        f(scr)
        scr.border()
        scr.noutrefresh()
    return wrapper


def make_win(winy, winx):
    x1 = random.randint(0, winx // 2)
    y1 = random.randint(0, winy // 2)
    x2 = random.randint(x1 + 20, winx)
    y2 = random.randint(y1 + 20, winy)
    return curses.newwin(y2 - y1, x2 - x1, y1, x1)


@fn
def noise(scr):
    my, mx = scr.getmaxyx()
    scr.clear()
    for y, x in itertools.product(range(my-1), range(0, mx-1, 2)):
        if random.random() > 0.65:
            scr.addch(y, x, chr(0x2588))


@fn
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


@fn
def pattern(scr):
    my, mx = scr.getmaxyx()
    color = curses.color_pair(2)
    a = ord('a')
    n = int(time.perf_counter() * 16)
    for y, x in itertools.product(range(my-1), range(0, mx-1)):
        scr.addch(y, x, a + (n + x + y) % 26, color)


if __name__ == '__main__':
    curses.wrapper(main)
