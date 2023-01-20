def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Constructs a prefix sum for the number of sausage links with the low cut
    fixed at 1 and high cut at different positions. Then, use two pointers to
    search the range of all heights for a cut that achieves the target.
    """
    max_H = max(H)
    prefix = [0] * (max_H + 1)
    for hi in range(1, max_H + 1):
        for i in range(N):
            if hi > L[i]:
                prefix[hi] += min(H[i], hi) - max(L[i], 1)
    
    lo, hi = 1, 2
    while hi <= max_H:
        total_sausages = prefix[hi] - prefix[lo]
        if total_sausages == K:
            return f'{lo} {hi}'
        elif total_sausages < K:
            hi += 1
        else:
            lo += 1

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
