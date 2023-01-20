#include <iostream>
#include <vector>

using namespace std;

string CONSONANTS = "mnptkswjl", VOWELS = "aeiou";
string ILLEGALS = "wu wo ji ti nn nm";

#define CONTAINS(text, pattern) text.find(pattern) != string::npos

bool is_valid_syllable(string s);

/**
 * Uses bottom-up dynamic programming to check the syllable structure, after
 * first checking for illegal sequences.
 */
string solve(string W) {
    for (int i = 0; i < W.length() - 1; i++) {
        if (CONTAINS(ILLEGALS, W.substr(i, 2)) ||
            CONTAINS(VOWELS, W[i]) && CONTAINS(VOWELS, W[i + 1])) {
            return "ike";
        }
    }
    
    // dp[i] is true if and only if W.substr(i) has a valid syllable structure.
    bool dp[W.length() + 3];
    dp[W.length()] = true;
    dp[W.length() + 1] = dp[W.length() + 2] = false;
    for (int i = W.length() - 1; i >= 0; i--) {
        dp[i] = dp[i + 1] && is_valid_syllable(W.substr(i, 1)) ||
                dp[i + 2] && is_valid_syllable(W.substr(i, 2)) ||
                dp[i + 3] && is_valid_syllable(W.substr(i, 3));
    }
    
    if (dp[0]) {
        return "pona";
    } else {
        return "ike";
    }
}

bool is_valid_syllable(string s) {
    switch (s.length()) {
        case 1:
            return CONTAINS(VOWELS, s[0]);
        case 2:
            return CONTAINS(CONSONANTS, s[0]) && CONTAINS(VOWELS, s[1]) ||
                   CONTAINS(VOWELS, s[0]) && s[1] == 'n';
        case 3:
            return CONTAINS(CONSONANTS, s[0]) &&
                   CONTAINS(VOWELS, s[1]) &&
                   s[2] == 'n';
        default:
            return false;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string W;
        cin >> W;
        cout << solve(W) << '\n';
    }
}
