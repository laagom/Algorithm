class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int odd_sum = 0;
        int even_sum = 0;
        
        int i = 0;
        for(int num : num_list) {
            if(i%2 == 0)
                even_sum += num;
            
            if(i%2 != 0)
                odd_sum += num;
            
            i++;
        }
        return odd_sum > even_sum ? odd_sum : (odd_sum < even_sum ? even_sum : odd_sum);
    }
}