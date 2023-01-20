def solve(N: int, P: str) -> bool:
    """
    Return True if the sequence of placed pieces is possible and False if it's
    impossible.
    
    N: the number of placed pieces
    P: the recorded sequence of placed pieces
    """
    # YOUR CODE HERE
    return False

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = input()
        print('YES' if solve(N, P) else 'NO')

if __name__ == '__main__':
    main()
