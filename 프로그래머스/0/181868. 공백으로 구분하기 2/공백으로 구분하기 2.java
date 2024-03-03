class Solution {
    public String[] solution(String my_string) {
        // 공백이 두 칸 이상 나오지 않도록 아래의 반복문을 수행.
        while (my_string.contains("  ")) {
            my_string = my_string.replace("  ", " ").trim();
        }
        return my_string.split(" ");
    }
}