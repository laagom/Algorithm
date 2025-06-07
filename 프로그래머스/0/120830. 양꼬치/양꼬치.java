class Solution {
    public int solution(int n, int k) {
        int yang = 12000; // 양꼬치
        int drink = 2000; // 음료
        
        // 양꼬치 + 음료 총합
        int yang_price = yang * n;
        int drink_price = drink * k;
        
        // 양꼬치 10인분에 음료 +1
        int service = (n/10)*2000;
        int tot_price = yang_price + drink_price - service;
        
        return tot_price;
    }
}