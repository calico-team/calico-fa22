def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Determine if a cut exists that yields exactly K sausage links. If such a cut
    exists, return any "c1 c2" where c1 and c2 are the heights of the cut. If
    such a cut is not possible, return "IMPOSSIBLE".
    
    N: the number of sausage chains
    K: the target number of sausage links
    H: a list of the heights of the top of each sausage chain
    L: a list of the heights of the bottom of each sausage chain
    """
    # YOUR CODE HERE
    return 'IMPOSSIBLE'

def main():
    T = int(input())
    for _ in range(T):
        NK = input().split(' ')
        N, K = int(NK[0]), int(NK[1])
        H = [int(i) for i in input().split(' ')]
        L = [int(i) for i in input().split(' ')]
        print(solve(N, K, H, L))

if __name__ == '__main__':
    main()
