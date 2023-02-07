"""
Generates data for the problem.

To make this script work for your specific problem, set a seed, create a
TestCase class, and fill out the first four functions. Everything else is
handled by the template after the ######## separator.

Run this file in verbose mode with -v to see debug prints.
"""

import glob
import os
import random
import sys

from bottles_utils import *
import submissions.accepted.bottles_with_iterator as MODEL

DATA_DIR = 'data/'

def make_sample_tests():
	"""
	Make sample test files by creating lists of TestCase objects and calling
	make_test_file using them with the is_secret parameter set to False.
	Consider creating cases that helps build understanding of the problem, helps
	debugging, or possibly helps identify edge cases.
	"""
	SAMPLE_DIR = DATA_DIR + 'sample/'

	(jc.SetGen(SAMPLE_DIR, 0, True, '0_main_', 1)
	.write_file('1\n3\n5 1 2', 'Main sample'))

	(jc.SetGen(SAMPLE_DIR, 0, False, '1_bonus_', 1)
	.write_file('\n'.join([
		'2',
		'3',
		'2 1 1',
		'4',
		'2 2 1 1'
	]), 'Bonus sample'))

	make_ans(SAMPLE_DIR)

def make_secret_tests():
	"""
	Make secret test files by creating lists of TestCase objects and calling
	make_test_file using them with the is_secret parameter set to True. Consider
	creating edge cases as well as randomized cases.
	"""
	SECRET_DIR = DATA_DIR + 'secret/'

	sg_main = (jc.SetGen(SECRET_DIR, BOTTLES_SEED, True, '0_main_', 2)
	.write_file(BottlesMain(t_range = jc.r(1)), 'T = 1')
	.write_file(
		BottlesMain(t_range = jc.r(1), sum_range = jc.r(1)), 'T = N = 1'
	)
	.write_file('1\n1\n1', 'c_i = 1')
	.write_file(BottlesMain(t_range = jc.r(100)), 'T = 100')
	.write_file(
		BottlesMain(t_range = jc.r(1), sum_range = jc.r(1000)),
		'N = 1e3 (stress test and max bounds)'
	))
	for i in jc.r2(5):
		jc.SetGen.seed = f'{BOTTLES_SEED}_{i}'
		sg_main.write_file(BottlesMain(), f'Fully random main test (#{i})')

	sg_bonus = (jc.SetGen(SECRET_DIR, BOTTLES_SEED, False, '1_bonus_', 2)
	.write_file(BottlesBonus(t_range = jc.r(1)), 'T = 1')
	.write_file(
		BottlesBonus(t_range = jc.r(1), sum_range = jc.r(1)), 'T = N = 1'
	)
	.write_file('1\n1\n1', 'C_i = 1')
	.write_file(BottlesBonus(t_range = jc.r(100)), 'T = 100')
	.write_file(
		BottlesBonus(t_range = jc.r(1), sum_range = jc.r(10 ** 5)),
		'N = 1e5 (stress test)'
	)
	.write_file(
		jc.InputFile([[10 ** 9] * 10 ** 5]), 'N = 1e5, C_i = 1e9 (max bounds)'
	))
	for i in jc.r2(5):
		jc.SetGen.seed = f'{BOTTLES_SEED}_{i}'
		sg_bonus.write_file(
			BottlesBonus(c_range = jc.r2(100)),
			f'Random with high repetition of C_i (#{i})'
		)
	for i in jc.r2(5):
		jc.SetGen.seed = f'{BOTTLES_SEED}_{i}'
		sg_bonus.write_file(BottlesBonus(), f'Fully random #{i}')
	
	make_ans(SECRET_DIR)

def make_ans(directory):
	for file in glob.glob(f'{directory}/*'):
		if file.endswith('.in'):
			with open(file[:-3] + '.ans', 'w', newline = '\n') as ans_file:
				tmp_std = sys.stdin, sys.stdout
				sys.stdin = open(file, 'r')
				sys.stdout = ans_file
				MODEL.main()
				sys.stdin, sys.stdout = tmp_std

################################################################################

def main():
	"""
	Generate data.
	"""
	debug_print('Generating data...')
	make_dirs()
	delete_old_data()
	debug_print('Creating sample tests...')
	make_sample_tests()
	debug_print('Done creating sample tests!')
	debug_print('Creating secret tests...')
	make_secret_tests()
	debug_print('Done creating secret tests!')
	debug_print('Done generating data!')

def make_dirs():
	"""
	Make the sample and secret directories in the data directory to store our
	data if they do not already exist.
	"""
	debug_print('Creating directories...', end='')
	sample_path, secret_path = make_path(False), make_path(True)
	if not os.path.exists(sample_path):
		os.makedirs(sample_path)
	if not os.path.exists(secret_path):
		os.makedirs(secret_path)
	debug_print('Done!')

def delete_old_data():
	"""
	Delete old data if it exists so we can start generating with a clean slate
	or to save storage space.
	"""
	debug_print('Deleting old data...', end='')
	deleted = False
	for file in glob.glob(make_path(False, '*')):
		if os.path.exists(file):
			os.remove(file)
		deleted = True
	for file in glob.glob(make_path(True, '*')):
		if os.path.exists(file):
			os.remove(file)
		deleted = True
	debug_print('Done!' if deleted else 'Nothing to delete!')

def make_path(is_secret, file_name='', ext=None):
	"""
	Make the path for a file given its name, extension, and a flag for if this
	is sample or secret. The path is absolute based on the location of this
	file, not the location that ran the command to execute this file.
	"""
	relative_path = ''.join([
		'data/',
		'secret/' if is_secret else 'sample/',
		('secret_' if is_secret else 'sample_') if file_name else '',
		file_name,
		f'.{ext}' if ext else ''
	])
	return os.path.join(os.path.dirname(__file__), relative_path)

def debug_print(*args, **kwargs):
	"""
	Only print if the verbose argument is passed
	"""
	if len(sys.argv) > 1 and 'v' in sys.argv[1]:
		print(*args, **kwargs)

if __name__ == '__main__':
	main()
