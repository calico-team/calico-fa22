def solve(W: int, O: int, B: int, Cow: int, Cbo: int, Cbw: int) -> int:
    """
    Compares the costs to convert all of the paint to each color (directly and indirectly).
    Returns the minimum cost, in overall constant time.
    """
    to_W = O * min(Cow, Cbo + Cbw) + B * min(Cbw, Cow + Cbo)
    to_O = W * min(Cow, Cbo + Cbw) + B * min(Cbo, Cbw + Cow)
    to_B = W * min(Cbw, Cow + Cbo) + O * min(Cbo, Cbw + Cow)
    return min(to_W, to_O, to_B)

def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        W, O, B = int(line[0]), int(line[1]), int(line[2])
        Cow, Cbo, Cbw = int(line[3]), int(line[4]), int(line[5])
        print(solve(W, O, B, Cow, Cbo, Cbw))

if __name__ == '__main__':
    main()
