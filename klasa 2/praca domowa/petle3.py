#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle-cw3.py
#  

def main(args):
	a = 0
	x = int(input("podaj: "))
	
	for x in range(x+1):
		a = x*x
		print(a)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
