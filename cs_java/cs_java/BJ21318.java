import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 피아노 체조 https://www.acmicpc.net/problem/21318
public class BJ21318 {
    static int N;
    static int Q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> list = new ArrayList<>();
        list.add(0);
        int prev = Integer.parseInt(st.nextToken());
        int current, total = 0;
        while (st.hasMoreTokens()) {
            current = Integer.parseInt(st.nextToken());
            if (prev > current) {
                total++;
            }
            list.add(total);
            prev = current;
        }
        list.add(total);

        Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            System.out.println(list.get(y - 1) - list.get(x - 1));
        }

    }
}