#include <iostream>
#include <vector>

using namespace std;

/**
 * Finds the volume by subtracting out the empty shelf space from
 * the volume of the rectangular prism occupied by the shelf.
 */
int solve(int N, int B, int W, int D, vector<int>& H) {
    int h_sum = 0;
    for (int i = 0; i < N; i++)
        h_sum += H[i];
    
    int volume = (W + 2 * B) * D * (h_sum + B * (N + 1));
    int shelf_volume = W * D * h_sum;

    return volume - shelf_volume;
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
