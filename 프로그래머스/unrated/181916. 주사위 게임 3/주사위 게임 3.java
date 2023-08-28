import java.util.*;

// 반환 객체
// 2개 이상 리턴을 만들기 위해 사용
final class Result {
    public List<Integer> list;
    public int type;
    
    public Result(int type, List<Integer> list){
        this.type = type;
        this.list = list;
    }
}

class Solution {
    // 상수
    public final static int _CONDITION_A = 1;
    public final static int _CONDITION_B = 2;
    public final static int _CONDITION_C = 3;
    public final static int _CONDITION_D = 4;
    public final static int _CONDITION_E = 5;
    
    public int solution(int a, int b, int c, int d) {
        int answer         = 0;
        Result condition   = getConditionType(a, b, c, d);
        List<Integer> list = condition.list;
        
        Collections.sort(list);

        switch(condition.type){
            // 모든 주사위가 동일한 경우
            case _CONDITION_A:
                answer = ( 1111*(int)list.get(0) );
                break;
            
            // 세 주사위가 동일하고 나머지 하나가 다른 경우
            case _CONDITION_B:
                int cnt_min = Collections.frequency(Arrays.asList(a, b, c, d), list.get(0));
                int cnt_max = Collections.frequency(Arrays.asList(a, b, c, d), list.get(1));
                int max     = cnt_min > cnt_max ? list.get(0) : list.get(1);
                int min     = cnt_min > cnt_max ? list.get(1) : list.get(0);

                answer = ( (int)Math.pow((10*max) + min, 2) );
                break;
            
            // 주사위가 2개씩 동일한 값이 나온 경우
            case _CONDITION_C:
                answer = ( ((int)list.get(0) + (int)list.get(1))*Math.abs((int)list.get(0) - (int)list.get(1)) );
                break;
            
            // 두개가 동일하고 나머지 2개가 각각 다른 경우
            case _CONDITION_D:
                int cnt1 = Collections.frequency(Arrays.asList(a, b, c, d), list.get(0));
                int cnt2 = Collections.frequency(Arrays.asList(a, b, c, d), list.get(1));
                int cnt3 = Collections.frequency(Arrays.asList(a, b, c, d), list.get(2));
                answer = ( cnt1 > cnt2 ? list.get(1)*list.get(2) : (cnt2 > cnt3) ? list.get(0)*list.get(2) : list.get(0)*list.get(1)  );
                break;
                
            // 모든 주사위가 다른경우
            case _CONDITION_E:
                answer = (int)list.get(0);
                break;                 
        }
        System.out.println(condition.type);
        return answer;
    }
    
    public Result getConditionType(int a, int b, int c, int d) {
        int type = 0; 
        List<Integer> initList = new ArrayList<Integer>(Arrays.asList(a, b, c, d));
        Set<Integer> set = new HashSet<Integer>(Arrays.asList(a, b, c, d));
        List<Integer> list = new ArrayList<Integer>(set);

        // 주사위가 모두 같은 경우
        if(list.size() == 1) {
            type = 1;
            
        }else if(list.size() == 2) {
            int cnt = Collections.frequency(initList, initList.get(0));
            System.out.println("첫번째 요소" + initList.get(0) + "의 개수" + cnt);
            // 주사위 3개가 같고 1개가 다른경우
            if (cnt == 1 || cnt == 3) {
                type = 2;
            // 주사위 2개씩 같은 경우
            }else if(cnt == 2) {
                type = 3;
            }
            
        // 주사위 2개가 같고 나머지 각각 다른경우
        }else if(list.size() == 3) {
            type = 4;
            
        // 주사위 4개가 모두 다른 경우
        }else if(list.size() == 4) {
            type = 5;
        }     
        return new Result(type, list);
    }
}