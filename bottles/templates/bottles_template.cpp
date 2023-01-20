#include <iostream>
#include <vector>

using namespace std;

/**
 * Output the minimum total wait time on the first line.
 * Output the optimal new permutation on the second line.
 * 
 * N: the number of students in line
 * C: the list of the bottle capacities, in liters, for each student
 */
void solve (int N, vector<int> C) {
    // YOUR CODE HERE
}

int main () {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;
        vector<int> C(N);
        for (int &C_i: C) cin >> C_i;
        solve(N, C);
    }
}