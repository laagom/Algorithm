import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr) {
        // 최소 2의 정수 거듭제곱 가져오기
        int square = getSquare(arr);
        
        return getResult(square, arr);
    }
    
    // 최소 2의 정수 거듭제곱 가져오기
    public int getSquare(int[] arr) {
        int square = 0;
        int[] list = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
        for(int j = 0; j <= list.length; j++) {
            if(list[j] < arr.length) {
                continue;
            }else{
                square = list[j];
                break;
            }
        }
        return square;
    }
    
    // 배열 외에 square의 길이가 될때까지 0추가 순회
    public List<Integer> getResult(int square, int[] arr) {
        List<Integer> intList = new ArrayList<Integer>();
        for(int i = 0; i <= square-1; i++) {
            if(i < arr.length) {
                intList.add(arr[i]);
            }else {
                intList.add(0);
            }
        }
        return intList;
    }
}