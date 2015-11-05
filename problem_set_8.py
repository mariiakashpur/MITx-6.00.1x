high = 100
low = 0
ind = ""
print "Please think of a number between 0 and 100!"
while ind != "c":
	ans = (high + low)/2
	print "Is your secret number " + str(ans) + "?"
	ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if ind not in "hlc":
		print "Sorry, I did not understand your input."
	else:
		if ind == "h":
		    high = ans
		else:
		    low = ans
print "Game over. Your secret number was: " + str(ans)

#  Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi; and x otherwise. 
#  For this problem, you can assume that lo < hi.

# Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max. 

def clip(lo, x, hi): 
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(lo, x), hi)

#print clip(3, 2, 4)
    # 1 2 3 -> 2     3 2 4 -> 3    


def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return bool(x%2)
#print odd(4)

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.  True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise.
    '''
    char = char.lower()
    return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"

#print isVowel('A')

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char.lower() in "aeiou"

#print isVowel2('f')