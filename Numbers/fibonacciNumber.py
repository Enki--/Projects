#!/usr/bin/env python

def fibonacci(howFar):
	F = [0, 1]
	for i in range(howFar - 2):
		F.append(F[-1] + F[-2])
	return F

howFar = int(raw_input("How far would you like to count? "))
fibList = fibonacci(howFar)

print fibList[-1]

