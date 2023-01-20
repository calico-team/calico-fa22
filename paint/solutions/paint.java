import java.io.*;

class paint {
    /**
     * Compares the costs to convert all of the paint to each color (directly and indirectly).
     * Returns the minimum cost, in overall constant time.
     */
    static int solve(int W, int O, int B, int Cow, int Cbo, int Cbw) {
    	int to_W = O * Math.min(Cow, Cbo + Cbw) + B * Math.min(Cbw, Cow + Cbo);
        int to_O = W * Math.min(Cow, Cbo + Cbw) + B * Math.min(Cbo, Cbw + Cow);
        int to_B = W * Math.min(Cbw, Cow + Cbo) + O * Math.min(Cbo, Cbw + Cow);
        return Math.min(to_W, Math.min(to_O, to_B));
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            int W = Integer.parseInt(line[0]);
            int O = Integer.parseInt(line[1]);
            int B = Integer.parseInt(line[2]);
            int Cow = Integer.parseInt(line[3]);
            int Cbo = Integer.parseInt(line[4]);
            int Cbw = Integer.parseInt(line[5]);
            out.println(solve(W, O, B, Cow, Cbo, Cbw));
        }
        out.flush();
    }
}
