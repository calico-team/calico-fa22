from collections import defaultdict
from math import gcd

def solve(N: int, K: int, H: list[int], L: list[int]) -> str:
    """
    Begin by using a line sweep to find the change in running sausages at each
    endpoint. Then, use two pointers to slide over all endpoint ranges. For each
    range pair, consider if a cut is possible within them by solving a two
    variable linear diophantine equation.
    """
    # Line sweep across all the endpoints.
    endpoints = defaultdict(int)
    for h in H:
        endpoints[h] -= 1
    for l in L:
        endpoints[l] += 1
    
    # Zeroes result in nasty degenerate solutions later. They don't affect the
    # calculation anyway, so just get rid of them here.
    filtered = filter(lambda kv: kv[1] != 0, endpoints.items())
    endpoints = sorted(filtered)
    # Use sentinel values for cleaner iteration.
    endpoints = endpoints + [(endpoints[-1][0], 0)]
    
    # Use two pointers to slide over all endpoint ranges.
    lo_ptr = hi_ptr = 1
    lo_delta = endpoints[0][1]
    hi_delta = lo_delta + endpoints[1][1]
    between = 0
    while hi_ptr < len(endpoints) - 1:
        lo_bot, lo_top = endpoints[lo_ptr - 1][0], endpoints[lo_ptr][0]
        hi_bot, hi_top = endpoints[hi_ptr][0], endpoints[hi_ptr + 1][0]
        lo_len, hi_len = lo_top - lo_bot, hi_top - hi_bot
        
        if between > K:
            lo_ptr += 1
            lo_delta += endpoints[lo_ptr - 1][1]
            between -= lo_delta * (endpoints[lo_ptr][0] - lo_top)
        else:
            a, max_x, b, max_y = lo_delta, lo_len, hi_delta, hi_len
            # A cut that produces K exists here if and only if we can use some
            # from the lo range and some from the hi range to make the
            # difference between the target and our in between sausages.
            solution = solve_equation(a, max_x, b, max_y, K - between)
            if solution != None:
                lo_offset, hi_offset = solution
                lo, hi = lo_top - lo_offset, hi_bot + hi_offset
                return f'{lo} {hi}'
            else:
                if between + hi_delta * hi_len > K:
                    lo_ptr += 1
                    lo_delta += endpoints[lo_ptr - 1][1]
                    between -= lo_delta * (endpoints[lo_ptr][0] - lo_top)
                else:
                    between += hi_delta * hi_len
                    hi_ptr += 1
                    hi_delta += endpoints[hi_ptr][1]
    
    return 'IMPOSSIBLE'

def solve_equation(a, max_x, b, max_y, c):
    """
    Solve a two variable linear diophantine equation and return the solution
    with the highest x value.
    
    Adapted from:
    https://cp-algorithms.com/algebra/linear-diophantine-equation.html
    """
    # Helper functions
    def mod_inv(x, m):
        return pow(x, -1, m)
    def shift_solution(x, y, a, b, cnt):
        return x + cnt * b, y - cnt * a
    def trunc_div(n, d):
        return n // d if n > 0 else -((-n) // d)
    
    if a == 0 and b == 0:
        return (0, 0) if c == 0 else None
    elif a == 0:
        return (0, c // b) if c % b == 0 and c // b <= max_y else None
    elif b == 0:
        return (c // a, 0) if c % a == 0 and c // a <= max_x else None
    
    # Solution does not exist if c is not a multiple of the gcd of a and b.
    g = gcd(a, b)
    if c % g != 0:
        return None
    
    # Begin by finding any arbitrary solution.
    ag, bg = a // g, b // g
    x = ((c // g) * mod_inv(ag, bg)) % bg
    y = (c - a * x) // b
    
    # Shift the solution to smallest and largest valid x and y. Record the x
    # values and take the intersection of the intervals created by them. If we
    # find evidence that the intervals are disjoint or empty, return early.
    sign_ag, sign_bg = 1 if ag > 0 else -1, 1 if bg > 0 else -1
    
    x, y = shift_solution(x, y, ag, bg, trunc_div(-x, bg))
    if x < 0:
        x, y = shift_solution(x, y, ag, bg, sign_bg)
    if x > max_x:
        return None
    lx1 = x
    
    x, y = shift_solution(x, y, ag, bg, trunc_div(max_x - x, bg));
    if x > max_x:
        x, y = shift_solution(x, y, ag, bg, -sign_bg)
    rx1 = x

    x, y = shift_solution(x, y, ag, bg, -trunc_div(-y, ag));
    if y < 0:
        x, y = shift_solution(x, y, ag, bg, -sign_ag)
    if y > max_y:
        return None
    lx2 = x
    
    x, y = shift_solution(x, y, ag, bg, trunc_div(-(max_y - y), ag));
    if y > max_y:
        x, y = shift_solution(x, y, ag, bg, sign_ag)
    rx2 = x
    
    if lx2 > rx2:
        lx2, rx2 = rx2, lx2
    lx, rx = max(lx1, lx2), min(rx1, rx2)
    
    if lx > rx:
        return None
    
    # Return the soluton with the rightmost x
    return rx, (c - a * rx) // b

def main():
    T = int(input())
    for _ in range(T):
        NK = input().split(' ')
        N, K = int(NK[0]), int(NK[1])
        H = [int(i) for i in input().split(' ')]
        L = [int(i) for i in input().split(' ')]
        print(solve(N, K, H, L))

if __name__ == '__main__':
    main()
