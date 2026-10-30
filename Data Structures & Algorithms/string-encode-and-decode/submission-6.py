class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return '-.8'
        else:
            b = '----'.join(strs)
            return b

    def decode(self, s: str) -> List[str]:
        if s == '-.8':
            return []
        else:
            l = s.split('----')
            return l
