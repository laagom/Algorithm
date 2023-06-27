class Solution {
    public int[] solution(int[] arr, int k) {
        // 짝수 true, 홀수 false
        boolean odd_oven = k%2 == 0 ? true : false;
        System.out.println(odd_oven);
        for(int i = 0; i < arr.length; i++) {
            if(odd_oven) {
                arr[i] += k;
            }else{
                arr[i] *= k;
            }
        }
        return arr;
    }
}