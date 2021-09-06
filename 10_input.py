balance = input ('Balance : ')

balance = int (balance)
interest = 0

if balance > 10000 and balance < 20001:
    print ("good for 1 month expense")
    interest = .5 * balance + balance
elif balance < 10000:
    print ("good for 25 days of life ")
    interest = .2 * balance + balance
else:
    print ("very minimal amount ")
    interest = .02 * balance + balance

print ("", interest)
