import re

VALID_SYLLABLES = re.compile(r'^([ptkmnlswj]?[aeiou]n?)+$')
ILLEGAL_SEQUENCES = re.compile(r'w[uo]|[jt]i|n[mn]|[aeiou]{2}')

def solve(W: str) -> str:
    """
    Checks W against a regex to see if it only uses valid syllables and against
    another to see if it contains any illegal sequences.
    """
    if VALID_SYLLABLES.search(W) and not ILLEGAL_SEQUENCES.search(W):
        return 'pona'
    else:
        return 'ike'

def main():
    T = int(input())
    for _ in range(T):
        W = input()
        print(solve(W))

if __name__ == '__main__':
    main()
