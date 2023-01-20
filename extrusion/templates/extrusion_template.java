import java.io.*;

class Template {
    /**
     * Output the image created by extruding the base with height H and width W
     * to a depth of D.
     * 
     * H: the height of the base
     * W: the width of the base
     * D: the depth to extrude the base to
     * base: a matrix of characters representing the base itself
     */
    static void solve(int H, int W, int D, char[][] base) {
        // YOUR CODE HERE
        return;
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
