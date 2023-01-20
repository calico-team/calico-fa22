def solve (N: int, C: list[int]):
    """
    Output the minimum total wait time on the first line.
    Output the optimal new permutation on the second line.
    
    N: the number of students in line
    C: the list of the bottle capacities, in liters, for each student
    """
    # Initial sort
    a = sorted([t[::-1] for t in enumerate(C)]) # `a` for array, `t` for tuple

    # Output total wait time
    print(sum([p[0] * (N - j) for j, p in enumerate(a)])) # `p` for pair

    # Output new permutation
    is_fixed = [p[0] == C[i] for i, p in enumerate(a)]
    j = 0
    for k in range(N):
        if is_fixed[k]:
            print(k + 1, end = ' ')
        else:
            while is_fixed[a[j][1]]:
                j += 1
            print(a[j][1] + 1, end = ' ')
            j += 1
    print()

def main ():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = [int(C_i) for C_i in input().split()]
        solve(N, C)

if __name__ == '__main__':
    main()