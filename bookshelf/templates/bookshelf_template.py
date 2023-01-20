def solve(N: int, B: int, W: int, D: int, H: list[int]) -> int:
    """
    Find the total volume of wood needed to construct the given bookshelf design.

    N: the number of shelves in the bookshelf
    B: the thickness of the boards, in inches
    W: the width of the shelves, in inches
    D: the depth of the bookshelf, in inches
    H: the list of integers denoting the height of each of the bookshelf’s shelves, in inches
    """
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        N, B, W, D = (int(i) for i in input().split())
        H = [int(x) for x in input().strip().split(' ')]
        print(solve(N, B, W, D, H))

if __name__ == '__main__':
    main()
