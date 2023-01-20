import java.io.*;

class Solution {
    /**
     * Greedily tries to match the largest syllable possible at the current
     * position, then repeats until running out of letters or finishing the
     * word.
     */
    static String solve(String W) {
        for (int i = 0; i < W.length() - 1; i++) {
            if (isIllegal(W.substring(i, i + 2)) ||
                isVowel(W.charAt(i)) && isVowel(W.charAt(i + 1))) {
                return "ike";
            }
        }
        
        int i = 0;
        while (i < W.length()) {
            if (i < W.length() - 2 &&
                isValidSyllable(W.substring(i, i + 3))) {
                i += 3;
            } else if (i < W.length() - 1 &&
                isValidSyllable(W.substring(i, i + 2))) {
                i += 2;
            } else if (isValidSyllable(W.substring(i, i + 1))) {
                i++;
            } else {
                return "ike";
            }
        }
        
        return "pona";
    }
    
    static boolean isValidSyllable(String s) {
        switch(s.length()) {
            case 1:
                return isVowel(s.charAt(0));
            case 2:
                return isConsonant(s.charAt(0)) && isVowel(s.charAt(1)) ||
                       isVowel(s.charAt(0)) && s.charAt(1) == 'n';
            case 3:
                return isConsonant(s.charAt(0)) &&
                       isVowel(s.charAt(1)) &&
                       s.charAt(2) == 'n';
            default:
                return false;
        }
    }
    
    static boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }
    
    static boolean isConsonant(char c) {
        return "mnptkswjl".indexOf(c) != -1;
    }
    
    static boolean isIllegal(String s) {
        return "wu wo ji ti nn nm".indexOf(s) != -1;
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
