class Solution {
    public String solution(String s) {
        String[] strArr = s.split(" ");
        // 최소값 + " " + 최대값
        return getMinNumber(strArr) + " " + getMaxNumber(strArr);
    }
    
    // 최대값 구하기
    public String getMaxNumber(String[] strArr) {
        int maxNum = Integer.valueOf(strArr[0]);
        for(String str:strArr)
            if(maxNum < Integer.valueOf(str))
                maxNum = Integer.valueOf(str);
        return String.valueOf(maxNum);
    }
    // 최솟값 구하기
    public String getMinNumber(String[] strArr) {
        int minNum = Integer.valueOf(strArr[0]);
        for(String str:strArr)
            if(minNum > Integer.valueOf(str))
                minNum = Integer.valueOf(str);
        return String.valueOf(minNum);
    }
}