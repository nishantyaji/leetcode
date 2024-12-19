# Problem 127
import collections
import copy
import sys
from typing import List


class WordLadder:
    def ladderLength_DFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #  This approach is slow because the adjacency matrix(dict) takes a lot of time
        adj = collections.defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                temp = sum([1 if wordList[i][k] != wordList[j][k] else 0 for k in range(len(beginWord))])
                if temp == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        for i in range(len(wordList)):
            temp = sum([(1 if beginWord[k] != wordList[i][k] else 0) for k in range(len(beginWord))])
            if temp == 1:
                adj[beginWord].append(wordList[i])

        def dfs(node: str, vis: set, end: str, steps: int):
            if end == node:
                return 1 + steps

            mn = sys.maxsize
            vis.add(node)
            nxts = [n for n in adj[node] if n not in vis]
            for n in nxts:
                if n not in vis:
                    temp = dfs(n, vis, end, steps + 1)
                    mn = min(mn, temp)
            return mn

        visited = set()
        res = dfs(beginWord, visited, endWord, 0)
        return 0 if res == sys.maxsize else res

    def ladderLength_BFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #  This approach is slow because the adjacency matrix(dict) takes a lot of time
        adj = collections.defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                temp = sum([1 if wordList[i][k] != wordList[j][k] else 0 for k in range(len(beginWord))])
                if temp == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        for i in range(len(wordList)):
            temp = sum([(1 if beginWord[k] != wordList[i][k] else 0) for k in range(len(beginWord))])
            if temp == 1:
                adj[beginWord].append(wordList[i])

        q = [[beginWord, 1]]
        visited = {beginWord}
        while q:
            [w, l] = q.pop()
            if w == endWord:
                return l
            nxts = [n for n in adj[w] if n not in visited]
            visited.update(nxts)
            q = [[n, 1 + l] for n in nxts] + q
        return 0


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wset = set(wordList)
        alpha = set(list("abcdefghijklmnopqrstuvwxyz"))
        end = list(endWord)
        q = [[list(beginWord), 1]]
        visited = {beginWord}
        # going through the 26 alphabets (minus 1 original) and all letters seems to be faster 26
        # since word length is 10 there might be 250 iterations per depth of BFS (or per while loop)
        while q:
            [w, l] = q.pop()
            if w == end:
                return l
            for i in range(len(w)):
                this_set = alpha - {w[i]}  # 25 in number
                for x in this_set:
                    w_copy = copy.deepcopy(w)
                    w_copy[i] = x
                    s = "".join(w_copy)
                    if s not in visited and s in wset:
                        visited.add(s)
                        q = [[w_copy, l + 1]] + q
        return 0


if __name__ == '__main__':
    w = WordLadder()
    print(w.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(w.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
