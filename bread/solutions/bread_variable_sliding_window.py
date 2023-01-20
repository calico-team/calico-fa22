def solve(N: int, K: int, D: int, B: list[int]) -> int:
    """
    Uses a two-pointers approach to more efficiently
    calculate how much bread can be eaten if you swiped
    on a given day.
    """   
    swipe_amts = []
    cur_amt = 0

    left_bound, right_bound = 0, 0
    while right_bound < min(N, left_bound + D) and B[right_bound] != 0:
        cur_amt += B[right_bound]
        right_bound += 1
    
    while left_bound < N:
        if left_bound == right_bound:
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

    return max(swipe_amts)

def main():
    T = int(input())
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        print(solve(N, K, D, B))

if __name__ == '__main__':
    main()
