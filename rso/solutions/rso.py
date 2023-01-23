def solve(Y: int, N: str) -> str:
    """
    Fails if the name exceeds the length guideline, or
    starts with a trademarked word while being established
    after 2010.
    """    
    if len(N) > 50:
        return False
    
    N = N.lower()
    list_of_words = N.split(' ')
    first_word = list_of_words[0]

    has_california = first_word == 'california'
    has_cal = first_word == 'cal'
    has_berkeley = first_word == 'berkeley'
    
    if Y >= 2010 and (has_california or has_cal or has_berkeley):
        return False
    
    return True

def main():
    T = int(input())
    for _ in range(T):
        Y = int(input())
        N = input()
        print('VALID' if solve(Y, N) else 'INVALID')

if __name__ == '__main__':
    main()
