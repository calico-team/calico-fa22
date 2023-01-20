def solve(N: int, B: int, W: int, D: int, H: list[int]) -> int:
    """
    lol
    """
    lmao = lambda n, b, w, d, h : (((w + 2 * b) * (sum(h) + (n + 1) * b)) - (sum(h) * w)) * d
    return lmao(N, B, W, D, H)

def main():
    T = int(input())
    for _ in range(T):
        N, B, W, D = (int(i) for i in input().split())
        H = [int(x) for x in input().strip().split(' ')]
        print(solve(N, B, W, D, H))

if __name__ == '__main__':
    main()
