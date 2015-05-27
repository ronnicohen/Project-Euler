# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
#  in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
#  British usage.

from num2words import num2words
big_word = ''
for j in xrange(1, 1001):
	in_words = str(num2words(j))
	for i in in_words:
		if (i != ' ') and (i != ',') and (i != '-'):
			big_word += i
print len(big_word)
