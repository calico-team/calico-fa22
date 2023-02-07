"""
Deletes data or zips.

Run this file in verbose mode with -d to delete data and -z to delete zips. You
can also run this file in verbose mode with -v to see debug prints.

Flags can also be combined, for example, to delete data with debug prints: -dv.
"""

import sys

import generate_zips

def main():
	destroyed = False
	if len(sys.argv) > 1 and 'd' in sys.argv[1]:
		if generate_zips.USE_GENERATE_DATA_SCRIPT:
			import generate_data
			generate_data.delete_old_data()
			destroyed = True
		else:
			print('Unable to delete data because USE_GENERATE_DATA_SCRIPT is False.')
	if len(sys.argv) > 1 and 'z' in sys.argv[1]:
		generate_zips.delete_old_zips()
		destroyed = True
		
	if not destroyed:
		print('Deleted nothing. Use -d to delete data and -z to delete zips.')

if __name__ == '__main__':
	main()
