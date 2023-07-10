class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String sumOfOven = "";
        String sumOfOdd = "";
        
        for(int num:num_list) {
            if(num%2 == 0) {
                sumOfOven += String.valueOf(num);   
            }else {
                sumOfOdd += String.valueOf(num);
            }
        }
        // System.out.println(sumOfOven);
        // System.out.println(sumOfOdd);
        
        return Integer.valueOf(sumOfOven) + Integer.valueOf(sumOfOdd);
    }
}