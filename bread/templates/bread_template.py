def solve(N: int, K: int, D: int, B: list[int]) -> int:
    """
    Find the maximum amount of bread you can eat before the semester ends, given 
    your available swipes.
    
    N: the number of days in the semester
    K: the number of meal cards you have
    D: the number of days a meal card will be activated for after swiping
    B: the list of integers denoting the number of bread loaves available 
       at the cafeteria on each day
    """
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        N, K, D = (int(x) for x in input().split())
        B = [int(x) for x in input().split()]
        print(solve(N, K, D, B))

if __name__ == '__main__':
    main()
