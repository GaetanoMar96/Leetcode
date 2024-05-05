from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for word in words:
            edges = 0
            for ch in word:
                indegree[ch] += edges
                edges += 1
            for i in range(len(word)-1):
                for j in range(i+1, len(word)):
                    adj[word[i]].append(word[j])
        q = deque()
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
                
        order = ''
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                order += node
                if node in adj:
                    for char in adj[node]:
                        indegree[char] -= 1
                        if indegree[char] == 0:
                            q.append(char)
                            
        for key in indegree:
            if indegree[key] != 0:
                order += key
        
        return order