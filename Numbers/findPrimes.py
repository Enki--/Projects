#!/usr/bin/env python
import math

def primeCheck(number):
	if number % 2 == 0 and number != 2:
		return False
	elif number == 2:
		return True
	else:
		for checkNumber in range(2, number):
			if number % checkNumber == 0:
				return False
			else:
				return True

def findPrimes(number):
	primeFactors = []
	for check in range(2, number):
		if primeCheck(check):
			if number % check == 0:
				primeFactors.append(check)

	return primeFactors

numberToBeChecked = int(raw_input("What number would you like to get prime factors of: "))

answer = findPrimes(numberToBeChecked)

print answer