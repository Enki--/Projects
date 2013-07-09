#!/usr/bin/env python

#Some peopel simply printed pi here, I wanted to actaully compute it, math is stolen obvously

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(digits):
	unity = 10**(digits + 10)
	pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
	return pi // 10**10

totalDigits = int(raw_input("How many digits do you want? (Don't do anything crazy)"))
print pi(totalDigits)