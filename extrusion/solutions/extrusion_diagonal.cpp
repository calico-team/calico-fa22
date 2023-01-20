#include <bits/stdc++.h>

using namespace std;

/**
 * Creates the output image by drawing edges on each diagonal. When a corner
 * is found, keep track of how many more slashes to draw for that edge. When
 * an intersection is found with an upcoming edge, reset the number of
 * slashes.
 */
void solve(int H, int W, int D, vector<vector<char>> base) {
    char image[H + D + 1][W + D + 1];
    memset(image, ' ', sizeof(image)); // initialize all values to spaces
    
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            image[i][j] = base[i][j];
        }
    }
    
    for (int d = 1 - W; d < H; d++) {
        int i = max(0, d);
        int j = i - d;
        int slashesToDraw = 0;
        while (i < H + D + 1 && j < W + D + 1) {
            if (slashesToDraw > 0) {
                image[i][j] = '\\';
                slashesToDraw--;
            }
            if (i < H && j < W && base[i][j] == '+') {
                slashesToDraw = D;
            }
            i++;
            j++;
        }
    }
    
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (base[i][j] != ' ') {
                image[i + D + 1][j + D + 1] = base[i][j];
            }
        }
    }
    
    for (int i = 0; i < H + D + 1; i++) {
        for (int j = 0; j < W + D + 1; j++) {
            cout << image[i][j];
        }
        cout << '\n';
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int H, W, D;
        cin >> H >> W >> D;
        vector<vector<char>> base(H);
        cin.ignore();
        for (int j = 0; j < H; j++) {
            string temp;
            getline(cin, temp);
            vector<char> row(temp.begin(), temp.end());
            base[j] = row;
        }
        solve(H, W, D, base);
    }
}
