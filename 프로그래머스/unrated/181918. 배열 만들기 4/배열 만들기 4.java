import java.util.Stack;

class Solution {
    public Stack<Integer> solution(int[] arr) {
        Stack<Integer> stack = new Stack<Integer>();
        int i = 0;
        
        while (i < arr.length) {
            // stack이 비어 있거나 arr[i] 값보다 작은 경우
            if(stack.empty() || stack.peek() < arr[i]) {
                stack.push(arr[i]);
                i++;
            }else if(stack.peek() >= arr[i]){
                // stack이 arr[i] 값보다 크거나 같은 경우
                stack.pop();
            }
        }
        return stack;
    }
}

