class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = []
        ans = 0
        for it in s:
            if it not in sub_s:
                sub_s.append(it)
                print(sub_s)
            else:
                if len(sub_s) > ans:
                    ans = len(sub_s)
                sub_s.append(it)
                del sub_s[:sub_s.index(it)]
                sub_s.pop(0)
                print(sub_s)
        if len(sub_s) > ans:
            ans = len(sub_s)
        return ans


if __name__ == '__main__':

    s = "abcccabd"
    s = 'ababcabbbb'
    a = Solution().lengthOfLongestSubstring(s)
    print(a)
