balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0
for month in range(1, 13):
	monthlyPayment = balance * monthlyPaymentRate
	unpaidBalance = balance - monthlyPayment 
	balance = unpaidBalance + annualInterestRate/12.0 * unpaidBalance
	print "Month: " + str(month)
	print "Minimum monthly payment: " + str(round(monthlyPayment, 2))
	print "Remaining balance: " + str(round(balance, 2))
	total += monthlyPayment
print "Total paid: " + str(round(total, 2))
print "Remaining balance: " + str(round(balance, 2))