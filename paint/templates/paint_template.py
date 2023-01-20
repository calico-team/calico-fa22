def solve(W: int, O: int, B: int, Cow: int, Cbo: int, Cbw: int) -> int:
    """
    Return the minimum cost to convert all of the paint into a single color.
    
    W: non-negative number of buckets of white paint
    O: non-negative number of buckets of orange paint
    B: non-negative number of buckets of brown paint
    Cow: positive cost to convert between a bucket of orange and white paint
    Cbo: positive cost to convert between a bucket of brown and orange paint
    Cbw: positive cost to convert between a bucket of brown and white paint
    """
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        W, O, B = int(line[0]), int(line[1]), int(line[2])
        Cow, Cbo, Cbw = int(line[3]), int(line[4]), int(line[5])
        print(solve(W, O, B, Cow, Cbo, Cbw))

if __name__ == '__main__':
    main()
