def solve(Y: int, N: str) -> str:
    """
    Determine if the RSO name for an entry is valid. Return True if it is and
    return False otherwise.
    
    Y: the year the RSO was established
    N: the name the RSO registered with
    """
    # YOUR CODE HERE
    return False

def main():
    T = int(input())
    for _ in range(T):
        Y = int(input())
        N = input()
        print('VALID' if solve(Y, N) else 'INVALID')

if __name__ == '__main__':
    main()
