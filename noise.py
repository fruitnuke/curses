import curses
import random
import time


def main(scr):
    scr.nodelay(True)
    while True:
        if scr.getch() not in (curses.ERR, curses.KEY_RESIZE):
            break
        my, mx = scr.getmaxyx()
        scr.clear()
        for y in range(my-1):
            for x in range(mx):
                if random.random() > 0.65:
                    scr.addch(y, x, chr(0x2588))
        scr.refresh()
        time.sleep(0.2)


if __name__ == '__main__':
    curses.wrapper(main)
