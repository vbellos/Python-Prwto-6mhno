#!/usr/bin/python
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
	return 9

def w2num(n):
	if 'one' in n:
		x = one()
	elif 'two' in n:
		x=two()
	elif 'three' in n:
		x=three()
	elif 'four' in n:
		x=four()
	elif 'five' in n:
		x=five()
	elif 'six' in n:
		x == six()
	elif 'seven' in n:
		x = seven()
	elif 'eight' in n:
		x = eight()
	elif 'nine' in n:
		x = nine()
	elif 'zero' in n:
		x=zero()
	else:
		print 'lathos eisodos'
		
	return x;

def calc(n):
    if 'plus' in n:
        y = n.split('plus')
        x = w2num(y[0]) + w2num(y[1])
    elif 'minus' in n:
        y = n.split('minus')
        x = w2num(y[0]) - w2num(y[1])
    elif 'times' in n:
        y = n.split('times')
        x = w2num(y[0]) * w2num(y[1]) 
    else :
		x = 0
    return x
    

    
z = raw_input("Dwse Ypologismo tou typou 'one plus two','five minus three','three times five': \n")    
print (calc(z))
    
    
