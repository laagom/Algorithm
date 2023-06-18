import java.util.Map;
import java.util.function.BiFunction;

class Solution {
    public int solution(int a, int b, boolean flag) {
        String var = String.valueOf(flag);
        Map<String, BiFunction<Integer, Integer, Integer>> calcs = Map.of(
            "true", (num1, num2) -> num1 + num2,
            "false", (num1, num2) -> num1 - num2
        );   
        return calcs.get(var).apply(a, b);
    }
}