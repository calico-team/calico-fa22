import java.io.*;

class Solution {
    /**
     * Find the maximum amount of bread you can eat before the semester ends, given 
     * your available swipes.
     * 
     * N: the number of days in the semester
     * K: the number of meal cards you have
     * D: the number of days a meal card will be activated for after swiping
     * B: the list of integers denoting the number of bread loaves available 
     *    at the cafeteria on each day
     */
    static int solve(int N, int K, int D, int[] B) {
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
            int K = Integer.parseInt(info[1]);
            int D = Integer.parseInt(info[2]);

            String[] b_input = in.readLine().split(" ");
            int[] B = new int[b_input.length];
            for (int j = 0; j < b_input.length; j++) {
                B[j] = Integer.parseInt(b_input[j]);
            }

            out.println(solve(N, K, D, B));
        }
        out.flush();
    }
}
