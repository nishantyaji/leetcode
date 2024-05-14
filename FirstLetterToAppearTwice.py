# Problem 2351

class FirstLetterToAppearTwice:
    def repeatedCharacter(self, s: str) -> str:
        my_set = set()
        for ch in s:
            if ch in my_set:
                return ch
            my_set.add(ch)
