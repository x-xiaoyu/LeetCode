class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        min_stuff = list(s)

        for i in range(n-2, -1, -1):
            min_stuff[i] = min(min_stuff[i], min_stuff[i + 1])
        
        t = []
        paper = []

        for i , char in enumerate(s):
            t.append(char)

            if i + 1 < n:
                remain_num = min_stuff[i + 1]
            else:
                remain_num = "{"
            
            while t and t[-1] <= remain_num:
                paper.append(t.pop())
        return "".join(paper)
 
