def solve(N: int, B: int, W: int, D: int, H: list[int]) -> int:
    """
    Adds together the volume of the boards needed to
    create the shelf.
    """
    shelf_board_volume = B * W * D
    total_shelf_volume = (N + 1) * shelf_board_volume

    bookshelf_height = sum(H) + B * (N + 1)
    side_board_volume = bookshelf_height * B * D
    total_side_volume = 2 * side_board_volume

    return total_shelf_volume + total_side_volume

def main():
    T = int(input())
    for _ in range(T):
        N, B, W, D = (int(i) for i in input().split())
        H = [int(x) for x in input().strip().split(' ')]
        print(solve(N, B, W, D, H))

if __name__ == '__main__':
    main()
