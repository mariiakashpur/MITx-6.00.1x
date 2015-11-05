def getSublists(L, n):
	finalList = []
	for i in range(len(L)-n+1):
		finalList.append(L[i:i+n])
	return finalList

# Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list 
# [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

# Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list 
# [[1, 1], [1, 1], [1, 1], [1, 4]]

#print getSublists([1, 1, 1, 1, 4], 2)

def longestRun(L):
	for i in range(len(L), 0, -1):
		sublists = getSublists(L, i)
		for sublist in sublists:
			if sorted(sublist) == sublist:
				return len(sublist)



# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 
# because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].
# >>> range(5, 0, -1)
# [5, 4, 3, 2, 1]

print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status not in ["citizen", "legal_resident", "illegal_resident"]:
            raise ValueError("") 
        self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status

a = USResident('Tim Beaver', 'citizen')
print a.getStatus()
b = USResident('Tim Horton', 'non-resident')