#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vp;

/**
 * Output the minimum total wait time on the first line.
 * Output the optimal new permutation on the second line.
 * 
 * N: the number of students in line
 * C: the list of the bottle capacities, in liters, for each student
 */
void solve (int N, vector<int> C) {
    // Initial sort
    vp a(N); // `a` for array of pairs
	for (int i = 0; i < N; ++i) a[i] = {C[i], i};
	sort(a.begin(), a.end());
	
    // Output total wait time
    int total = 0;
    for (int j = 0; j < N; ++j) {
        int wait = 0;
        for (int k = 0; k <= j; ++k) wait += a[k].first;
        total += wait;
    }
    cout << total << '\n';

    // Output new permutation
    for (pii p: a) cout << p.second + 1 << ' ';
    cout << endl;
}

int main () {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;
        vector<int> C(N);
        for (int &C_i: C) cin >> C_i;
        solve(N, C);
    }
}