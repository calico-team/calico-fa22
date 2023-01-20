import java.io.*;

class tower_main {
    /**
     * Simulates going around the circle, beginning at every tower.
     * This runs in O(N^2) time, only passing the main test set.
     */
    static int solve(int N, int[] P, int[] D) {
    	int bestTime = Integer.MAX_VALUE;
		
		for (int start = 0; start < N; start++) {
			int totalTime = P[start];
			for (int i = 0; i < N - 1; i++) {
				int curTower = (start + i) % N;
				totalTime += D[curTower];
				totalTime = Math.max(totalTime, P[(curTower + 1) % N]);
			}
			bestTime = Math.min(bestTime, totalTime);
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
            int[] P = new int[N];
            for (int j = 0; j < N; j++) P[j] = Integer.parseInt(line[j]);

            line = in.readLine().split(" ");
            int[] D = new int[N];
            for (int j = 0; j < N; j++) D[j] = Integer.parseInt(line[j]);

            out.println(solve(N, P, D));
        }
        out.flush();
    }
}
