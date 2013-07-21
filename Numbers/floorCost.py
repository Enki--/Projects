#!/usr/bin/python

#Find Cost of Tile to Cover W x H Floor

import argparse

def is_number(s):
    try:
		float(s)
		return True
    except ValueError:
		return False

parser = argparse.ArgumentParser(description='Determine the cost of flooring')
parser.add_argument('dementions', metavar='W,D,C', type=int, nargs='+',
                   help='Width, Depth, and Cost (in any order)')

args = parser.parse_args()
totalCost = 1

for element in args.dementions:
	totalCost = element * totalCost

print "The total cost of your flooring project is: " + str(totalCost)