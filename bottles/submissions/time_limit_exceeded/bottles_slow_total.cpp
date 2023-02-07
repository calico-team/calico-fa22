/**
 * @file bottles_slow_total.cpp
 * @brief This file is copied from bottles.cpp, except the code for calculating
 * the total time is adapted from the slower bottles_main.cpp (there are
 * modifications to support long longs.) It eventually outputs the correct
 * answer but takes O(N^2) time.
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<int> vi;
typedef vector<bool> vb;

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
	ll total = 0;
	for (int j = 0; j < N; ++j) {
		ll wait = 0;
		for (int k = 0; k <= j; ++k) wait += a[k].first;
		total += wait;
	}
	cout << total << '\n';

	// Output new permutation
	vb is_fixed(N); // is_fixed[i] denotes whether student `i` is in place
	for (int i = 0; i < N; ++i) if (a[i].first == C[i]) is_fixed[i] = true;
	int j = 0; // Pointer to pair in `a`
	for (int k = 0; k < N; ++k) {
		if (is_fixed[k]) cout << k + 1 << ' ';
		else {
			while (is_fixed[a[j].second]) ++j;
			cout << a[j].second + 1 << ' ';
			++j;
		}
	}
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