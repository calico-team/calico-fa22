def solve(N: int, P: list[int], D: list[int]) -> int:
    '''
    Return the minimum number of hours needed to destroy all the towers in the circle.
    
    N: the number of towers in the circle
    P: the list of integers denoting the power level of each tower
    D: the list of integers denoting the distance to the next tower in the circle
    '''
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        N = int(line[0])

        line = input().split(' ')
        P = [int(x) for x in line]

        line = input().split(' ')
        D = [int(x) for x in line]

        print(solve(N, P, D))

if __name__ == '__main__':
    main()
