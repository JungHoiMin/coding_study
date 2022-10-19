import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 공주님의 정원 https://www.acmicpc.net/problem/2457
public class BJ2457 {
    static class Pair {
        private final int x, y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int first() {
            return x;
        }

        int second() {
            return y;
        }

        static Pair of(int x, int y) {
            return new Pair(x, y);
        }
    }

    static int N;
    static List<Pair> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int day1 = Integer.parseInt(st.nextToken()) * 100 + Integer.parseInt(st.nextToken());
            int day2 = Integer.parseInt(st.nextToken()) * 100 + Integer.parseInt(st.nextToken());
            list.add(Pair.of(day1, day2));
        }

        list.sort((o1, o2) -> {
            if (o1.first() == o2.first()) return o2.second() - o1.second();
            return o1.first() - o2.first();
        });
        int start = 301, end = 0;
        int current = 0, answer = 0;

        while (start < 1201) {
            boolean change = false;
            for (int i = current; i < N; i++) {
                if (list.get(i).first() <= start && list.get(i).second() > end) {
                    end = list.get(i).second();
                    current = i + 1;
                    change = true;
                }
            }
            if (change) {
                start = end;
                answer++;
            } else {
                break;
            }
        }
        if (end < 1201) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
        br.close();
    }
}
