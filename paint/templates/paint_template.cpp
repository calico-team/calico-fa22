#include <iostream>

using namespace std;

/**
 * Return the minimum cost to convert all of the paint into a single color.
 * 
 * W: non-negative number of buckets of white paint
 * O: non-negative number of buckets of orange paint
 * B: non-negative number of buckets of brown paint
 * Cow: positive cost to convert between a bucket of orange and white paint
 * Cbo: positive cost to convert between a bucket of brown and orange paint
 * Cbw: positive cost to convert between a bucket of brown and white paint
 */
int solve(int W, int O, int B, int Cow, int Cbo, int Cbw) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int W, O, B, Cow, Cbo, Cbw;
        cin >> W >> O >> B >> Cow >> Cbo >> Cbw;
        cout << solve(W, O, B, Cow, Cbo, Cbw) << '\n';
    }
}
