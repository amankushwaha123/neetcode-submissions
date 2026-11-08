class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 48 and ord(i) <= 57):
                s1=s1+i
        if s1[0::].upper() == s1[::-1].upper():
            return True
        return False

        