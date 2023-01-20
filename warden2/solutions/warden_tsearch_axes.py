import math

WARDEN, STEVE, ALEX = (0, 0), (61926, -18290), (-81928, -73681)

PLAYER_LIMIT = 10 ** 5
P = 1500
ITERATIONS = 500
MIN_DISTANCE = 1000
HALF_MIN_DISTANCE = MIN_DISTANCE / 2

def solve() -> None:
    """
    TODO add docs
    TODO implement
    """
    def dist_x_0_to_players(x):
        dist_pulse_path = pulse(x, 0)
        dist_warden_to_pulse = abs(x)
        dist_pulse_to_players = dist_pulse_path / 2 - dist_warden_to_pulse
        return dist_pulse_to_players
    XB = tsearch(-PLAYER_LIMIT, PLAYER_LIMIT, ITERATIONS, dist_x_0_to_players)
    
    def dist_XB_y_to_players(y):
        dist_pulse_path = pulse(XB, y)
        dist_warden_to_pulse = math.sqrt(XB ** 2 + y ** 2)
        dist_pulse_to_players = dist_pulse_path / 2 - dist_warden_to_pulse
        return dist_pulse_to_players
    YB = tsearch(-PLAYER_LIMIT, PLAYER_LIMIT, ITERATIONS, dist_XB_y_to_players)
    
    dist_pulse_path = pulse(XB, YB)
    dist_warden_to_pulse = math.sqrt(XB ** 2 + YB ** 2)
    opt_dist = dist_pulse_path / 2 - dist_warden_to_pulse
    
    def dist_XYB_circle_angle(theta):
        pulse_x, pulse_y = XB + HALF_MIN_DISTANCE * math.cos(theta), YB + HALF_MIN_DISTANCE * math.sin(theta)
        dist_pulse_path = pulse(pulse_x, pulse_y)
        dist_warden_to_pulse = math.sqrt(pulse_x ** 2 + pulse_y ** 2)
        dist_pulse_to_players = dist_pulse_path / 2 - dist_warden_to_pulse
        return dist_pulse_to_players
    
    theta = rsearch(0, math.pi, 4, ITERATIONS, dist_XYB_circle_angle)
    XB1, YB1 = XB + HALF_MIN_DISTANCE * math.cos(theta), YB + HALF_MIN_DISTANCE * math.sin(theta)
    
    print(XB, YB, XB1, YB1)
    
    def line_interp_y(x1, y1, x2, y2, x):
        return (y2 - y1) / (x2 - x1) * (x - x1) + y1
    
    def line_interp_x(x1, y1, x2, y2, y):
        return (y - y1) * (x2 - x1) / (y2 - y1) + x1
    
    left_player_y = line_interp_y(XB, YB, XB1, YB1, -PLAYER_LIMIT)
    if left_player_y < -PLAYER_LIMIT:
        x, y = line_interp_x(XB, YB, XB1, YB1, -PLAYER_LIMIT), -PLAYER_LIMIT
    elif left_player_y > PLAYER_LIMIT:
        x, y = line_interp_x(XB, YB, XB1, YB1, PLAYER_LIMIT), PLAYER_LIMIT
    else:
        x, y = -PLAYER_LIMIT, left_player_y
    
    print(x, y)
    
    def true_if_on_segment(x):
        pulse_x, pulse_y = x, line_interp_y(XB, YB, XB1, YB1, x)
        dist_pulse_path = pulse(pulse_x, pulse_y)
        dist_warden_to_pulse = math.sqrt(pulse_x ** 2 + pulse_y ** 2)
        dist_pulse_to_players = dist_pulse_path / 2 - dist_warden_to_pulse
        print(x, pulse_y, dist_pulse_to_players - opt_dist, 'yes' if abs(dist_pulse_to_players - opt_dist) < 1 else 'no')
        return abs(dist_pulse_to_players - opt_dist) < 1
    
    XS = bsearch(x, min(XB, XB1), 300, true_if_on_segment)
    YS = line_interp_y(XB, YB, XB1, YB1, XS)
    
    blast(XS, YS, 0, 0)

def bsearch(lo, hi, iter, func):
    for i in range(iter):
        mid = (lo + hi) / 2
        if func(mid):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def rsearch(lo, hi, iter, recur, func):
    for i in range(recur):
        range_size = (hi - lo) / iter
        lowest_lo = func_lowest_mid = float('inf')
        for j in range(iter):
            mid = lo + (j + 0.5) * range_size
            func_mid = func(mid)
            if func_mid < func_lowest_mid:
                func_lowest_mid = func_mid
                lowest_lo = lo + j * range_size
        lo, hi = lowest_lo, lowest_lo + range_size
    return (lo + hi) / 2

def tsearch(lo, hi, iter, func):
    for _ in range(iter):
        range_third = (hi - lo) / 3
        mid_lo, mid_hi = lo + range_third, hi - range_third
        mid_lo_val, mid_hi_val = func(mid_lo), func(mid_hi)
        if mid_lo_val < mid_hi_val or abs(mid_hi_val - mid_lo_val) < 5 * 10 ** -6:
            hi = mid_hi
        else:
            lo = mid_lo
    return (lo + hi) / 2

def pulse(xp: float, yp: float) -> float:
    pulse = (xp, yp)
    path = [
        WARDEN,
        pulse,
        STEVE,
        pulse,
        ALEX,
        pulse,
        WARDEN
    ]
    pulse_dist = 0
    for src, dest in zip(path, path[1:]):
        pulse_dist += dist(src, dest)
    return pulse_dist

def dist(xy0, xy1):
    x0, y0 = xy0
    x1, y1 = xy1
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

def blast(xb1: float, yb1: float, xb2: float, yb2: float) -> None:
    print('Actual:', STEVE, ALEX)
    print(f'Got: ({xb1}, {yb1}) ({xb2}, {yb2})')

def main():
    solve()

if __name__ == '__main__':
    main()
