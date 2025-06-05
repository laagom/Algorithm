class Solution {
    public int solution(int age) {
        // 2022년도 기준 나이 age
        // 40 => 2022-40 + 1 = 1982
        // 23 => 2022-23 + 1 = 2000
        int pivot = 2022;
        return (pivot - age + 1);
    }
}