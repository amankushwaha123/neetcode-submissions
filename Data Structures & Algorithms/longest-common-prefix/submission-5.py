class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        base = strs[0]
        result = ""
        for i in range(len(base)):
            ch = base[i]
            for j in range(1,len(strs)):
                if(i>=len(strs[j]) or ch != strs[j][i]):
                    return result
            result += ch
        return result




 
       

        