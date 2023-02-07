"""
Generates zip files following the DomJudge zip file format.

To make this script work for your specific problem, fill out the global
variables and the first two functions. Everything else is handled by the
template after the ######## separator.

Run this file in verbose mode with -v to see debug prints.
"""

import os
import sys
import zipfile

"""
Set this to True if you generate data with generate_data.py. When set to true,
the script runs generate_data.py to re-generate the latest data before zipping.
When set to False, the script only zips the data it finds in the data folder.
"""
USE_GENERATE_DATA_SCRIPT = True

"""
Set this string to be the short name of the problem. Names must only use
lowercase letters and digits. A good name should be memorable and unique across
all contests.
"""
PROBLEM_NAME = 'bottles'

"""
Set this int to be the time limit in seconds. Typically this is 1 but feel free
to adjust as necessary for your problem.
"""
TIME_LIMIT = 1

"""
Set this list to be a list of strings containing the names of every test set.
The script will generate a zip for each test set. The filter functions below
should only return names from this list.
"""
TEST_SET_NAMES = ['main', 'bonus']

def filter_data_file_name(file_name):
	"""
	Return a collection of test set names that the data file with the provided
	file name should belond to.
	
	this data file should belong to.
	The data file will be added to every test with those names.
	"""
	if 'bonus' in file_name:
		return 'bonus'
	else:
		return 'main', 'bonus'

def filter_submissions_file_name(file_name):
	"""
	Return a collection of test set names that this submission file should
	belong to. The submission file will be added to every test with those names.
	"""
	main_only, bonus_only, both = 'main', 'bonus', ('main', 'bonus')
	files = {
		'bottles_main_only.cpp': main_only,
		'bottles_with_iterator.py': both,
		'bottles.cpp': both,
		'bottles.py': both,
		
		'bottles_slow_total.cpp': bonus_only,
		
		'bottles_bad_fixing.cpp': bonus_only,
		'bottles_bad_iterator.py': bonus_only,
		'bottles_no_tiebreak.cpp': bonus_only
	}
	return files[file_name] if file_name in files else []

################################################################################

def main():
	"""
	Generate zips
	"""
	if USE_GENERATE_DATA_SCRIPT:
		import generate_data
		generate_data.main()
	debug_print('Generating zips...')
	delete_old_zips()
	make_zips()
	debug_print('Done generating zips!')

def delete_old_zips():
	"""
	Delete old zips if they exist so we can start generating with a clean slate
	or to save storage space.
	"""
	debug_print('Deleting old zips...', end='')
	deleted = False
	for test_set_name in TEST_SET_NAMES:
		zip_file_name = make_zip_file_path(test_set_name)
		if os.path.exists(zip_file_name):
			os.remove(zip_file_name)
			deleted = True
	debug_print('Done!' if deleted else 'Nothing to delete!')

def make_zips():
	"""
	Create a zip for each test set. Each test set consists of data, submissions,
	and the DomJudge metadata file.
	"""
	for test_set_name in TEST_SET_NAMES:
		debug_print(f'Creating test set zip "{test_set_name}"...')
		file_name = make_zip_file_path(test_set_name)
		with zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
			zip_path(zip_file, 'data', test_set_name, filter_data_file_name)
			zip_path(zip_file, 'submissions', test_set_name, filter_submissions_file_name)
			zip_domjudge_problem_ini(zip_file, test_set_name)
		debug_print(f'Done creating test set zip "{test_set_name}"!')

def make_zip_file_path(test_set_name):
	"""
	Make the path for a zip file given the name of the test set and the DomJudge
	metadata name. The path is absolute based on the location of this file, not
	the location that ran the command to execute this file.
	"""
	relative_path = f'{PROBLEM_NAME}_{test_set_name}.zip'
	return os.path.join(os.path.dirname(__file__), relative_path)

def zip_path(zip_file, relative_path, test_set_name, filter_func):
	"""
	Add all files in the relative_path relative to this file's path into the
	zip_file with the test_set_name. Only files that the filter_func says are to
	be added to the current test_set_name will be added.
	"""
	debug_print(f'Zipping directory "{relative_path}" for test set "{test_set_name}"...', end='')
	path = os.path.join(os.path.dirname(__file__), relative_path)
	for root, dirs, files in os.walk(path):
		for file in files:
			if test_set_name in filter_func(file):
				file_path = os.path.join(root, file)
				zip_path = os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
				zip_file.write(file_path, zip_path)
	debug_print('Done!')

def zip_domjudge_problem_ini(zip_file, test_set_name):
	"""
	Add the domjudge metadata file to the zip_file with the test_set_name. This
	function creates the file, writes the data in DOMJUDGE_METADATA to it, adds
	it to the zip, then deletes it.
	"""
	debug_print(f'Zipping domjudge metadata for test set "{test_set_name}"...', end='')
	meta_path = os.path.join(os.path.dirname(__file__), 'domjudge-problem.ini')
	with open(meta_path, 'w') as meta_file:
		print(f'name=*{PROBLEM_NAME}_{test_set_name}', file=meta_file)
		print(f'timelimit={TIME_LIMIT}', file=meta_file)
		print(f'special_compare=\'bottles_compare\'', file=meta_file)
	
	zip_file.write(meta_path, 'domjudge-problem.ini')
	os.remove(meta_path)
	debug_print('Done!')

def debug_print(*args, **kwargs):
	"""
	Only print if the verbose argument is passed
	"""
	if len(sys.argv) > 1 and 'v' in sys.argv[1]:
		print(*args, **kwargs)

if __name__ == '__main__':
	main()
