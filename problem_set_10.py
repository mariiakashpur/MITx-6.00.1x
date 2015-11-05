def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return round (a * x ** 2 + b * x + c , 4)

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    print evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)


def primesList(N): 
	my_list = []
	for num in range(2, N+1): 
		prime = True
		for div in range(2, num): 
			if num % div == 0:
				prime = False
				break
		if prime:
			my_list.append(num)
	return my_list
				
#print primesList(100)


def count7(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
    	return 0
    elif N % 10 == 7:
    	return 1 + count7(N / 10)
    else:
    	return count7(N / 10)
    	
#print count7(8989)


def uniqueValues(aDict):
	'''
	aDict: a dictionary
	'''
	my_dict = dict()
	my_list = list()
	for key, value in aDict.iteritems():
 		if value not in my_dict:
 			my_dict[value] = [key]
 		else:
 			my_dict[value].append(key)
 	for key, value in my_dict.iteritems():
 		if len(value) == 1:
 			my_list.append(value[0])
 	return sorted(my_list)



# print uniqueValues({1: 100, 2: 100, 3: 1})

def f(s):
    return 'a' in s
      
def satisfiesF(L):
	"""
	Assumes L is a list of strings
	Assume function f is already defined for you and it maps a string to a Boolean
	Mutates L such that it contains all of the strings, s, originally in L such
	that f(s) returns True, and no other elements. Remaining elements in L
	should be in the same order.
	Returns the length of L after mutation
	"""
	count = len(L)
	rec_list = list()
	for i in range(0,count):
		if(f(L[i]) == False):
			rec_list.append(L[i])    
	if(rec_list):
		for j in rec_list:
			L.remove(j)
	return len(L)

# L = ['a', 'b', 'a']
# print satisfiesF(L)
# print L

# 2
# ['a', 'a']

# my_list = list()
# for item in L:
# 	if f(item):
# 		my_list.append(item)
# L[:] = my_list
# return len(L)