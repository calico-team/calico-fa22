def solve(H: int, W: int, D: int, base: list[list[str]]) -> None:
    """
    Output the image created by extruding the base with height H and width W to
    a depth of D.
    
    H: the height of the base
    W: the width of the base
    D: the depth to extrude the base to
    base: a matrix of characters representing the base itself
    """
    # YOUR CODE HERE
    return

def main():
    T = int(input())
    for _ in range(T):
        H, W, D = (int(i) for i in input().split(' '))
        base = [list(input()) for _ in range(H)]
        solve(H, W, D, base)

if __name__ == '__main__':
    main()
