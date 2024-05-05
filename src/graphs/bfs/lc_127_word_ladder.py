from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def wordsDifferByOneChar(str1, str2):
            diff_count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1

        self.minpath = float('inf')                

        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        for word in wordList:
            if wordsDifferByOneChar(beginWord, word):
                adj[beginWord].append(word)
                adj[word].append(beginWord)
        for i in range(len(wordList) - 1):
            word1 = wordList[i]
            for j in range(i+1, len(wordList)):
                word2 = wordList[j]
                if wordsDifferByOneChar(word1, word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for neigh in adj[word]:
                    if neigh not in visit:
                        visit.add(neigh)
                        q.append(neigh)
            res += 1
        return 0