import curses


def main(scr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE,  curses.COLOR_WHITE)
    curses.curs_set(0)

    winy, winx = scr.getmaxyx()
    scr.keypad(1)
    scr.refresh()

    menus = [
        ('File', [
            ('Open', None),
            ('Save', None),
            ('Exit', exit)]),
        ('Edit', [
            ('Cut',   None),
            ('Copy',  None),
            ('Paste', None)]),
        ('Boonswaggle', [
            ('Swoondoggle', None)]),
        ('Window', [
            ('Split...', None),
            ('Reset',    None)]),
        ('Help', [
            ('Manual',    None),
            ('Reference', None),
            ('About',     None)])]

    segs  = [len(s) + 3 for s, _ in menus]
    stops = [1] + [1 + sum(segs[:i]) for i in range(1, len(menus) + 1)]
    sel   = 0
    lens  = [len(s) for s, _ in menus]
    mcol  = curses.color_pair(1)

    mwin = curses.newwin(1, winx, 0, 0)
    mwin.bkgd(curses.color_pair(1))
    rest = curses.newwin(winy-1, winx, 1, 0)

    drop       = None
    drop_sel   = 0

    while True:
        rest.clear()
        rest.noutrefresh()

        mwin.addstr(0, 0, ' ', mcol)
        for i, menu in enumerate(name for name, _ in menus):
            attr = curses.A_REVERSE if sel == i else 0
            start = sum(lens[:i]) + 1 + (3 * i)
            mwin.addstr(0, start, menu[0], attr|curses.color_pair(3))
            mwin.addstr(0, start + 1, menu[1:], attr)
            mwin.addstr(0, start + len(menu), '   ')
        drawn = 1 + sum(lens) + (3 * len(menus))
        mwin.addstr(0, drawn, ' ' * (mwin.getmaxyx()[1] - 1 - drawn))
        mwin.noutrefresh()

        if drop:
            items = [n for n, _ in menus[sel][1]]
            my, mx = drop.getmaxyx()
            drop.clear()
            drop.hline(0, 0, '-', mx)
            for i, name in enumerate(items):
                attr = curses.A_REVERSE if drop_sel == i else 0
                drop.addstr(1 + i, 1, name, attr)
            drop.hline(my - 1, 0, '-', mx)
            drop.noutrefresh()

        curses.doupdate()

        key = scr.getch()
        if key in [curses.KEY_RIGHT, ord('f'), ord('F')]:
            sel  = min(sel + 1, len(menus) - 1)
            drop = None
        elif key in [curses.KEY_LEFT, ord('b'), ord('B')]:
            sel  = max(sel - 1, 0)
            drop = None
        elif drop and key == curses.KEY_DOWN:
            items = [n for n, _ in menus[sel][1]]
            drop_sel = min(drop_sel + 1, len(items) - 1)
        elif drop and key == curses.KEY_UP:
            drop_sel = max(drop_sel - 1, 0)
        elif drop and key in [ord('\n'), ord(' ')]:
            fn = menus[sel][1][drop_sel][1]
            if fn:
                fn()
        elif key in [ord('\n'), ord(' '), curses.KEY_DOWN]:
            if drop:
                drop = None
            else:
                items = [n for n, _ in menus[sel][1]]
                if items:
                    w = max(10, max(len(s) for s in items) + 2)
                    h = 2 + len(items)
                else:
                    w = 10
                    h = 2
                drop = curses.newwin(h, w, 1, stops[sel])
                drop.bkgd(curses.color_pair(1))
                drop_sel = 0


if __name__ == '__main__':
    curses.wrapper(main)
