# Problem 884
import collections
from typing import List


class UncommonWordsFrom2Sentences:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w, count in collections.Counter((s1 + " " + s2).split(" ")).items() if count == 1]