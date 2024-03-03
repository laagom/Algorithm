class Solution {
    public int solution(String myString, String pat) {
        myString = myString.toLowerCase().replace("a", "B").replace("b", "A");
        return myString.contains(pat) ? 1 : 0;
    }
}