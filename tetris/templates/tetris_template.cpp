#include <iostream>

using namespace std;

/**
 * Return true if the sequence of placed pieces is possible and false if it's
 * impossible.
 * 
 * N: the number of placed pieces
 * P: the recorded sequence of placed pieces
 */
bool solve(int N, string P) {
    // YOUR CODE HERE
    return false;
}

int main() {
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
