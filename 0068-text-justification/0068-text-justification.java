import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        
        // i 시작 
        // k 현재 줄에 포함될 단어의 수
        // l 현재 줄에 있는 단어들의 총 길이
        for (int i = 0, k, l; i < words.length; i += k) {
            
            // 이 반복문은 현재 줄에 얼마나 많은 단어들이 들어갈 수 있는지를 계산.
            for (k = l = 0; i + k < words.length && l + words[i + k].length()  <= maxWidth -k ; k++) {
                //i+k < words.length = 최대 길이를 초과하지 않기 위함
                //l + words[i+k].length() <= maxWidth - k = 한줄의 최대 길이를 계산하는 줄 -k를 하는 이유는 띄어쓰기가 있어야 하므로... 
                l += words[i + k].length();
            }

            // 줄의 첫 번째 단어를 추가
            StringBuilder tmp = new StringBuilder(words[i]);
            
            // 줄의 나머지 단어를 추가
            for (int j = 0; j < k - 1; j++) {
                
                // 만약 마지막 줄이라면, 단어 사이에는 한 칸의 공백만 추가
                if (i + k >= words.length) {
                    tmp.append(" ");
                } else {
                    // 공백을 계산 (몇 개의 공백이 필요한지)
                    int spaces = (maxWidth - l) / (k - 1) + (j < (maxWidth - l) % (k - 1) ? 1 : 0);
                    for (int s = 0; s < spaces; s++) {
                        tmp.append(" "); // 필요한 공백을 추가
                    }
                }
                tmp.append(words[i + j + 1]);
            }
            
            // 현재 줄의 남은 부분에 공백을 채움
            while (tmp.length() < maxWidth) {
                tmp.append(" ");
            }
            
            // 현재 줄을 결과 리스트에 추가
            res.add(tmp.toString());
        }
        return res;
    }
}
