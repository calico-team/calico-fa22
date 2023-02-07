"""This solution solves the problem as if holds were not allowed."""

def solve(N: int, P: str) -> str:
	curr_bag, held_piece = None, None
	
	for piece in P:
		if not curr_bag:
			curr_bag = set('ZLOSIJT')
		
		if piece in curr_bag:
			curr_bag.remove(piece)
		else:
			return 'NO'
	return 'YES'

def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		P = input()
		print(solve(N, P))

if __name__ == '__main__':
	main()
