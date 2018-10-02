#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle-cw3.py
#  

def main(args):
	
	for x in range(10, 100):
		if x %2 ==0 and x %3 == 0:
			print (x)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

