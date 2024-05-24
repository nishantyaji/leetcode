# Problem 1255
import collections
from typing import List


class MaxScoreWordsFormedByLetters:

    def __init__(self):
        self.max_score = 0
        self.letter_dict = dict()
        self.counter_dict = dict()
        self.score = []

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.letter_dict = collections.Counter(letters)
        self.score = score
        new_words = []
        for word in words:
            my_counter = collections.Counter(word)
            if not self.is_lhs_le(my_counter, self.letter_dict):
                continue
            new_words.append(word)
            self.counter_dict[word] = my_counter

        if len(self.counter_dict) == 0:
            return 0
        self.recurse(new_words, 0, dict())
        return self.max_score

    def recurse(self, words: List[str], index: int, running: dict):
        if index == len(words) - 1:
            temp = self.add(running, self.counter_dict[words[index]])
            if self.is_lhs_le(temp, self.letter_dict):
                self.max_score = max(self.max_score, self.calc_score(temp, self.score))
            return

        self.recurse(words, index + 1, running)

        this_counter = self.counter_dict[words[index]]
        temp = self.add(running, this_counter)
        if self.is_lhs_le(temp, self.letter_dict):
            self.max_score = max(self.max_score, self.calc_score(temp, self.score))
            self.recurse(words, index + 1, temp)

    def is_lhs_le(self, dict1: dict, dict2: dict) -> bool:
        for k, v in dict1.items():
            v2 = dict2[k]
            if v2 is None or v2 < v:
                return False
        return True

    def add(self, dict1: dict, dict2: dict) -> dict:
        result = dict(dict1)
        for k, v in dict2.items():
            if k not in result:
                result[k] = 0
            result[k] += v
        return result

    def calc_score(self, dict1: dict, score: List[int]) -> int:
        return sum([score[ord(k) - ord('a')] * v for k, v in dict1.items()])


if __name__ == '__main__':
    m = MaxScoreWordsFormedByLetters()
    print(m.maxScoreWords(["e", "bac", "baeba", "eb", "bbbbd", "cad", "c", "c"],
                          ["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c",
                           "c", "d", "d", "d", "d", "d", "d", "d", "e", "e", "e", "e"],
                          [8, 4, 6, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    m = MaxScoreWordsFormedByLetters()
    print(m.maxScoreWords(["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                          [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    m = MaxScoreWordsFormedByLetters()
    print(m.maxScoreWords(["leetcode"], ["l", "e", "t", "c", "o", "d"],
                          [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
    m = MaxScoreWordsFormedByLetters()
    print(m.maxScoreWords(["xxxz", "ax", "bx", "cx"], ["z", "a", "b", "c", "x", "x", "x"],
                          [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))

    # print(m.maxScoreWords())
