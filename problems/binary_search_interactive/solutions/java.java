import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static void solve() throws IOException {
        int n = Integer.parseInt(br.readLine().trim());
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            out.println(mid);
            out.flush();   // MUST flush for interactive

            String resp = br.readLine().trim();
            if      (resp.equals("less"))    hi  = mid - 1;
            else if (resp.equals("greater")) lo  = mid + 1;
            else                             return;   // equal
        }
        out.println(lo);
        out.flush();
        br.readLine();   // read "equal"
    }

    public static void main(String[] args) throws IOException {
        solve();
        out.flush();
    }
}
