public class LongestRepeatingCharacterReplacement {
    public static int characterReplacement(String s, int k){
        int[] charCounts = new int[26];

        int start =0, maxLength = 0, maxCount = 0;

        for(int end = 0; end < s.length(); end++){
            charCounts[s.charAt(end)-'A']++;
            int currentCount = charCounts[s.charAt(end)-'A'];
            maxCount = Math.max(maxCount,currentCount);

            while(end - start - maxCount + 1 > k){
                charCounts[s.charAt(start)-'A']--;
                start++;
            }

            maxLength = Math.max(maxLength,end - start+1);

        }

        return maxLength;

    }

    public static void main(String[] args){
        String s = "AABABBA";
        int k = 1;

        System.out.println(characterReplacement(s,k));
    }
}
