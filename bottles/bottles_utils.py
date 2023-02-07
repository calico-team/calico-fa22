import jewato_gen as jc
import random

BOTTLES_SEED = 'b0T7lE5'

class Bottles (jc.MultiTestFile):
	def __init__ (
		self,
		t_range: range,
		sum_range: range,
		c_range: range,
		replace: bool
	):
		"""
		t_range -- inherited from `jewato_gen.py`
		sum_range -- inherited from `jewato_gen.py`
		[max(`sum_range.start`, T), `sum_range.stop`). Each N is then selected
		from a random integer partition of `sum_n` into T summands.
		c_range -- all capacities c_i are randomly selected from `c_range`
		replace -- whether replacement occurs when selecting capacities
		"""
		assert t_range.start > 0 and t_range.stop <= 101
		assert c_range.start > 0
		super().__init__([], t_range, sum_range)
		for n in self.partition:
			if replace:
				self.data.append(random.choices(c_range, k = n))
			else:
				self.data.append(random.sample(c_range, n))

class BottlesMain (Bottles):
	def __init__ (
		self,
		t_range: range = jc.r2(100),
		sum_range: range = jc.r2(10 ** 3),
		c_range: range = jc.r2(10 ** 3)
	):
		"""Forced to select without replacement."""
		assert sum_range.stop <= 10 ** 3 + 1
		assert c_range.stop <= 10 ** 3 + 1
		assert len(c_range) >= sum_range.stop - 1, 'too few distinct c values'
		super().__init__(t_range, sum_range, c_range, False)

class BottlesBonus (Bottles):
	def __init__ (
		self,
		t_range: range = jc.r2(100),
		sum_range: range = jc.r2(10 ** 5),
		c_range: range = jc.r2(10 ** 9)
	):
		"""Tests with replacement should be harder than tests without
		replacement. A few manually created input files can cover exceptions."""
		assert sum_range.stop <= 10 ** 5 + 1
		assert c_range.stop <= 10 ** 9 + 1
		super().__init__(t_range, sum_range, c_range, True)