class Solution {
    public int solution(int[] arr, int idx) {
        // idx보다 큰 인덱스부터 반복문 순회
        for(int i = idx; i < arr.length; i++) {
            // 조건에 해당하는 최소 인덱스를 반환하면 되기 때문에 바로 i 리턴
            if(arr[i] == 1) { 
                return i;
            }
        }
        // 조건에 해당하는 인덱스가 없으면 -1 리턴
        return -1;
    }
}