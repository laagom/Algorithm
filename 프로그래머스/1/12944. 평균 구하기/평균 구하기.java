class Solution {
    public double solution(int[] arr) {
        return getArraySum(arr);
    }
    
    public double getArraySum(Object obj) {
        int amount = 0;
        int[] arr = (int[])obj;
        
        for(int number:arr)
            amount += number;

        return amount/Double.valueOf(arr.length);
    }
}