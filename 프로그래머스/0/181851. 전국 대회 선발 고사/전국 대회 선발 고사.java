import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        
        // 학생 객체 생성
        int len = rank.length;
        Student[] students = new Student[len];
        for(int i = 0; i < len; i++) {
            students[i] = new Student(i, rank[i], attendance[i]);
        }
        // 학생 객체 정렬
        Arrays.sort(students,(a, b) -> a.rank - b.rank);
        
        // 학생 추출
        int cnt = 0;
        int[] abc = new int[3];
        for(int i = 0; i < rank.length; i++) {
            if(cnt == 3) break;

            if(students[i].attend) {
                abc[cnt++] = students[i].num;     
            }
        }
        
        return 10000*abc[0] + 100*abc[1] + abc[2];
    }
    
    class Student{
        int num;
        int rank;
        boolean attend;
        
        Student(int num, int rank, boolean attend) {
            this.num = num;
            this.rank = rank;
            this.attend = attend;
        }
    }
}