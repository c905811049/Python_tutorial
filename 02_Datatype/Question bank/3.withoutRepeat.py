class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用一个字典来保存每个字符的最后出现的位置
        char_index_map = {}
        # 初始化窗口的起始和结束位置
        start = 0
        max_length = 0
        
        # 遍历字符串
        for end in range(len(s)):
            char = s[end]
            
            # 如果字符已经在窗口中，则将窗口的起始位置移动到之前出现该字符的位置后一位
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
                
            # 将字符的当前位置保存到字典中
            char_index_map[char] = end
            
            # 更新窗口的长度
            max_length = max(max_length, end - start + 1)
        
        return max_length
      
def test():
    solution = Solution()
    char = solution.lengthOfLongestSubstring("abcabcbabd")
    return char

test = test()

print(test)