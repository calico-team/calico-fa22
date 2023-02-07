/**
 * @file tetris_no_hold_overwrite.cpp
 * @brief This program neglects to update the value of the held piece when
 * pulling from the next bag.
 */

#include <iostream>
#include <set>

using namespace std;

string PIECES = "ZLOSIJT";

bool solve () {
	int N;
	string p;
	cin >> N >> p;

	char hold = ' ';
	set<char> seen; // Seen in current bag
	for (char p_i: p) {
		if (seen.size() == PIECES.size()) seen.clear();
		if (seen.count(p_i) == 0) seen.insert(p_i); // Take from current bag
		else if (p_i == hold) hold = p_i; // Take from hold
		// Take from next bag if within reach
		else if (hold == ' ' && seen.size() == PIECES.size() - 1) { 
			for (char c: PIECES) if (seen.count(c) == 0) hold = c;
			seen = {p_i};
		} else return false; // No sources
	}

	return true;
}

int main () {
	int T;
	cin >> T;
	while (T--) cout << (solve() ? "YES\n" : "NO\n");
}