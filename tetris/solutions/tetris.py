def solve(N: int, P: str) -> bool:
    """
    Simulates the process of placing the sequence while considering the set of
    all pieces in the current bag that have yet to be placed and also the held
    piece. Use process of elimination to figure out what piece was held when we
    find a sequence that would normally be impossible without holds.
    """
    curr_bag = set()
    held_piece = None
    
    for piece in P:
        if not curr_bag:
            curr_bag.update('ZLOSIJT')
        
        if piece in curr_bag:
            curr_bag.remove(piece)
        else:
            if not held_piece and len(curr_bag) == 1:
                held_piece = curr_bag.pop()
                curr_bag.update('ZLOSIJT')
                curr_bag.remove(piece)
            elif held_piece == piece:
                held_piece = None
            else:
                return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = input()
        print('YES' if solve(N, P) else 'NO')

if __name__ == '__main__':
    main()
