import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int[] arr = new int[26];

        int i = 0;
        while(i < s.length()){
            arr[(int)s.charAt(i)%26] += 1;
            arr[(int)t.charAt(i)%26] -= 1;  
            i++;         
        }
    
        if(Arrays.stream(arr).parallel().filter(a -> a!=0).findFirst().orElse(0) != 0){
            return false;
        }

        return true;
    }
}