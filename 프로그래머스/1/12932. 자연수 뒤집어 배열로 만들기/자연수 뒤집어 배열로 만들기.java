import java.util.*;
class Solution {
    public List<Integer> solution(long n) {
        String numStr = String.valueOf(n);
        List<Integer> numArray = new ArrayList();
        for(int i = numStr.length()-1; i >= 0; i--)
            numArray.add(numStr.charAt(i)-'0');
        
        return numArray;
    }
}