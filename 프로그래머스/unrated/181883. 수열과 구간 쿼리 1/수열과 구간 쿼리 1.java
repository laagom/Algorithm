class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for(int[] query : queries) {
            int s = query[0];
            int e = query[1];
            
            // s~e까지 순회를 돌며 ++
            for(int i = s ; i <= e ; i++) {
                arr[i]++;
            }
        }
        return arr;
    }
}