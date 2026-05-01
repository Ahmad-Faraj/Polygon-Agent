import java.util.*;
import java.io.*;

// <<<PF_PLACEHOLDER>>>
// Rules:
//   Class name MUST be Main.
//   Use BufferedReader+StreamTokenizer (fast IO). Never Scanner for large input.
//   Same algorithm as acc.cpp, independently implemented in Java.
//   Use out.println() not System.out.println().
//   No package declarations, no System.exit().
//   Uploaded with tag OK, sourceType java21.

public class Main {
    static BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
    static StreamTokenizer in = new StreamTokenizer(br);
    static PrintWriter    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static int  nextInt()  throws IOException { in.nextToken(); return (int)  in.nval; }
    static long nextLong() throws IOException { in.nextToken(); return (long) in.nval; }

    static void solve() throws IOException {
        // <<<PF_PLACEHOLDER>>>
        // Read with nextInt()/nextLong(). Write with out.println().
    }

    public static void main(String[] args) throws IOException {
        int t = 1;
        // t = nextInt();  // uncomment if spec.multitest == true
        while (t-- > 0) solve();
        out.flush();
    }
}