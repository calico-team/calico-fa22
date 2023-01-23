/* Credits: CodeTiger (Alex Fan), OlyFans */

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

using namespace std;

#include <iostream>
#include <cstring>

#define MAXN 100005

int N,a[MAXN];
string s;
string bag = "JOTLIZS";
bool dp[MAXN][1 << 7][8];

void solve() {
	cin >> N >> s;
	for(int i = 1;i <= N;++i) {
		memset(dp[i],0,sizeof(dp[i]));
		for(int j = 0;j < 7;++j) {
			if(s[i - 1] == bag[j]) {
				a[i - 1] = j;
				break;
			}
		}
	}

	memset(dp[0],0,sizeof(dp[0]));
	dp[0][0][7] = true;
	for(int i = 0;i < N;++i) {
		for(int J = 0;J < (1 << 7);++J) {
			int j = J;
			if(J == (1 << 7) - 1) {
				j = 0;
			}
			// No hold yet
			if(dp[i][J][7]) {
				// hold
				for(int l = 0;l < 7;++l) {
					if(j & (1 << l)) continue;
					dp[i][j | (1 << l)][l] = true;
				}
				// play
				if(~j & (1 << a[i])) {
					dp[i][j | (1 << a[i])][7] = true;
				}
			}
			for(int k = 0;k < 7;++k) {
				if(!dp[i][J][k]) continue;
				int uwu = a[i];
				// hold
				if(k == a[i]) {
					for(int l = 0;l < 7;++l) {
						if(j & (1 << l)) continue;
						dp[i + 1][j | (1 << l)][l] = true;
					}
				}
				// current thing matches
				if(~j & (1 << a[i])) {
					dp[i + 1][j | (1 << a[i])][k] = true;
				}
			}
		}
	}

	for(int i = 0;i < (1 << 7);++i) {
		for(int j = 0;j < 8;++j) {
			if(dp[N][i][j]) {
				cout << "YES" << "\n";
				return;
			}
		}
	}

	cout << "NO" << "\n";
	return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	while(T--) solve();
	return 0;
}