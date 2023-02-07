"""
A version of the solution using Python's iterators. The logic begins to deviate
significantly from the main solution; as a result, the lines of code are very
few, but each line is more dense. Note that every non-comment line in the
function body uses a list comprehension. In C++ or Java, a separate loop would
likely be used instead.
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
	unfixed = (i for _, i in a if a[i][0] != C[i]) # Most tricky line
	perm = [j if p[0] == C[j] else next(unfixed) for j, p in enumerate(a)]
	print(*[x + 1 for x in perm])

def main ():
	T = int(input())
	for _ in range(T):
		N = int(input())
		C = [int(C_i) for C_i in input().split()]
		solve(N, C)

if __name__ == '__main__':
	main()