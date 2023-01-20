#include <iostream>

using namespace std;

/**
 * Determine if the RSO name for an entry is valid. Return True if it is and
 * return False otherwise.
 * 
 * Y: the year the RSO was established
 * N: the name the RSO registered with
 */
bool solve(int Y, string N) {
    // YOUR CODE HERE
    return false;
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
