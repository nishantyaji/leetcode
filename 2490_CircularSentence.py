class CircularSentence:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        return all([words[(i + 1) % len(words)][0] == w[-1] for i, w in enumerate(words)])
