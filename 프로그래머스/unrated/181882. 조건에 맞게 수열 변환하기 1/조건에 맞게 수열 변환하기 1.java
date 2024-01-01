class Solution {
    public int[] solution(int[] arr) {
        int i = 0;
        for(int number : arr) {
            // 원소에 대한 값이 50보다 크거나 같은 짝수
            if(number >= 50 && number%2 == 0) {
                arr[i] = number/2;
                
            // 원소에 대한 값이 50보다 작은 홀수
            }else if(number < 50 && number%2 != 0) {
                arr[i] = number*2;
            }
            i++;
        }
        return arr;
    }
}