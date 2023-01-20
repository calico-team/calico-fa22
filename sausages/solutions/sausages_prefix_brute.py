def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Constructs a prefix sum for the number of sausage links with the low cut
    fixed at 1 and high cut at different positions. Then, check every possible
    low and high cut efficiently using differences of prefix sums.
    """
    max_H = max(H)
    prefix = [0] * (max_H + 1)
    for hi in range(1, max_H + 1):
        for i in range(N):
            if hi > L[i]:
                prefix[hi] += min(H[i], hi) - max(L[i], 1)
    
    for lo in range(1, max_H):
        for hi in range(lo + 1, max_H + 1):
            if prefix[hi] - prefix[lo] == K:
                return f'{lo} {hi}'

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
