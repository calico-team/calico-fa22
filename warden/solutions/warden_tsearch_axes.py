import math

PLAYER_LIMIT = 10 ** 5
P = 150
ITERATIONS = P // 4

def solve() -> None:
    """
    TODO add docs
    """
    def dist_x_0_to_steve(x):
        dist_pulse_path = pulse(x, 0)
        dist_warden_to_pulse = abs(x)
        dist_pulse_to_steve = dist_pulse_path / 2 - dist_warden_to_pulse
        return dist_pulse_to_steve
    XS = tsearch(-PLAYER_LIMIT, PLAYER_LIMIT, ITERATIONS, dist_x_0_to_steve)
    
    def dist_XS_y_to_steve(y):
        dist_pulse_path = pulse(XS, y)
        dist_warden_to_pulse = math.sqrt(XS ** 2 + y ** 2)
        dist_pulse_to_steve = dist_pulse_path / 2 - dist_warden_to_pulse
        return dist_pulse_to_steve
    YS = tsearch(-PLAYER_LIMIT, PLAYER_LIMIT, ITERATIONS, dist_XS_y_to_steve)
    
    blast(XS, YS)

def tsearch(lo, hi, iter, func):
    for _ in range(iter):
        range_third = (hi - lo) / 3
        mid_lo, mid_hi = lo + range_third, hi - range_third
        mid_lo_val, mid_hi_val = func(mid_lo), func(mid_hi)
        if mid_lo_val < mid_hi_val:
            hi = mid_hi
        else:
            lo = mid_lo
    return (lo + hi) / 2

def pulse(xp: float, yp: float) -> float:
    print('P', xp, yp, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return float(response)

def blast(xb: float, yb: float) -> None:
    print('B', xb, yb, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
