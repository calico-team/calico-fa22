import java.io.*;
import java.util.*;

class Solution {
    /**
    * Creates the output image by drawing edges on each diagonal. When a corner
    * is found, keep track of how many more slashes to draw for that edge. When
    * an intersection is found with an upcoming edge, reset the number of
    * slashes.
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
        
        for (int d = -W + 1; d < H; d++) {
            int r = Math.max(0, d);
            int c = r - d;
            int slashesToDraw = 0;
            while (r < H + D + 1 && c < W + D + 1) {
                if (slashesToDraw > 0) {
                    image[r][c] = '\\';
                    slashesToDraw--;
                }
                if (r < H && c < W && base[r][c] == '+') {
                    slashesToDraw = D;
                }
                r++;
                c++;
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
