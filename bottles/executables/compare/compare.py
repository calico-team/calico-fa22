import sys

def main ():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
        exit(1)
    _, test_in_path, test_out_path = sys.argv
    
    try:
        with open(test_in_path, 'r') as test_in:
            with open(test_out_path, 'r') as test_out:
                compare(test_in, test_out)
    except IOError:
        print('Failed to open test input')
        exit(1)

cnt_fixed = lambda perm: sum(j + 1 == p for j, p in enumerate(perm))

def compare (test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):
        N = int(read_file(test_in))
        C = [int(i) for i in read_file(test_in).split()]
        
        ref_total = int(read_file(test_out))
        ref_perm = [int(i) for i in read_file(test_out).split()]
        
        submitted_total = read()
        if submitted_total.isdigit():
            submitted_total = int(submitted_total)
            if submitted_total != ref_total:
                print(f'Test #{case}: the given total wait time is not minimal')
        else:
            print(f'Test #{case}: total wait time is not a positive integer')
        
        submitted_perm = read()
        if len(submitted_perm.split()) != len(ref_perm):
            print(f'Test #{case}: permutation has wrong length')
            continue
        submitted_perm = submitted_perm.split()
        
        if not all(A_i.isdigit() for A_i in submitted_perm):
            print(f'Test #{case}: some permutation values are not'
                'positive integers')
            continue
        submitted_perm = [int(Ai) for Ai in submitted_perm]
        
        if sorted(submitted_perm) != sorted(ref_perm):
            print(f'Test #{case}: index list is not a permutation of length N')
            continue
        
        submitted_perm_total = sum(
            [C[x - 1] * (N - i) for i, x in enumerate(submitted_perm)]
        )
        total_diff = submitted_perm_total - ref_total

        if total_diff > 0:
            print(f'Test #{case}: total wait time is not minimal')
            continue
        if total_diff < 0:
            print(f'Test #{case}: submitted total less than reference.'
                'The reference output is wrong.')
            exit(1)
        
        fixed_diff = cnt_fixed(submitted_perm) - cnt_fixed(ref_perm)
        if fixed_diff < 0:
            print(f'Test #{case}: fixed students not maximized')
            continue
        if fixed_diff > 0:
            print(f'Test #{case}: submitted fixed students more than reference.'
                'The reference output is wrong.')
            exit(1)
    
    try:
        temp = ''
        while not temp:
            temp = input().strip()
        print('Trailing output when judge expected no more output')
    except:
        pass

def read_file (file):
    try:
        return file.readline().strip()
    except EOFError:
        print('End of test input while judge expected more input')
        exit(1)

def read ():
    try:
        return input().strip()
    except EOFError:
        print('End of output while judge expected more output')
        exit()

if __name__ == '__main__':
    main()
