import java.io.*;

class Template {
    /**
     * Determine if a cut exists that yields exactly K sausage links. If such a
     * cut exists, return any "c1 c2" where c1 and c2 are the heights of the
     * cut. If such a cut is not possible, return "IMPOSSIBLE".
     * 
     * N: the number of sausage chains
     * K: the target number of sausage links
     * H: a list of the heights of the top of each sausage chain
     * L: a list of the heights of the bottom of each sausage chain
     */
    static String solve(int N, long K, long[] H, long[] L) {
        // YOUR CODE HERE
        return "IMPOSSIBLE";
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] NK = in.readLine().split(" ");
            int N = Integer.parseInt(NK[0]);
            long K = Long.parseLong(NK[1]);
            String[] HS = in.readLine().split(" "), LS = in.readLine().split(" ");
            long[] H = new long[N], L = new long[N];
            for (int j = 0; j < N; j++) {
                H[j] = Long.parseLong(HS[j]);
                L[j] = Long.parseLong(LS[j]);
            }
            out.println(solve(N, K, H, L));
        }
        out.flush();
    }
}
