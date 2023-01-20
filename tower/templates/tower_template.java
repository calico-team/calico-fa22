import java.io.*;

class Solution {
    /**
     * Return the minimum number of hours needed to destroy all the towers in the circle.
     * 
     * N: the number of towers in the circle
     * P: the list of integers denoting the power level of each tower
     * D: the list of integers denoting the distance to the next tower in the circle
     */
    static long solve(int N, long[] P, long[] D) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            int N = Integer.parseInt(line[0]);

            line = in.readLine().split(" ");
            long[] P = new long[N];
            for (int j = 0; j < N; j++) P[j] = Long.parseLong(line[j]);

            line = in.readLine().split(" ");
            long[] D = new long[N];
            for (int j = 0; j < N; j++) D[j] = Long.parseLong(line[j]);

            out.println(solve(N, P, D));
        }
        out.flush();
    }
}
