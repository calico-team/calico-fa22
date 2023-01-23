import math

def solve(N: int, P: list[int], D: list[int]) -> int:
    """
    Precomputes the walking and waiting times for every power of 2 length arc.
    Uses these precomputed arcs to simulate each starting point in O(log N) time.
    This runs in O(N log N) time, passing the bonus test set.
    """
    if N == 1:
        return P[0]

    minPow = math.floor(math.log2(N - 1)) + 1
    arcs = [[[None, None] for _ in range(N)] for _ in range(minPow)]

    for i in range(N):
        arcs[0][i] = [D[i], max(P[(i + 1) % N] - P[i] - D[i], 0)]

    for i in range(1, minPow):
        len = 2 ** i
        for j in range(N):
            k = (j + len // 2) % N
            arcs[i][j][0] = arcs[i - 1][j][0] + arcs[i - 1][k][0]
            initPower = P[j] + arcs[i - 1][j][0] + arcs[i - 1][j][1] - P[k]
            arcs[i][j][1] = arcs[i - 1][j][1] + max(arcs[i - 1][k][1] - initPower, 0)

    bestTime = float('inf')

    for i in range(N):
        temp, curPow, curLen = N - 1, 0, 0
        curArc = [0, 0]

        while temp > 0:
            if temp % 2 == 1:
                initPower = P[i] + curArc[0] + curArc[1] - P[(i + curLen) % N]
                curArc[0] += arcs[curPow][(i + curLen) % N][0]
                curArc[1] += max(arcs[curPow][(i + curLen) % N][1] - initPower, 0)
                curLen += 2**curPow

            temp >>= 1
            curPow += 1

        bestTime = min(bestTime, P[i] + curArc[0] + curArc[1])

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
