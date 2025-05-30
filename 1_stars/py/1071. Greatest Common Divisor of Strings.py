# iteratively check for longest common substring
# update:
# Check for greatest common divisor.
# refer: https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        res = None
        for i in range(min(m,n), 0, -1):
            if m%i == 0 and n%i == 0 and str1[:i] == str2[:i] and str1[:i]*(m//i) == str1 and str2[:i]*(n//i) == str2:
                return str1[:i]
        if res:
            return res
        else:
            return ''


# update:
# Check for greatest common divisor.
# refer: https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a 