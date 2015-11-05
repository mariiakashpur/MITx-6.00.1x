def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    i = exp
    if exp == 0:
        result = 1
    else:
        while i > 1:
            result = result * base
            i -= 1
    return result

#print iterPower(-5.7, 2)

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base * recurPowerNew(base, exp-1)

#print recurPowerNew(2, 4)

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    small = min(a, b) 
    while a % small != 0 or b % small !=0 and small != 1:
        small = small - 1
    return small

# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

#     If b = 0, then the answer is a

#     Otherwise, gcd(a, b) is the same as gcd(b, a % b)
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

#print gcdRecur(17, 12)      

    # gcd(2, 12) = 2

    # gcd(6, 12) = 6

    # gcd(9, 12) = 3

    # gcd(17, 12) = 1


def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    l = 0
    for c in aStr:
        l += 1
    return l
                

#print lenIter("mokka")

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == "":
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

#print lenRecur("mokka")

def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string

	returns: True if char is in aStr; False otherwise
	'''
	high = len(aStr)
	low = 0
	ans = (high + low)/2
	if len(aStr) == 0:
		return False
	elif len(aStr) == 1:
		if char == aStr:
			return True
		else:
			return False
	elif aStr[ans] == char:
		return True
	else:
		if char < aStr[ans]:
			return isIn(char, aStr[:ans])
		else:
			return isIn(char, aStr[ans+1:])
#print isIn("b", "abc")

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
    	return False
    if str1 == str2:
    	return True
    else:
    	if str1[0] == str2[-1]:
    		return semordnilap(str1[1:], str2[:-1])
    	else:
    		return False


#print semordnilapWrapper("tag", "gatg")
    # nametag / gateman
    # dog / god
    # live / evil
    # desserts / stressed


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[0: len(aTup): 2]
#print oddTuples(('I', 'am', 'a', 'test', 'tuple'))



def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for values_list in aDict.values():
        for animal in values_list:
            total += 1
    return total

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        biggest_key = aDict.keys()[0]
        biggest_total = 0
        for key in aDict:
            total = 0
            for value in aDict[key]:
                total += 1
            if total > biggest_total:
                biggest_key = key
                biggest_total = total
        return biggest_key
        
    
