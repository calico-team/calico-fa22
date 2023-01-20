import java.io.*;
import java.util.regex.Pattern;

class Solution {
    static Pattern VALID_SYLLABLES = Pattern.compile("^([ptkmnlswj]?[aeiou]n?)+$");
    static Pattern ILLEGAL_SEQUENCES = Pattern.compile("w[uo]|[jt]i|n[mn]|[aeiou]{2}");
    
    /**
     * Checks W against a regex to see if it only uses valid syllables and against
     * another to see if it contains any illegal sequences.
     */
    static String solve(String W) {
        if (VALID_SYLLABLES.matcher(W).find() &&
            !ILLEGAL_SEQUENCES.matcher(W).find()) {
            return "pona";
        } else {
            return "ike";
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String W = in.readLine();
            out.println(solve(W));
        }
        out.flush();
    }
}
