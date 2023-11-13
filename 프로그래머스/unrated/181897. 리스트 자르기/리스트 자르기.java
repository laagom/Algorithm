import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Solution {
    
    public static final int CONDITION_ONE   = 1;
    public static final int CONDITION_TWO   = 2;
    public static final int CONDITION_THREE = 3;
    public static final int CONDITION_FOUR  = 4;
    
    public List<Integer> solution(int n, int[] slicer, int[] num_list) {
        
        // int[] -> List<Integer>로 변환
        List<Integer> list = Arrays.stream(num_list)
                                    .boxed()
                                    .collect(Collectors.toList());
        
        // 특정 n마다 조건을 다르게 num_list를 슬라이싱
        List<Integer> rtnList = new ArrayList<Integer>();
        switch(n) {
            case CONDITION_ONE:
                rtnList = getSliceList(list,0,slicer[1],1);
                break;
            case CONDITION_TWO:
                rtnList = getSliceList(list,slicer[0],list.size()-1,1);
                break;
            case CONDITION_THREE:
                rtnList = getSliceList(list,slicer[0],slicer[1],1);
                break;
            case CONDITION_FOUR:
                rtnList = getSliceList(list,slicer[0],slicer[1],slicer[2]);
                break;
        }
        return rtnList;
    }
    
    // List 슬라이스 함수
    // PARAM : List, 시작 idx, 종료 idx, 건너뛰는 수
    public List<Integer> getSliceList(List<Integer> list, int start, int end, int jump) {
        List<Integer> subList = new ArrayList<Integer>();        
        for(int i = start; i <= end; i= i+jump) {
            subList.add(list.get(i));    
        }
        return subList;
    }
}