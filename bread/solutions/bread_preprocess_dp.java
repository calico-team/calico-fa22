import java.io.*;

class Solution {
    /**
     * Combines the sliding window technique with the
     * dynamic programming approach to remove the need to
     * manually simulate all swipes.
     */
    static int solve(int N, int K, int D, int[] B) {
        K = Math.min(K, (N / D) + 1);

        int[] swipeAmts = preprocessSwipeAmounts(N, K, D, B);

        int[][] dp = new int[N + 1][K + 1];

        for (int swipes = 1; swipes <= K; swipes++) {
            for (int startDay = N; startDay >= 0; startDay--) {
                if (startDay == N) {
                    dp[startDay][swipes] = 0;
                } else {
                    dp[startDay][swipes] = Math.max(
                        dp[Math.min(N, startDay + D)][swipes - 1] + swipeAmts[startDay],
                        dp[startDay + 1][swipes]
                    );
                }
            }
        }

        return dp[0][K];
    }

    static int[] preprocessSwipeAmounts(int N, int K, int D, int[] B) {
        int[] queue = new int[N];
        int queueLeftBound = 0;
        int queueRightBound = 0;

        for (int i = 0; i < Math.min(N, D); i++) {
            if (B[i] == 0) {
                queueRightBound++;
            } else {
                queue[queueRightBound] += B[i];
            }
        }

        int[] swipeAmts = new int[N];
        for (int windowTail = 0; windowTail < N; windowTail++) {
            swipeAmts[windowTail] = queue[queueLeftBound];

            if (B[windowTail] == 0) {
                queueLeftBound++;
            } else {
                queue[queueLeftBound] -= B[windowTail];
            }

            int windowHead = windowTail + D;
            if (windowHead >= N) {
                ;
            } else if (B[windowHead] == 0) {
                queueRightBound++;
            } else {
                queue[queueRightBound] += B[windowHead];
            }
        }

        return swipeAmts;
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
