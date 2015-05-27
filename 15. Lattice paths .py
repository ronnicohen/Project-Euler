# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2*2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# *** uncopiable drawings here
#
#
# How many such routes are there through a 20*20 grid?

def options(squarei):
	rowo = squarei[0] - 1
	col = squarei[1] - 1
	paths = 0
	if grid[rowo + 1][col][2] == 0:
		paths += 1
	else:
		paths += grid[rowo + 1][col][2]
	if grid[rowo][col + 1][2] == 0:
		paths += 1
	else:
		paths += grid[rowo][col + 1][2]
	return paths


square = [None, None]
grid = []
from copy import deepcopy
for i in xrange(0, 20):
	row = []
	for j in xrange(0, 20):
		row.append(deepcopy(square))
	grid.append(deepcopy(row))
curr_r = 1
for i in grid:
	curr_c = 1
	for j in i:
		j[1] = curr_c
		j[0] = curr_r
		curr_c += 1
	curr_r += 1
for i in grid:
	i[-1].append(0)
for i in grid[-1]:
	i.append(0)
for i in xrange(18, 0, -1):
	for j in xrange(18, -1, -1):
		grid[j][i].append(options(grid[j][i]))
final = grid[0][1][2] * 2
print 'There are: ' + str(final) + ' ' + 'possible routes in a 20*20 grid'




