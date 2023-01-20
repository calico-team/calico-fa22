def solve() -> None:
    """
    Communicate with the judge using a series of pulse queries and blast
    queries. Using P = 150 or fewer pulses, find Steve and blast them.
    
    You can send queries by calling the pulse(xp, yp) and blast(xb, yb)
    functions as defined below. If you miss your blast, your program will exit.
    """
    # YOUR CODE HERE
    return

def pulse(xp: float, yp: float) -> float:
    print('P', xp, yp, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return float(response)

def blast(xb1: float, yb1: float, xb2: float, yb2: float) -> None:
    print('B', xb1, yb1, xb2, yb2, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
