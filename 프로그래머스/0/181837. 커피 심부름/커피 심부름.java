class Solution {
    public int solution(String[] order) {
        int amount = 0;
        int americano_price = 4500;
        int cafelatte_price = 5000;
        for(String coffee:order) {
            if(coffee.contains("americano") || coffee.contains("anything"))
                amount += americano_price;
            if(coffee.contains("cafelatte"))
                amount += cafelatte_price;
        }
        return amount;
    }
}