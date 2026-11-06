class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Method 1: Nested Loop
            Look for the pair that adds up to the target

            Time Complexity: O(n^2)
            Space Complexity: O(1)

        Method 2: Hashmap
            Map each num to its respective index
            At each iteration if we find a value present in the hashmap which is (target-current_val), then that means we have found a solution pair
            Saving the indices as the values because that is what we want to return

            Time Complexity: O(n)
            Space Complexity: O(n)
        '''

        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement],i]

            hash_map[nums[i]] = i
