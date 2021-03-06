# https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.


sequence = [1, 1]
term = 3
current = 1
while current < 4000000:
	new = sequence[term - 2] + sequence[term - 3]
	current = new
	term += 1
	sequence.append(new)
count = 0
for i in sequence:
	if i % 2 == 0:
		count += i
print count