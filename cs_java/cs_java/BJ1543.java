import java.io.*;

// 문서 검색 https://www.acmicpc.net/problem/1543
public class BJ1543 {
    // 문서의 시작 인덱스부터 단어의 길이까지 단어가 포함이 되는지 확인하는 함수
    static boolean check(String origin, String find, int s){
        boolean flag = true;

        // 한 글자씩 확인
        for (int i = 0; i<find.length(); i++) {
            // 글자가 같지 않다면 flag 체크 후 중지
            if (origin.charAt(i+s) != find.charAt(i)){
                flag = false;
                break;
            }
        }
        return flag;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 문서
        String origin = br.readLine();
        // 단어
        String find = br.readLine();

        int cnt = 0;
        for (int i=0;i<origin.length()-find.length()+1; i++){
            if (check(origin,find,i)){
                cnt++;
                i += find.length()-1;
            }
        }

        System.out.println(cnt);
        br.close();
    }
}
