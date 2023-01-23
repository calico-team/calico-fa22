import java.io.*;
import java.util.StringTokenizer;

class Solution {
    /**
     * Checks the name length requirement, followed by the 
     * registration year, and finally the trademark guidelines.
     */
    static boolean solve(int Y, String N) {
        if (N.length() > 50) {
            return false;
        }
        
        if (Y < 2010) {
            return true;
        }

        String s = N.toLowerCase();
        int index = s.indexOf(" ");

        String word;
        if (index == -1){
            word = s;
        } else {
            word = s.substring(0, index);
        }

        return !(word.equals("california") || word.equals("cal") 
                || word.equals("berkeley"));
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int Y = Integer.parseInt(in.readLine());
            String N = in.readLine();
            out.println(solve(Y, N) ? "VALID" : "INVALID");
        }
        out.flush();
    }
}
