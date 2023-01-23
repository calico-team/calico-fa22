import java.io.*;

class Solution {
    /**
     * Precomputes the walking and waiting times for every power of 2 length arc.
     * Uses these precomputed arcs to simulate each starting point in O(log N) time.
     * This runs in O(N log N) time, passing the bonus test set.
     */
    static long solve(int N, long[] P, long[] D) {
    	if (N == 1) {
    		return P[0];
    	}
		
		int minPow = (int) Math.floor(Math.log(N - 1) / Math.log(2)) + 1;
		long[][][] arcs = new long[minPow][N][2];
		
		for (int i = 0; i < N; i++) {
			arcs[0][i] = new long[] {D[i], Math.max(P[(i + 1) % N] - P[i] - D[i], 0)};
		}
		
		for (int i = 1; i < minPow; i++) {
			int len = (int) Math.pow(2, i);
			for (int j = 0; j < N; j++) {
				int k = (j + len / 2) % N;
				arcs[i][j][0] = arcs[i - 1][j][0] + arcs[i - 1][k][0];
				long initPower = P[j] + arcs[i - 1][j][0] + arcs[i - 1][j][1] - P[k];
				arcs[i][j][1] = arcs[i - 1][j][1] + Math.max(arcs[i - 1][k][1] - initPower, 0);
			}
		}
		
		long bestTime = Long.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			int temp = N-1, curPow = 0, curLen = 0;
			long[] curArc = new long[2];
			while (temp > 0) {
				if (temp % 2 == 1) {
					long initPower = P[i] + curArc[0] + curArc[1] - P[(i + curLen) % N];
					curArc[0] += arcs[curPow][(i + curLen) % N][0];
					curArc[1] += Math.max(arcs[curPow][(i + curLen) % N][1] - initPower, 0);
					curLen += Math.pow(2, curPow);
				}
				temp >>= 1;
				curPow++;
			}
			
			bestTime = Math.min(bestTime, P[i] + curArc[0] + curArc[1]);
		}
		
		return bestTime;
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
