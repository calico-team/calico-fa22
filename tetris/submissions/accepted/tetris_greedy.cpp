#include <iostream>
#include <set>

using namespace std;

string PIECES = "ZLOSIJT";

/**
 * Return true if the sequence of placed pieces is possible and false if it's
 * impossible.
 * 
 * N: the number of placed pieces
 * P: the recorded sequence of placed pieces
 */
bool solve (int N, string P) {
	char hold = '?';
	set<char> used;
	for (int i = 0; i < N; i++) {
		if (used.count(P[i]) == 0) used.insert(P[i]);
		else if (P[i] == hold) hold = '?';
		else if (hold == '?' && used.size() == PIECES.size() - 1) {
			for (char c: PIECES) if (used.count(c) == 0) hold = c;
			used = {P[i]};
		} else return false;
		if (used.size() == PIECES.size()) used.clear();
	}
	
	return true;
}

int main () {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        string P;
        cin >> P;
        cout << (solve(N, P) ? "YES" : "NO") << '\n';
    }
}
