def solve (N: int, C: list[int]):
    """
    Output the minimum total wait time on the first line.
    Output the optimal new permutation on the second line.
    
    N: the number of students in line
    C: the list of the bottle capacities, in liters, for each student
    """
    # YOUR CODE HERE

def main ():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = [int(C_i) for C_i in input().split()]
        solve(N, C)

if __name__ == '__main__':
    main()