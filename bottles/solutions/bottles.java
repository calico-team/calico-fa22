// Credits: Joshc (Joshua Chen)

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Template {
    /**
    * Output the minimum total wait time on the first line.
    * Output the optimal new permutation on the second line.
    * 
    * N: the number of students in line
    * C: the list of the bottle capacities, in liters, for each student
    */
    static void solve (int N, int[] C) {
        // Solve the problem 0-indexed, then adjust to 1-indexed at the end
        ArrayList<Integer> bottleOrder = new ArrayList<>(); // Sorted list of bottles
        int res[] = new int[N]; // The outputted permutation
        for (int i=0; i<N; i++) {
            bottleOrder.add(C[i]);
            res[i] = i;
        }
        Collections.sort(bottleOrder);
        
        ArrayList<Integer> movedPeople = new ArrayList<>(); // Which people will move?
        ArrayList<Integer> movedPeopleOrdering = new ArrayList<>(); // The sorted ordering of the moved people 
        long ans = 0, curWaitTime = 0;

        for (int i=0; i<N; i++) {
            if (C[i] != bottleOrder.get(i)) {
                movedPeople.add(i);
                movedPeopleOrdering.add(i);
            }
            curWaitTime += bottleOrder.get(i);
            ans += curWaitTime;
        }

        Collections.sort(movedPeopleOrdering, Comparator.comparingInt(x -> C[x]));
        for (int i=0; i<movedPeople.size(); i++) res[movedPeople.get(i)] = movedPeopleOrdering.get(i);
        
        out.println(ans);
        for (int i=0; i<N; i++) out.print((res[i]+1) + (i == N-1 ? "\n" : " "));
    }
    
    static BufferedReader in = new BufferedReader(
        new InputStreamReader(System.in)
    );
    static PrintWriter out = new PrintWriter(System.out);

    public static void main (String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; ++i) {
            int N = Integer.parseInt(in.readLine());
            String[] Cs = in.readLine().split(" ");
            int[] C = new int[N];
            for (int j = 0; j < N; ++j) C[j] = Integer.parseInt(Cs[j]);
            solve(N, C);
        }
        out.flush();
    }
}