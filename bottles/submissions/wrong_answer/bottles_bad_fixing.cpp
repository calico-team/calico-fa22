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
	for (int j = 0; j < N; ++j) total += ll(a[j].first) * (N - j);
	cout << total << '\n';

	// Output new permutation
	vi perm(N, -1); // -1 is a placeholder for undetermined indices
	// The line below is wrong. It incorrectly fixes the students who appear in
	// the same index before and after sorting, while the correct criterion for
	// fixing students is that the student's original index must correspond
	// to the same capacity before and after `a` is sorted. Neither of these two
	// criteria imply the other.
	for (int i = 0; i < N; ++i) if (a[i].second == i) perm[i] = i;
	// A deeper correction to the perspective used is necessary.
	int j = 0;
	for (int k = 0; k < N; ++k) {
		if (perm[k] != -1) cout << k + 1 << ' ';
		else {
			while (perm[k] != -1) ++j;
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