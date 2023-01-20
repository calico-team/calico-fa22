import java.io.*;

class Solution {
    /**
     * Communicate with the judge using a series of pulse queries and blast
     * queries. Using P = 150 or fewer pulses, find Steve and blast them.
     * 
     * You can send queries by calling the pulse(double xp, double yp) and
     * blast(double xb, double yb) methods as defined below. If you miss your
     * blast, your program will exit.
     */
    static void solve() throws IOException {
        // YOUR CODE HERE
        return;
    }
    
    static double pulse(double xp, double yp) throws IOException {
        out.println("P " + xp + " " + yp);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return Double.parseDouble(response);
    }
    
    static void blast(double xb1, double yb1, double xb2, double yb2) throws IOException {
        out.println("B " + xb1 + " " + yb1 + " " + xb2 + " " + yb2);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            solve();
        }
    }
}
