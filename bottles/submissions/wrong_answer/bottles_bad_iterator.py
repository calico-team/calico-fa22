"""
This is a program very similar to bottles_with_iterator.py that is wrong
because of a mistake on the most tricky line.
"""

def solve (N: int, C: list[int]):
	"""
	Output the minimum total wait time on the first line.
	Output the optimal new permutation on the second line.
	
	N: the number of students in line
	C: the list of the bottle capacities, in liters, for each student
	"""
	# Initial sort
	a = sorted([t[::-1] for t in enumerate(C)]) # `a` for array, `t` for tuple

	# Output total wait time
	print(sum([p[0] * (N - j) for j, p in enumerate(a)])) # `p` for pair

	# Output new permutation
	# The iterator construction (the most tricky line) below is wrong. Simply
	# inverting the inclusion criteria for `is_fixed` and taking the student
	# number is incorrect: the capacities at an index in `a` have been scrambled
	# for unplaced students.
	unfixed = (p[1] for j, p in enumerate(a) if p[0] != C[j])
	# The program would get AC if the line were replaced with the one below.
	# unfixed = (p[1] for j, p in enumerate(a) if a[p[1]][0] != C[p[1]])
	perm = [j if p[0] == C[j] else next(unfixed) for j, p in enumerate(a)]
	print(' '.join([str(x + 1) for x in perm]))

def main ():
	T = int(input())
	for _ in range(T):
		N = int(input())
		C = [int(C_i) for C_i in input().split()]
		solve(N, C)

if __name__ == '__main__':
	main()