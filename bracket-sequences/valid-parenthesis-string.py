class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0, 0
        for ch in s:
            if ch == '(':
                min_left, max_left = min_left + 1, max_left + 1
            elif ch == ')':
                min_left, max_left = min_left - 1, max_left - 1
            else:
                min_left, max_left = min_left - 1, max_left + 1
            print(min_left, max_left)
            if max_left < 0: # handles unmatched )
                return False
            min_left = max(0, min_left) # just use * as an empty string
        return min_left == 0 # handles unmatched (
