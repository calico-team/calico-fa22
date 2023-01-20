import java.io.*;

class Solution {
    /**
     * Return true if the sequence of placed pieces is possible and false if
     * it's impossible.
     * 
     * N: the number of placed pieces
     * P: the recorded sequence of placed pieces
     */
    static boolean solve(int N, String P) {
        // YOUR CODE HERE
        return false;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String P = in.readLine();
            out.println(solve(N, P) ? "YES" : "NO");
        }
        out.flush();
    }
}
