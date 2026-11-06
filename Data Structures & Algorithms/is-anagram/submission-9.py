class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        If len of both not equal immediately return false

        Method 1 - Hashmap
            Iterate over one word adding char and freq to hashmap
            Iterate over second and remove
            In the end if lenght of hashmap is 0 then anagrams

            Note: Hashing overhead
            Time Complexity: O(n) 
            Space Complexity: O(k)

        Method 2 - Advantage of simply lowercase
            We have only 26 viable characters
                Represent them as an array where index matches char
                a=0, b=1

            Iterate over the char and increment/decrement for each char
            If all elements are 0 at the end then they are anagrams

            Time Complexity: O(n)
            Space Complexity: O(k)

        Opting to go for the second method because input space is small (Only 26 letters) and we can avoid the hashing overhead
        '''

        if len(s) != len(t):
            return False

        char_frequency = [0] * 26
        for i in range(len(s)):
            char_frequency[ord(s[i]) - ord('a')] += 1
            char_frequency[ord(t[i]) - ord('a')] -= 1
        
        for freq in char_frequency:
            if freq != 0:
                return False
        
        return True

        

