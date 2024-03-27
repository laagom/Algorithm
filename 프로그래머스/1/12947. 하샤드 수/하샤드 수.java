import java.util.*;
class Solution {
    public boolean solution(int x) {
        return getHarshad(x);
    }
    
    public boolean getHarshad(int x) {
        int sum = 0;
        boolean flag = false;
        String[] list = String.valueOf(x).split("");
        for(String str: list)
            sum += Integer.valueOf(str); 
        
        if(x%sum == 0)
            flag = true;
        return flag;
    }
}