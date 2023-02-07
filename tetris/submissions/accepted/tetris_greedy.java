import java.io.*;
import java.util.*;

class Solution {
	static String PIECES = "ZLOSIJT";
	
	/**
	 * Return true if the sequence of placed pieces is possible and false if
	 * it's impossible.
	 * 
	 * N: the number of placed pieces
	 * P: the recorded sequence of placed pieces
	 */
	static boolean solve(int N, String P) {
		Set<Character> seenSoFar = new HashSet<>();
		char heldPiece = '_';
		
		for (int i = 0; i < P.length(); i++) {
			if (seenSoFar.size() == 7) {
				seenSoFar.clear();
			}
			
			char piece = P.charAt(i);
			if (!seenSoFar.contains(piece)) {
				seenSoFar.add(piece);
			} else {
				if (heldPiece == '_' && seenSoFar.size() == 6) {
					for (int j = 0; j < 7; j++) {
						if (!seenSoFar.contains(PIECES.charAt(j))) {
							heldPiece = PIECES.charAt(j);
						}
					}
					seenSoFar.clear();
					seenSoFar.add(piece);
				} else if (heldPiece == piece) {
					heldPiece = '_';
				} else {
					return false;
				}
			}
		}
		
		return true;
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
