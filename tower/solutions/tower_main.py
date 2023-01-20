def solve(N: int, P: list[int], D: list[int]) -> int:
    """
    Simulates going around the circle, beginning at every tower.
    This runs in O(N^2) time, only passing the main test set.
    """
    bestTime = 10 ** 8

    for start in range(N):
        totalTime = P[start]
        for i in range(N - 1):
            curTower = (start + i) % N
            totalTime += D[curTower]
            totalTime = max(totalTime, P[(curTower + 1) % N])
        bestTime = min(bestTime, totalTime)
    
    return bestTime

def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        N = int(line[0])

        line = input().split(' ')
        P = [int(x) for x in line]

        line = input().split(' ')
        D = [int(x) for x in line]

        print(solve(N, P, D))

if __name__ == '__main__':
    main()
