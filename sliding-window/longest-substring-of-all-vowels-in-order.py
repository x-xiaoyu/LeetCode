class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        left = 0
        answer = 0
        types = 1

        for right in range(1, len(word)):
            if word[right] < word[right - 1]:
                left = right
                types = 1
            
            elif word[right] > word[right - 1]:
                types += 1

            if types == 5:
                answer = max(answer, right - left + 1)
        return answer
            
        