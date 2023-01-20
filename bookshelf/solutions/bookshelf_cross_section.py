def solve(N: int, B: int, W: int, D: int, H: list[int]) -> int:
    """
    Finds the volume by subtracting out the empty shelf space from
    the volume of the rectangular prism occupied by the shelf.
    """
    bookshelf_width = 2 * B + W
    bookshelf_height = sum(H) + (N + 1) * B
    shelf_space = sum(H) * W

    cross_section_area = bookshelf_width * bookshelf_height - shelf_space
    return cross_section_area * D

def main():
    T = int(input())
    for _ in range(T):
        N, B, W, D = (int(i) for i in input().split())
        H = [int(x) for x in input().strip().split(' ')]
        print(solve(N, B, W, D, H))

if __name__ == '__main__':
    main()
