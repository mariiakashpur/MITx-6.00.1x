balance = 999999
annualInterestRate = 0.18
monthlyInterest = annualInterestRate / 12.0
upper = (balance * (1 + monthlyInterest) ** 12) / 12.0
lower = balance / 12
initialBalance = balance
while abs(balance) > 0.01:
	balance = initialBalance
	monthlyPayment = (upper + lower)/2
	for month in range(12):
		unpaidBalance = balance - monthlyPayment 
		balance = unpaidBalance + annualInterestRate/12.0 * unpaidBalance
	if balance > 0 :
		lower = monthlyPayment
	else:
		upper = monthlyPayment
print "Lowest Payment: " + str(round(monthlyPayment, 2)) 



# Test Case 2:
# 	      balance = 999999
# 	      annualInterestRate = 0.18
	      
# 	      Result Your Code Should Generate:
# 	      -------------------
# 	      Lowest Payment: 90325.03

