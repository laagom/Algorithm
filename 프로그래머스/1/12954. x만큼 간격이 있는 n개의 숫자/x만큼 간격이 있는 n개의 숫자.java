import java.util.*;
class Solution {
    public List<Long> solution(long x, int n) {
        List<Long> list = new ArrayList<Long>();
        int count = 0;
        long firstX = x;
        while(count < n) {
            list.add(x);
            x += firstX;
            count ++;
        }

        return list;
    }
}