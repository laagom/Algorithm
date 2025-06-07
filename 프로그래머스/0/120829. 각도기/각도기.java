class Solution {
    public int solution(int angle) {
        if(angle <= 90) {
            return angle < 90 ? 1 : 2; // 예각 & 직각
        }else {
            return angle < 180 ? 3 : 4; // 둔각 & 평각
        }
    }
}