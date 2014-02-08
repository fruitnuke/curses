Learning to use the (python) curses library. See [screencasts](http://www.youtube.com/watch?v=FqiUClkEWz0&list=PLuUP5eKYlWmLtB-I5Y3TCFibpaz7xBwbf&feature=share) of the code being written.

#### 01 checkers.py

Drawing an ascii picture of a (configurable-size) checkers board in the
terminal.

<img src="http://fruitnuke.github.io/curses/img/checkers.png" height="50%" width="50%"/>

    $ python3 checkers.py --size=10

#### 02 noise.py

Using refresh and non-blocking key input to display an animation of white noise.

<img src="http://fruitnuke.github.io/curses/img/noise.gif" height="50%" width="50%"/>

    $ python3 noise.py

#### 03 mandelbrot.py

Experimenting with color in curses by drawing a mandelbrot plot. (Requires a
terminal with at least 16 colors.) I discovered after trial-and-error that
extended support for color in Terminal.App on Mac OS X is pretty limited!

    $ python3 mandelbrot.py

#### 04 move.py

Using keyboard input to move a character around the terminal screen.

	$ python3 move.py

#### 05 windows.py

Experimenting with windows in curses by displaying random windows of pretty
patterns (noise, mandelbrot or scrolling ascii).

	$ python3 windows.py

#### 06 mandelpad.py

Using pads to scroll around an area larger than the screen.

	$ python3 mandelpad.py

#### 07 menu.py

Create an interactive menu from scratch, and try out attributes while I'm at it.

	$ python3 menu.py
