class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String tempStr = "";
        for(int i = 0; i < myString.length(); i++) {
            tempStr = myString.substring(i);
            if(tempStr.startsWith(pat)) {
                answer ++;
            }
        }
        return answer;
    }
}