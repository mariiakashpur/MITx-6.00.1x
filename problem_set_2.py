s = 'azcbobobegghakl' 
current = ""
longest_so_far = ""
for char in s:
	if current == "":
		current += char
	elif current[-1] <= char:
		current += char
	elif current[-1] > char:
		if len(longest_so_far) < len(current):
			longest_so_far = current
			current = char
		else:
			current = char
if len(longest_so_far) < len(current):
	longest_so_far = current
print "Longest substring in alphabetical order is: " + longest_so_far

# Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code should print out the result:

# 21

# which is 1 + 2 + 3 + 4 + 5 + 6.

num = 1
total = 0
while num <= end:
	total += num
	num += 1
print total


for variable in range(20): 
	if variable % 4 == 0:
		print variable
	if variable % 16 == 0:
		print 'Foo!' 

# 0 foo 4 8 12 16 foo

count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 



iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)



high = 100
low = 0
ind = ""
print "Please think of a number between 0 and 100!"
while ind != "c":
	ans = (high - low)/2
	print "Is your secret number " + str(ans) + "?"
	ind = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if ind not in "hlc":
		print "Sorry, I did not understand your input."
	else:
		if ind == "h":
			high = ans
		elif ind == "l":
			low = ans
print "Game over. Your secret number was: " + str(ans)


# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 25?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 37?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 43?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 40?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 41?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 42?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 42