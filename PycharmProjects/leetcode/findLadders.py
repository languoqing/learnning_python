"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        new_wordlist = []
        if endWord in wordList:
            
            for w in range(len(beginWord)):
                res_word = ''
                for a in range(len(endWord)):
                    if w == a :
                        res_word += endWord[a]
                    else:
                        res_word += beginWord[a]
                if res_word in wordList:
                    beginWord = res_word
                    new_wordlist.append(res_word)
                self.findLadders( beginWord, endWord, wordList)
                
            return new_wordlist
            
        else: return []
        
if __name__ == '__main__':
    a = Solution()
    begW = "hit"
    endW = "cog"
    w_list = ["hot","dot","dog","lot","log","cog"]
    res = a.findLadders(begW,endW,w_list)
    