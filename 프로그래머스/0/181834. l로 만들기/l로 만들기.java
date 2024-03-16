import java.util.*;
class Solution {
    public String solution(String myString) {
        List<String> rtnList = new ArrayList<String>();
        
        String temp = "";
        for(int i = 0; i < myString.length(); i++) {
            // 숫자로 변경된 String 값 할당
            temp = String.valueOf((int) myString.charAt(i));
            
            // 자리의 문자가 l보다 앞서는 문자면 숫자로 변경된 String이 l보다 작을거임
            if(Integer.valueOf(temp) < (int)'l') {
                // l보다 작은 경우 l을 넣어주고
                temp = "l";
            }else {
                // l보다 큰 경우 있는 자리의 값을 넣어준다.
                temp = String.valueOf(myString.charAt(i));
            }
            rtnList.add(temp);
        }
        return String.join("", rtnList);
    }
}