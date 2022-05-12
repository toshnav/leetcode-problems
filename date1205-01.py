# 500. Keyboard Row
# Easy

# 904

# 910

# Add to List

# Share
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 

# My try 
# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         res =[]
#         k = [["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T"],["a","s","d","f","g","h","j","k","l"],["z","x","c","v","b","n","m"]]
#         for i in words :
#             a = list(i.split())
#             print(a)
#             print(len(a))
#             count1 =0
#             count2 =0
#             count3 =0
#             for j in a :
#                 if j.lower() in k[0]:
#                     count1 =  count1 + 1
#                 if j.lower() in k[1] :
#                     count2 = count2 +  1 
#                 if j.lower() in k[2] :
#                     count3 =  count3 + 1
#             if count1 == len(a) or count2 ==  len(a) or count3 == len(a):
#                 res.append(i)
#         return res

# solved problem by referance :

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        res = []
        for i in words:
            if i[0].lower() in row1:
                if all(x in row1 for x in i.lower()):
                    res.append(i)
            elif i[0].lower() in row2:
                if all(x in row2 for x in i.lower()):
                    res.append(i)
            elif i[0].lower() in row3:
                if all(x in row3 for x in i.lower()):
                    res.append(i)
        return res

#||||| set based easy apporch|||||

        class Solution(object):
            def findWords(self, words):
                ans=[]
                set1=set("qwertyuiop")
                set2=set("asdfghjkl")
                set3=set("zxcvbnm")
                for i in words:
                    if set(i.lower()) <= set1:
                        ans.append(i)
                    elif set(i.lower()) <= set2:
                        ans.append(i)
                    elif set(i.lower()) <= set3:
                        ans.append(i)
                return ans