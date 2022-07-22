
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        for i in range(len(s2)-window_size+1):
            s = s2[i:i + window_size]
            for j in s1:
                if j not in s:
                    break
                try:
                    s = s.replace(j, '', 1)
                except:
                    break
            if j == s1[-1] and len(s) == 0:
                return True
        return False


if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "eidbaooo"
    # s1 = "hello"
    # s2 = "ooolleoooleh"
    s1 = "abc"
    s2 = "ccccbbbbaaaa"
    result = Solution().checkInclusion(s1,s2)
    print(result)
