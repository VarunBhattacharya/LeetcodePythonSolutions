'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
'''

class Solution:
    def compress(self, chars) -> int:
        #Naive Approach: Two Pointer - Time Complexity - O(N) and Space Complexity - O(1)
        if not chars:
            return 0
        initialChar = chars[0]
        initialLen = len(chars)
        skips = 0
        chars.append(" ")

        for _ in range(initialLen + 1):
            popChar = chars.pop(0)
            if popChar == initialChar:
                skips += 1
            else:
                if skips == 1:
                    chars.append(initialChar)
                elif skips > 1:
                    chars.append(initialChar)
                    chars += list(str(skips))
                initialChar = popChar
                skips = 1
        return len(chars)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.compress(["a","a","b","b","c","c","c"]))