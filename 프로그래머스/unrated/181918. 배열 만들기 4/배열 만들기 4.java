import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] arr) {
        ArrayList<Integer> stack = new ArrayList<Integer>(); 
        int last_element;
        int compare_element;
        
        // i가 0부터 arr 길이까지 반복문
        int i = 0;
        while(i < arr.length) {
            if(stack.size() == 0) {
                stack.add(arr[i]);
                i++;
            }else{
                // 마지막 stack 값
                last_element = stack.get(stack.size()-1);
                compare_element = arr[i];

                // arr[i] 보다 작을 때
                if(last_element < compare_element) {
                    stack.add(compare_element);
                    i++;
                }else if(last_element >= compare_element) {
                    // arr[i] 보다 크거나 같을 때
                    stack.remove(stack.size()-1);
                }
            }
        }
        return stack;
    }
}

