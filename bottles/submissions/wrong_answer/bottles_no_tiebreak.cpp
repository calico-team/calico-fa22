/**
 * @file bottles_no_tiebreak.cpp
 * @brief This file is copied from bottles.cpp, except the part responsible for
 * outputting the new permutation is copied from bottles_main.cpp. Although the
 * code runs quickly, it will almost certainly output the wrong answer on bonus
 * tests.
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<int> vi;

/**
 * Output the minimum total wait time on the first line.
 * Output the optimal new permutation on the second line.
 * 
 * N: the number of students in line
 * C: the list of the bottle capacities, in liters, for each student
 */
void solve (int N, vector<int> C) {
	// Find optimal permutation
	vp a(N); // `a` for array of pairs
	for (int i = 0; i < N; ++i) a[i] = {C[i], i};
	sort(a.begin(), a.end());

	// Output total wait time
	ll total = 0;
	for (int i = 0; i < N; ++i) total += ll(a[i].first) * (N - i);
	cout << total << '\n';

	// Output new permutation
	for (pii p: a) cout << p.second + 1 << ' ';
	cout << endl;
}

int main () {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		vector<int> C(N);
		for (int &C_i: C) cin >> C_i;
		solve(N, C);
	}
}