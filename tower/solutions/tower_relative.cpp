/* Credits: Austin Geng, OlyFans */

#include <iostream>
#include <vector>

using namespace std;

typedef long long int lli;

/**
 * Return the minimum number of hours needed to destroy all the towers in the circle.
 * 
 * N: the number of towers in the circle
 * P: the list of integers denoting the power level of each tower
 * D: the list of integers denoting the distance to the next tower in the circle
 */
lli solve(int N, vector<lli> P, vector<lli> D) {
    // start at Tower #1
    lli maxRelPow = 0;
    lli totalDist = 0;
    for (int i = 0; i < N; ++i) {
        maxRelPow = max(maxRelPow, P[i] - totalDist);
        totalDist += D[i];
    }
    lli best = maxRelPow + totalDist - D[N-1];
    // move backwards
    for (int i = N-1; i > 0; --i) {
        maxRelPow = max(maxRelPow - D[i], P[i]);
        best = min(best, maxRelPow + totalDist - D[i-1]);
    }
    return best;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        vector<lli> P(N);
        for (lli &power: P) {
            cin >> power;
        }

        vector<lli> D(N);
        for (lli &dist: D) {
            cin >> dist;
        }

        cout << solve(N, P, D) << '\n';
    }
    return 0;
}