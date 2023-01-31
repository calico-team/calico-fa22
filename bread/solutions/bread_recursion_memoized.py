def solve(N: int, K: int, D: int, B: list[int]) -> int:
    """
    Uses recursion (with memoization) to maximize the amount of bread
    that can be eaten with all swipes. Manually simulates the 
    effect of using a swipe.
    """
    seen = {}
    def most_bread(i, k):
        if i >= N or k <= 0:
            return 0
        
        if (i, k) in seen:
            return seen[(i, k)]
        
        amt_eaten = 0
        for j in range(i, min(i + D, N)):
            if B[j] == 0:
                break
            amt_eaten += B[j]
        
        best = max(most_bread(i + 1, k), most_bread(i + D, k - 1) + amt_eaten)
        seen[(i, k)] = best

        return best
    
    return most_bread(0, K)

def main():
    T = int(input())
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        print(solve(N, K, D, B))

if __name__ == '__main__':
    main()