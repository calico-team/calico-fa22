def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Begin by using a line sweep to find the change in running sausages at each
    endpoint. Then, use two pointers to go over all possible cut heights.
    """
    endpoints = [(l, 1) for l in L] + [(h, -1) for h in H]
    endpoints.sort()
    
    lo = hi = 1
    lo_ptr = hi_ptr = 0
    lo_delta = hi_delta = 0
    total = 0
    while hi <= endpoints[-1][0]:
        if total == K:
            return f'{lo} {hi}'
        elif total < K:
            while hi_ptr < len(endpoints) and hi == endpoints[hi_ptr][0]:
                hi_delta += endpoints[hi_ptr][1]
                hi_ptr += 1
            total += hi_delta
            hi += 1
        else:
            while lo_ptr < len(endpoints) and lo == endpoints[lo_ptr][0]:
                lo_delta += endpoints[lo_ptr][1]
                lo_ptr += 1
            total -= lo_delta
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
