import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
    static StreamTokenizer in = new StreamTokenizer(br);
    static PrintWriter    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static int  nextInt()  throws IOException { in.nextToken(); return (int)  in.nval; }
    static long nextLong() throws IOException { in.nextToken(); return (long) in.nval; }

    static void solve() throws IOException {
        int n = nextInt();
        long target = nextLong();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = nextLong();

        java.util.HashMap<Long, Integer> seen = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            long complement = target - a[i];
            if (seen.containsKey(complement)) {
                out.println((seen.get(complement) + 1) + " " + (i + 1));
                return;
            }
            seen.put(a[i], i);
        }
        out.println("-1 -1");
    }

    public static void main(String[] args) throws IOException {
        int t = 1;
        while (t-- > 0) solve();
        out.flush();
    }
}