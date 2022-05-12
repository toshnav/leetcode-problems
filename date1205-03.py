# Given an integer num, return a string of its base 7 representation.
# Example 1:
# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
# Constraints:

# -107 <= num <= 107

#My solution :
from bdb import effective


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        r  =""
        if num == 0:
            return "0"
        num1 = abs(num)
        while(num1 >0):
            prevnum =  num1
            num1 =num1/7
            l =  num1 * 7
            k = abs(l-prevnum)
            r =   str(k) +  r 
        if num < 0 :
            return "-"  + r
        else : 
            return  r 
            
# effective soltion :
# Python

    def convertToBase7(self, num):
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n /= 7
        return '-' * (num < 0) + res or "0"
# Recursive Solution
# Java:

#     public String convertToBase7(int n) {
#         if (n < 0) return "-" + convertToBase7(-n);
#         if (n < 7) return Integer.toString(n);
#         return convertToBase7(n / 7) + Integer.toString(n % 7);
#     }
# C++:

#     string convertToBase7(int n) {
#         if (n < 0) return "-" + convertToBase7(-n);
#         if (n < 7) return to_string(n);
#         return convertToBase7(n / 7) + to_string(n % 7);
#     }
# Python:

    def convertToBase7(self, n):
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7: return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)