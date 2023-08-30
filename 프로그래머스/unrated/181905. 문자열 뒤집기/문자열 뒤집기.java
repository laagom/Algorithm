class Solution {
    public String solution(String my_string, int s, int e) {
        String first = my_string.substring(0, s);
        String midle = new StringBuffer(my_string.substring(s, e+1)).reverse().toString();
        String last  = my_string.substring(e+1, my_string.length());

        return first + midle + last;
    }
}