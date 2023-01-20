import functools
import sys

sys.setrecursionlimit(100000)

CONSONANTS, VOWELS, ILLEGALS = 'mnptkswjl', 'aeiou', 'wu wo ji ti nn nm'

def solve(W: str) -> str:
    """
    Uses top-down dynamic programming to check the syllable structure, after
    first checking for illegal sequences.
    """    
    for i in range(len(W) - 1):
        if W[i:i + 2] in ILLEGALS or W[i] in VOWELS and W[i + 1] in VOWELS:
            return 'ike'
    
    @functools.cache
    def dp(i):
        """
        Returns True if and only if W[i:] has a valid syllable structure.
        """
        if i == len(W):
            return True
        elif i > len(W):
            return False
        else:
            return is_valid_syllable(W[i:i + 1]) and dp(i + 1) or \
                   is_valid_syllable(W[i:i + 2]) and dp(i + 2) or \
                   is_valid_syllable(W[i:i + 3]) and dp(i + 3)
    return 'pona' if dp(0) else 'ike'

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
