#include <iostream>

using namespace std;

/**
 * Compares the costs to convert all of the paint to each color (directly and indirectly).
 * Returns the minimum cost, in overall constant time.
 */
int solve(int W, int O, int B, int Cow, int Cbo, int Cbw) {
    int to_W = O * min(Cow, Cbo + Cbw) + B * min(Cbw, Cow + Cbo);
    int to_O = W * min(Cow, Cbo + Cbw) + B * min(Cbo, Cbw + Cow);
    int to_B = W * min(Cbw, Cow + Cbo) + O * min(Cbo, Cbw + Cow);
    return min(to_W, min(to_O, to_B));

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
