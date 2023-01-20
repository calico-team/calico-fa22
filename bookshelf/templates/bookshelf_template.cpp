#include <iostream>
#include <vector>

using namespace std;

/**
 * Find the total volume of wood needed to construct the given bookshelf design.
 *
 * N: the number of shelves in the bookshelf
 * B: the thickness of the boards, in inches
 * W: the width of the shelves, in inches
 * D: the depth of the bookshelf, in inches
 * H: the list of integers denoting the height of each of the bookshelf’s shelves, in inches
 */
int solve(int N, int B, int W, int D, vector<int> H) {
    // YOUR CODE HERE
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, B, W, D;
        cin >> N >> B >> W >> D;

        vector<int> H(N);
        for (int &height: H) {
            cin >> height;
        }

        cout << solve(N, B, W, D, H) << '\n';
    }
    return 0;
}
