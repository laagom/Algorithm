import java.math.BigInteger;
class Solution {
    public String solution(String a, String b) {
        return sum(a, b);
    }
    
    public String sum(String a, String b) {
        BigInteger num_a = new BigInteger(a);
        BigInteger num_b = new BigInteger(b);
        return String.valueOf(num_a.add(num_b));
    }
}