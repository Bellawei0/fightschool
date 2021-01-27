class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = 0, start = 0;
        
        for(int end = 0; end < s.length(); end ++){
            char rightChar = s.charAt(end);
            map.put(rightChar,map.getOrDefault(rightChar, 0) + 1); 
            
            while(map.size() > k){
                char leftChar = s.charAt(start);
                map.put(leftChar, map.get(leftChar)- 1);
                
                if(map.get(leftChar) == 0)
                    map.remove(leftChar);
                start ++;
            }
            
            maxLength = Math.max(maxLength, end - start +1); 
        }  
        return maxLength;            
    }
}