import java.util.*;
class Solution {
    public int solution(int a, int b) {
        int merge_number = Integer.valueOf(String.valueOf(a) + String.valueOf(b));
        int multi_number = 2*a*b;
        return merge_number >= multi_number ? merge_number : multi_number;
    }
}