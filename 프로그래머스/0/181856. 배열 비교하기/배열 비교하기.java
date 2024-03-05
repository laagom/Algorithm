class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int arr1_length = arr1.length;
        int arr2_length = arr2.length;
        int arr1_sum = 0;
        int arr2_sum = 0;
        
        // 두 배열의 크기가 동일하지 않은 경우
        if(arr1_length != arr2_length) {
            return arr1_length > arr2_length ? 1 : -1;
            
        // 두 배열의 크기가 동일한 경우
        }else {
            // 두 배열의 합 가져와 비교
            arr1_sum = getSumArray(arr1);
            arr2_sum = getSumArray(arr2);
            
            if(arr1_sum == arr2_sum) {
                return 0;
            }else {
                return arr1_sum > arr2_sum ? 1 : -1;
            }
        }
    }
    
    // 배열의 합 가져오기
    public int getSumArray(int[] arr) {
        int sum = 0;
        for(int i=0; i<arr.length; i++)
            sum += arr[i];
        return sum;
    }
}