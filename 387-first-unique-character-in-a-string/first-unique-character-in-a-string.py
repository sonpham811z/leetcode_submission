class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque()
        my_dict= {}

        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for i in s:
            if my_dict.get(i) == 1:
                q.append(i)

        if(len(q) == 0):
            return -1
        
        key = q.popleft()
        for i in range(len(s)):
            if(s[i] == key):
                return i