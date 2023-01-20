#include <iostream>
#include <vector>

using namespace std;

/**
 * Find the maximum amount of bread you can eat before the semester ends, given 
 * your available swipes.
 * 
 * N: the number of days in the semester
 * K: the number of meal cards you have
 * D: the number of days a meal card will be activated for after swiping
 * B: the list of integers denoting the number of bread loaves available 
 *    at the cafeteria on each day
 */
int solve(int N, int K, int D, vector<int> B) {
    // YOUR CODE HERE
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K, D;
        cin >> N >> K >> D;

        vector<int> B(N);
        for (int &bread: B) {
            cin >> bread;
        }

        cout << solve(N, K, D, B) << '\n';
    }
    return 0;
}
