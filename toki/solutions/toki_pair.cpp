#include <iostream>
#include <vector>

using namespace std;

string CONSONANTS = "mnptkswjl", VOWELS = "aeiou";
string ILLEGALS = "wu wo ji ti nn nm";

#define CONTAINS(text, pattern) text.find(pattern) != string::npos

bool is_valid_syllable(string s);

/**
 * Considers if W is a valid syllable or if W can be broken into two valid
 * syllables after first checking for illegal sequences.
 */
string solve(string W) {
    for (int i = 0; i < W.length() - 1; i++) {
        if (CONTAINS(ILLEGALS, W.substr(i, 2)) ||
            CONTAINS(VOWELS, W[i]) && CONTAINS(VOWELS, W[i + 1])) {
            return "ike";
        }
    }
    
    if (is_valid_syllable(W)) {
        return "pona";
    }
    
    for (int i = 0; i < W.length(); i++) {
        string left = W.substr(0, i), right = W.substr(i);
        if (is_valid_syllable(left) && is_valid_syllable(right)) {
            return "pona";
        }
    }
    
    return "ike";
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
