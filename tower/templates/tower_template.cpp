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
int solve(int N, vector<lli> P, vector<lli> D) {
    // YOUR CODE HERE
    return 0;
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
        for (lli &dist: P) {
            cin >> dist;
        }

        cout << solve(N, P, D) << '\n';
    }
    return 0;
}
