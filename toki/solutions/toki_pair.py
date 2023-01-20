import sys

sys.setrecursionlimit(100000)

CONSONANTS, VOWELS, ILLEGALS = 'mnptkswjl', 'aeiou', 'wu wo ji ti nn nm'

def solve(W: str) -> str:
    """
    Considers if W is a valid syllable or if W can be broken into two valid
    syllables after first checking for illegal sequences.
    """
    for i in range(len(W) - 1):
        if W[i:i + 2] in ILLEGALS or W[i] in VOWELS and W[i + 1] in VOWELS:
            return 'ike'
    
    if is_valid_syllable(W):
        return 'pona'
    
    for i in range(len(W)):
        left, right = W[:i], W[i:]
        if is_valid_syllable(left) and is_valid_syllable(right):
            return 'pona'

    return 'ike'

def is_valid_syllable(s):
    if len(s) == 1:
        return s in VOWELS
    elif len(s) == 2:
        return s[0] in CONSONANTS and s[1] in VOWELS or \
               s[0] in VOWELS and s[1] == 'n'
    elif len(s) == 3:
        return s[0] in CONSONANTS and s[1] in VOWELS and s[2] == 'n'
    else:
        return False

def main():
    T = int(input())
    for _ in range(T):
        W = input()
        print(solve(W))

if __name__ == '__main__':
    main()
