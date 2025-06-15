import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] numArry = String.valueOf(n).split("");
        for(String numStr:numArry) 
            answer += Integer.valueOf(numStr);
        return answer;
    }
}