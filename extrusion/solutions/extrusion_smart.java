import java.io.*;
import java.util.Arrays;

class Solution {
    /**
     * Creates the output image by reversing the edge drawing direction and
     * ending each edge early if it intersects with another edge.
     */
    static void solve(int H, int W, int D, char[][] base) {
        char[][] image = new char[H + D + 1][W + D + 1];
        for (int r = 0; r < H + D + 1; r++) {
            Arrays.fill(image[r], ' ');
        }
        
        for (int r = 0; r < H; r++) {
            for (int c = 0; c < W; c++) {
                image[r][c] = base[r][c];
            }
        }
        
        for (int r = 0; r < H; r++) {
            for (int c = 0; c < W; c++) {
                if (base[r][c] == '+') {
                    for (int d = D; d > 0; d--) {
                        if (image[r + d][c + d] == '\\') {
                            break;
                        }
                        image[r + d][c + d] = '\\';
                    }
                }
            }
        }
        
        for (int r = 0; r < H; r++) {
            for (int c = 0; c < W; c++) {
                if (base[r][c] != ' ') {
                    image[r + D + 1][c + D + 1] = base[r][c];
                }
            }
        }
        
        for (int r = 0; r < H + D + 1; r++) {
            out.println(image[r]);
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] HWD = in.readLine().split(" ");
            int H = Integer.parseInt(HWD[0]);
            int W = Integer.parseInt(HWD[1]);
            int D = Integer.parseInt(HWD[2]);
            char[][] base = new char[H][];
            for (int j = 0; j < H; j++) {
                base[j] = in.readLine().toCharArray();
            }
            solve(H, W, D, base);
        }
        out.flush();
    }
}
