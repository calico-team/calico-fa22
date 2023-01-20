#include <bits/stdc++.h>

using namespace std;

/**
 * Creates the output image by naively drawing every slash of every edge.
 */
void solve(int H, int W, int D, vector<vector<char>> base) {
    char image[H + D + 1][W + D + 1];
    memset(image, ' ', sizeof(image)); // initialize all values to spaces
    
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            image[i][j] = base[i][j];
        }
    }
    
    vector<pair<int,int>> corners;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (base[i][j] == '+') {
                for (int k = D; k > 0; k--) {
                    image[i + k][j + k] = '\\';
                }
            }
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

