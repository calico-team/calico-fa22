def solve(H: int, W: int, D: int, base: list[list[str]]) -> None:
    """
    Creates the output image by naively drawing every slash of every edge.
    """
    image = [[' ' for i in range(D + W + 1)] for i in range(D + H + 1)]
    
    for i in range(H):
        for j in range(W):
            image[i][j] = base[i][j]
    
    corners = []
    for i in range(H):
        for j in range(W):
            if base[i][j] == '+':
                corners.append((i, j))
    for corner in corners:
        corner_row, corner_col = corner
        for i in range(1, D + 1):
            image[corner_row + i][corner_col + i] = '\\'
    
    for i in range(H):
        for j in range(W):
            if base[i][j] != ' ':
                image[i + D + 1][j + D + 1] = base[i][j]
    
    for i in range(H + D + 1):
        print(''.join(image[i]))

def main():
    T = int(input())
    for _ in range(T):
        H, W, D = (int(i) for i in input().split(' '))
        base = [list(input()) for _ in range(H)]
        solve(H, W, D, base)

if __name__ == '__main__':
    main()
