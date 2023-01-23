#include <iostream>

using namespace std;

/**
 * Checks the name length requirement, followed by the 
 * registration year, and finally the trademark guidelines.
 */
bool solve(int Y, string N) {
    if (N.length() > 50) {
        return false;
    }

    if (Y < 2010) {
        return true;
    }
    
    for (int i = 0; i < N.length(); i++) 
        N[i] = tolower(N[i]);

    string word = N.substr(0, N.find(" "));
    return !(word == "cal" || word == "california" || word == "berkeley");
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int Y;
        cin >> Y;
        cin.ignore();
        string N;
        getline(cin, N);
        cout << (solve(Y, N) ? "VALID" : "INVALID") << '\n';
    }
}
