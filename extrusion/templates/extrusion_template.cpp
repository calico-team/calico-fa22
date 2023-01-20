#include <bits/stdc++.h>

using namespace std;

/**
 * Output the image created by extruding the base with height H and width W to a
 * depth of D.
 * 
 * H: the height of the base
 * W: the width of the base
 * D: the depth to extrude the base to
 * base: a matrix of characters representing the base itself
 */
void solve(int H, int W, int D, vector<vector<char>> base) {
    // YOUR CODE HERE
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int H, W, D;
        cin >> H >> W >> D;
        vector<vector<char>> base(H);
        cin.ignore();
        for (int j = 0; j < H; r++) {
            string temp;
            getline(cin, temp);
            vector<char> row(temp.begin(), temp.end());
            base[j] = row;
        }
        solve(H, W, D, base);
    }
}
