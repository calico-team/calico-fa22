import jewato_gen as jc
import random

TETRIS_SEED = '7ETr1S'

BAG = list('ZLOSIJT')
def bag_randomizer ():
	"""Generator function that simulates an infinite series of randomized bags
	and yields individual pieces from them
	"""
	bag_perm = BAG[:]
	while True:
		random.shuffle(bag_perm)
		for p in bag_perm:
			yield p

class Tetris (jc.MultiTestFile):
	def __init__ (
		self,
		t_range: range,
		sum_range: range,
		hold_prob: float,
		mutate_prob: float
	):
		"""t_range: Inherited from `jewato_gen.py`
		sum_range: Inherited from `jewato_gen.py`
		hold_prob: Each piece independently has this probability of being held
		after coming from the bag
		mutate_prob: Each piece independently has this probability of being
		replaced with a random other piece in the final sequence
		"""
		assert t_range.start > 0 and t_range.stop <= 101
		assert sum_range.start > 0 and sum_range.stop <= 10 ** 5 + 1
		assert 0 <= hold_prob <= 1
		assert 0 <= mutate_prob <= 1
		super().__init__([], t_range, sum_range)
		for n in self.partition:
			seq = ''
			hold = None
			randomizer = bag_randomizer()
			while len(seq) < n:
				cur = next(randomizer)
				nxt_piece = ''
				if random.random() < hold_prob:
					if hold:
						nxt_piece = hold
					hold = cur
				else:
					nxt_piece = cur
				if nxt_piece and random.random() < mutate_prob:
					nxt_piece = random.choice(BAG)
				seq += nxt_piece
			self.data.append(seq)

class Tetris0 (Tetris):
	def __init__ (
		self,
		t_range: range = range(1, 101),
		sum_range: range = range(1, 10 ** 5),
		hold_prob: float = 0.5,
		mutate_prob: float = 1e-3
	):
		super().__init__(t_range, sum_range, hold_prob, mutate_prob)