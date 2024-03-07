class Solution {
    public int[] solution(int[] arr, int n) {
        int len = arr.length;
        
        for(int i = 0; i < arr.length; i++) {
            // 배열의 길이가 짝수인 경우
            if(len%2 == 0) {
                // 홀수 위치의 값에 n 증가
                if(i%2 == 1) {
                    arr[i] += n;
                }
                
            // 배열의 길이가 홀수인경우
            }else {
                // 짝수 위치의 값에 n 증가
                if(i%2 == 0) {
                    arr[i] += n;
                }
            }
        }
        return arr;
    }
}