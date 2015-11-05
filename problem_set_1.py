s = 'azcbobobegghakl'
count = 0
for char in s:
   if char in "aeiou":
       count += 1
print "Number of vowels: " + str(count)
   
count_bob = 0
for i in range(len(s)):
   if s[i:i+3] == 'bob':
       count_bob += 1
print "Number of times bob occurs is: " + str(count_bob)

