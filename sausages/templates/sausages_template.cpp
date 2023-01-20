#include <iostream>
#include <vector>

using namespace std;

/**
 * Determine if a cut exists that yields exactly K sausage links. If such a cut
 * exists, return any "c1 c2" where c1 and c2 are the heights of the cut. If
 * such a cut is not possible, return "IMPOSSIBLE".
 * 
 * N: the number of sausage chains
 * K: the target number of sausage links
 * H: a list of the heights of the top of each sausage chain
 * L: a list of the heights of the bottom of each sausage chain
 */
string solve(int N, long K, vector<long>& H, vector<long>& L) {
    // YOUR CODE HERE
    return "IMPOSSIBLE";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        long K;
        cin >> K;
        vector<long> H(N), L(N);
        for (int j = 0; j < N; j++) {
            cin >> H[j];
        }
        for (int j = 0; j < N; j++) {
            cin >> L[j];
        }
        cout << solve(N, K, H, L) << '\n';
    }
}
