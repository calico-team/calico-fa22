import java.io.*;

class Solution {
    /**
     * Find the total volume of wood needed to construct the given bookshelf design.
     *
     * N: the number of shelves in the bookshelf
     * B: the thickness of the boards, in inches
     * W: the width of the shelves, in inches
     * D: the depth of the bookshelf, in inches
     * H: the list of integers denoting the height of each of the bookshelf’s shelves, in inches
     */
    static int solve(int N, int B, int W, int D, int[] H) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] info = in.readLine().split(" ");
            int N = Integer.parseInt(info[0]);
            int B = Integer.parseInt(info[1]);
            int W = Integer.parseInt(info[2]);
            int D = Integer.parseInt(info[3]);

            info = in.readLine().split(" ");
            int[] H = new int[info.length];
            for (int j = 0; j < info.length; j++) {
                H[j] = Integer.parseInt(info[j]);
            }

            out.println(solve(N, B, W, D, H));
        }
        out.flush();
    }
}
