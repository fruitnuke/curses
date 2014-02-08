import argparse
import curses


def main(scr, n):
    curses.curs_set(0)

    maxy, maxx = scr.getmaxyx()
    for y in range(maxy-1):
        for x in range(maxx):
            xx = int(x / 2)
            board_row = int(y / n)
            if not abs(board_row % 2 - int((xx % (2 * n)) / n)):
                scr.addstr(y, x, chr(0x2588))
    scr.getch()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, default=None)
    args = parser.parse_args()
    curses.wrapper(main, args.size or 5)
    args = parser.parse_args()
