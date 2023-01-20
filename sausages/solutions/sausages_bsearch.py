def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Checks every possible low cut, and binary searches for a high cut that
    achieves the target. In each iteration, compute the amount of sausage in
    between by scanning all the sausages.
    """
    max_H = max(H)
    for lo in range(1, max_H):
        lower_bound, upper_bound = lo + 1, max_H
        while lower_bound <= upper_bound:
            hi = (lower_bound + upper_bound) // 2
            
            total_sausages = 0
            for i in range(N):
                if H[i] > lo and L[i] < hi:
                    total_sausages += min(H[i], hi) - max(L[i], lo)
            if total_sausages == K:
                return f'{lo} {hi}'
            
            if total_sausages < K:
                lower_bound = hi + 1
            else:
                upper_bound = hi - 1
    
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
