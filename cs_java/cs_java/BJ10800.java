import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 컬러볼 https://www.acmicpc.net/problem/10800
public class BJ10800 {
    static class Pair {
        int a, b, c;

        Pair(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        static Pair of(int a, int b, int c) {
            return new Pair(a, b, c);
        }
    }

    static int N;
    static int[] answer;
    static Pair[] balls;
    static int[] colors;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        balls = new Pair[N];
        colors = new int[N + 1];
        answer = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int color = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());
            balls[i] = Pair.of(i, color, size);
        }
        Arrays.sort(balls, Comparator.comparingInt(o -> o.c));  // 크기순으로 나열하기 위해서 정렬
        int sum = 0;
        int idx=0;
        for (int i=0;i<N;i++){  // 공들 크기 순으로 진행
            Pair current = balls[i];
            while(balls[idx].c<current.c){  // 크기가 현재보다 작을 때만 진행
                sum+=balls[idx].c;  // sum은 누적합
                colors[balls[idx].b] += balls[idx].c;   // 색별 누적합 (공들의 크기 순으로 누적합)
                idx++;
            }
            answer[idx] = sum-colors[current.b];    // 결과 저장
        }

        // 출력을 한번에 모아서 하는 것이 시간면에서 효율적
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<N;i++){
            sb.append(answer[i]).append("\n");
        }
        System.out.print(sb);
    }

}


