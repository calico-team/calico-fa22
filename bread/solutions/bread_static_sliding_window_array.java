import java.io.*;

class Solution {
    /**
     * Uses a sliding window approach with a queue-like structure
     * to more efficiently calculate how much bread can be eaten
     * if you swiped on a given day.
     */
    static int solve(int N, int K, int D, int[] B) {
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

        int highestSwipeAmt = 0;
        for (int windowTail = 0; windowTail < N; windowTail++) {
            highestSwipeAmt = Math.max(highestSwipeAmt, queue[queueLeftBound]);

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

        return highestSwipeAmt;
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
