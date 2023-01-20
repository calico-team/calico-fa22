def solve(N: int, K: int, D: int, B: list[int]) -> int:
    """
    Tries all possible start days to use your one swipe,
    simulating each possibility to count the amount of bread
    eaten.
    """   
    cur_best = -float('inf')
    for start_day in range(N):
        amt_eaten = 0
        for i in range(start_day, min(start_day + D, N)):
            if B[i] == 0:
                break
            amt_eaten += B[i]
        
        cur_best = max(cur_best, amt_eaten)
    
    return cur_best

def main():
    T = int(input())
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        print(solve(N, K, D, B))

if __name__ == '__main__':
    main()
