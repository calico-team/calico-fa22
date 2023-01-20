import java.io.*;

class Solution {
    /**
     * Uses dynamic programming to maximize the amount of bread
     * that can be eaten with all swipes. Manually simulates the 
     * effect of using a swipe.
     */
    static int solve(int N, int K, int D, int[] B) {
        K = Math.min(K, (N / D) + 1);

        int[][] dp = new int[N + 1][K + 1];

        for (int swipes = 1; swipes <= K; swipes++) {
            for (int startDay = N; startDay >= 0; startDay--) {
                if (startDay == N) {
                    dp[startDay][swipes] = 0;
                } else {
                    int runningTotal = 0;
                    for (int i = startDay; i < Math.min(N, startDay + D); i++) {
                        if (B[i] == 0) {
                            break;
                        }

                        runningTotal += B[i];
                    }

                    dp[startDay][swipes] = Math.max(
                        dp[Math.min(N, startDay + D)][swipes - 1] + runningTotal,
                        dp[startDay + 1][swipes]
                    );
                }
            }
        }

        return dp[0][K];
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
