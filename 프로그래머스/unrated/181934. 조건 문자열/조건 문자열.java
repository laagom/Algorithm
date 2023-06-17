class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;    
        if(ineq_func(ineq)){
            if(eq_func(eq)){
                answer = n >= m ? 1 : 0;
            }else{
                answer = n > m ? 1 : 0;
            }
        }else{
            if(eq_func(eq)){
                answer = n <= m ? 1 : 0;
            }else{
                answer = n < m ? 1 : 0;
            } 
        }
        return answer;
    }
    
    public boolean ineq_func(String ineq){
        return ineq.equals(">") ? true : false;
    }
    
    public boolean eq_func(String eq){
        return eq.equals("=") ? true : false;
    }
    
}