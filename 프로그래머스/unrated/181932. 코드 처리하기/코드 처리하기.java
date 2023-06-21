class Solution {
    public String solution(String code) {
        String answer = "";
        String code_peace = "";
        int mode = 0;
        
        for(int i = 0; i < code.length(); i++) {
            code_peace = String.valueOf(code.charAt(i));
            if(mode == 0) {
                if(!code_peace.equals("1") && i%2 == 0) {
                    answer += code_peace;
                } else if(code_peace.equals("1")) {
                    mode = 1;
                }
            } else if(mode == 1) {
                if(!code_peace.equals("1") && i%2 != 0) {
                    answer += code_peace;
                } else if(code_peace.equals("1")) {
                    mode = 0;
                }
            }
        }  
        return answer == "" ? "EMPTY" : answer;
    }
}