class Solution {
    public int solution(int angle) {
        int angleDiv = 0;
        if(angle > 0 && angle < 90) {
            angleDiv = 1; // 예각
        }else if(angle == 90) {
            angleDiv = 2; // 직각
        }else if(angle > 90 && angle < 180) { 
            angleDiv = 3; // 둔각
        }else if(angle == 180) {        
            angleDiv = 4; // 평각
        }
        
        return angleDiv;
    }
}