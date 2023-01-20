def solve(H: int, W: int, D: int, base: list[list[str]]) -> None:
    """
    Creates the output image by drawing edges on each diagonal. When a corner
    is found, keep track of how many more slashes to draw for that edge. When
    an intersection is found with an upcoming edge, reset the number of
    slashes.
    """
    image = [[' ' for _ in range(D + W + 1)] for _ in range(D + H + 1)]
    
    for i in range(H):
        for j in range(W):
            image[i][j] = base[i][j]
    
    for d in range(-W + 1, H):
        i = max(0, d)
        j = i - d
        slashesToDraw = 0;
        while i < H + D + 1 and j < W + D + 1:
            if slashesToDraw > 0:
                image[i][j] = '\\'
                slashesToDraw -= 1
            if i < H and j < W and base[i][j] == '+':
                slashesToDraw = D
            i += 1
            j += 1 
    
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
