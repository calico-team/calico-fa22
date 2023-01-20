def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Using brute force to checking every possible low and high cut, and for each
    cut, compute the amount of sausage in between by scanning all the sausages.
    """
    max_H = max(H)
    for lo in range(1, max_H):
        for hi in range(lo + 1, max_H + 1):
            total_sausages = 0
            for i in range(N):
                if lo < H[i] and hi > L[i]:
                    total_sausages += min(H[i], hi) - max(L[i], lo)
            if total_sausages == K:
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
