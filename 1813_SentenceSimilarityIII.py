# Problem 1813

class SentenceSimilarityIII:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1 if len(sentence1) < len(sentence2) else sentence2
        s2 = sentence1 if s1 == sentence2 else sentence2
        # s1 <= s2

        w1, w2 = s1.split(), s2.split()
        consumed = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                break
            consumed += 1
        for _ in range(consumed):
            w1.pop(0)
            w2.pop(0)
        w1.reverse()
        w2.reverse()
        consumed = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                break
            consumed += 1

        return consumed == len(w1)


if __name__ == '__main__':
    s = SentenceSimilarityIII()
    print(s.areSentencesSimilar("xD iP tqchblXgqvNVdi", "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"))
    print(s.areSentencesSimilar("My name is Haley", "My Haley"))
    print(s.areSentencesSimilar("of", "A lot of words"))
    print(s.areSentencesSimilar("Eating right now", "Eating"))