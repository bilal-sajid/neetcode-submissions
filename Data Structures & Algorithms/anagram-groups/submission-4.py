from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Method 1: Sorting + Hashmap
            Each anagram would have the same sorted key
            On every element, sort it, compare with hashmap and then add it to the hashmap
            At the end, iterate over all keys and append the values into a final answer
            n is length of strs
            m is average length of each word

            Time Complexity: O(n * mlogm)
            Space Complexity: O(n)

        Method 2: Hashmap (No sorting)
            Take advantage of only lowercase input
                A tuple acts as a key (immutable) where each index represents frequency of a character - a at index 0, b at index 1, c at index 2
                Anagrams would have the same tuple

            
            Time Complexity:O(n*m)
            Space Complexity: O(n)
        '''

        anagram_map = defaultdict(list)

        for word in strs:
            char_frequency = [0] * 26
            for char in word:
                char_frequency[ord(char) - ord('a')] += 1

            anagram_map[tuple(char_frequency)].append(word)
        
        ans = []
        for anagrams in anagram_map.values():
            ans.append(anagrams)
        
        return ans

            

