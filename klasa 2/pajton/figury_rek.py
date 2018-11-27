#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py
#  
#  Copyright 2018  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py
import turtle

def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat < warunek:
        rysuj(bok, kat, przyrost, warunek-przyrost)


def main(args):
    turtle.setup(800, 600)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.speed(10)
    
    rysuj(bok=400, kat=120, przyrost=10, warunek=180)
    
    turtle.end_fill()
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
