balance = 3400
initialBalance = balance
annualInterestRate = 0.2
monthlyPayment = 0

while balance > 0:
	balance = initialBalance
	monthlyPayment += 10
	for month in range(12):
		unpaidBalance = balance - monthlyPayment 
		balance = unpaidBalance + annualInterestRate/12.0 * unpaidBalance
print "Lowest Payment: " + str(monthlyPayment)




# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

#     Now imagine that we try our initial balance with a monthly payment of $10. 
#     If there is a balance remaining at the end of the year, how could we write code that would reset the balance to the initial balance, increase the payment by $10, 
#     and try again (using the same code!) to compute the balance at the end of the year, to see if this new payment value is large enough.
#     A good way to implement this problem will be to use a loop structure. You may want to refresh your understanding of while loops.
#      Think hard about how the program will know when it has found a good minimum monthly payment value - when a good value is found, the loop can terminate. 

# Be careful - you don't want to overwrite the original value of balance. You'll need to save that value somehow for later reference!