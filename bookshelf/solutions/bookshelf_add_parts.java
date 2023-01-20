import java.io.*;

class Solution {
    /**
     * Adds together the volume of the boards needed to
     * create the shelf.
     */
    static int solve(int N, int B, int W, int D, int[] H) {
        int totalShelfHeight = 0;
        for (int shelfHeight : H) {
            totalShelfHeight += shelfHeight;
        }

        int totalHeight = totalShelfHeight + (N + 1) * B;
        int sideBoardsVolume = totalHeight * B * 2;
        int middleBoardsVolume = B * W * (N + 1);

        return (sideBoardsVolume + middleBoardsVolume) * D;
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
