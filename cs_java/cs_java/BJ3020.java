import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 개똥벌레 https://www.acmicpc.net/problem/3020
public class BJ3020 {
    static int N;
    static int H;
    static int[] top;
    static int[] bottom;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        top = new int[H + 1];
        bottom = new int[H + 1];

        // 입력받기
        for (int i = 0; i < N; i++) {
            int size = Integer.parseInt(br.readLine());
            if (i % 2 == 0) {
                top[size]++;
            } else {
                bottom[size]++;
            }
        }

        // 누적합 구하기
        for (int i = H; i > 1; i--){
            top[i-1] += top[i];
            bottom[i-1] += bottom[i];
        }

        // 답 구하기
        int min = Integer.MAX_VALUE;
        int cnt = 0;
        for (int i = 1; i < H + 1; i++) {
            // H가 6일 때 Top에서 size가 5인 것들과 부딛히는 것은 bottom에서는 size가 2인 것들이다.
            // -> bottom에서의 size = H-i+1 이다.
            int sum = bottom[i] + top[H - i + 1];
            if (min > sum) {
                min = sum;
                cnt = 1;
            } else if (min == sum) {
                cnt++;
            }
        }
        System.out.println(min + " " + cnt);
    }
}
