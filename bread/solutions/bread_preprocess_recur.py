import sys
sys.setrecursionlimit(10 ** 6)

def solve(N: int, K: int, D: int, B: list[int]) -> int:
    """
    Uses the two-pointer approach to preprocess how much
    bread can be eaten from any given swipe, using that
    information to speed up the recursion used to maximize
    bread eaten with all swipes.
    """   
    def preprocess_swipe_amts():
        swipe_amts = []
        cur_amt = 0

        left_bound, right_bound = 0, 0
        while right_bound < min(N, left_bound + D) and B[right_bound] != 0:
            cur_amt += B[right_bound]
            right_bound += 1
        
        while left_bound < N:
            if left_bound == right_bound:
                assert cur_amt == 0
                swipe_amts.append(cur_amt)
                left_bound += 1
                right_bound += 1

                while right_bound < min(N, left_bound + D) and B[right_bound] != 0:
                    cur_amt += B[right_bound]
                    right_bound += 1
                
                continue
            
            swipe_amts.append(cur_amt)
            cur_amt -= B[left_bound]
            left_bound += 1

            if right_bound < N and B[right_bound] != 0:
                cur_amt += B[right_bound]
                right_bound += 1

        return swipe_amts
    
    swipe_amts = preprocess_swipe_amts()

    cache = {}
    def most_bread_from(start, swipes):
        if start >= N or swipes == 0:
            return 0
        if (start, swipes) in cache:
            return cache[(start, swipes)]
        
        best = max(
            most_bread_from(start + D, swipes - 1) + swipe_amts[start],
            most_bread_from(start + 1, swipes)
        )

        cache[(start, swipes)] = best
        return best
    
    return most_bread_from(0, K)

def main():
    T = int(input())
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        print(solve(N, K, D, B))

if __name__ == '__main__':
    main()
