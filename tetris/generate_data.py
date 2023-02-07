"""
Generates data for the problem.

To make this script work for your specific problem, set a seed, create a
TestCase class, and fill out the first four functions. Everything else is
handled by the template after the ######## separator.

Run this file in verbose mode with -v to see debug prints.
"""

import glob
import os
import sys

from tetris_utils import *
import submissions.accepted.tetris_greedy as MODEL

def make_sample_tests():
	"""
	Make sample test files by creating lists of TestCase objects and calling
	make_test_file using them with the is_secret parameter set to False.
	Consider creating cases that helps build understanding of the problem, helps
	debugging, or possibly helps identify edge cases.
	"""
	jc.SetGen('data/sample', TETRIS_SEED, True).write_file(
		'\n'.join([
			'3',
			'3',
			'LIT',
			'14',
			'JOTLIZZJSOTLSO',
			'3',
			'LOL'
		]),
		'Sample'
	)
	
	make_ans('sample')

def make_secret_tests():
	"""
	Make secret test files by creating lists of TestCase objects and calling
	make_test_file using them with the is_secret parameter set to True. Consider
	creating edge cases as well as randomized cases.
	"""
	sg = jc.SetGen('data/secret', TETRIS_SEED, True, num_digits = 2)
	(
	sg.write_file(Tetris0(t_range = jc.r(1)), 'T = 1')
	.write_file('''1\n1\nT''', 'T = N = 1')
	.write_file(jc.InputFile([[p] for p in BAG]), 'N = 1 with all pieces')
	.write_file(Tetris0(t_range = jc.r(100)), 'T = 100')
	.write_file(
		Tetris0(t_range = jc.r(1), sum_range = jc.r(10 ** 5)),
		'N = 1e5 (stress test and max bounds #1)'
	)
	.write_file(
		jc.InputFile([''.join(BAG) * (10 ** 5 // 7)]),
		'Repeating same bag (max bounds #2)'
	)
	)
	K = 4
	for i in range(0, K + 1):
		hp = i / K
		sg.seed = f'{TETRIS_SEED}_{i}'
		sg.write_file(Tetris0(hold_prob = hp), f'P(hold) = {hp}')
	
	make_ans('secret')

def make_ans(secret_or_sample):
	for file in glob.glob(f'data/{secret_or_sample}/*'):
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
	for file in glob.glob('data/sample/*'):
		if os.path.exists(file):
			os.remove(file)
		deleted = True
	for file in glob.glob('data/secret/*'):
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