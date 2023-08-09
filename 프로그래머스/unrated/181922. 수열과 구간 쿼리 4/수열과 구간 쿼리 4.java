class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int start, end, pivot;
        
        for(int[] query:queries) {
            start = query[0];
            end   = query[1];
            pivot = query[2];
            
            for(int num = start; num <= end; num++) {
                if(num%pivot == 0) {
                    arr[num] += 1;
                }
            }
        }
        return arr;
    }
}