# Problem 648
from typing import List


class ReplaceWords:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # there are better ways of doing this
        # Running through each letter of each word & checking whether substring exists in dictionary
        # Creating a Trie and traversal of each word through the trie
        # Let me revise the code sometime in the future
        remove_set = set()
        for i in range(0, len(dictionary)):
            for j in range(i + 1, len(dictionary)):
                if dictionary[j].startswith(dictionary[i]):
                    remove_set.add(j)
                elif dictionary[i].startswith(dictionary[j]):
                    remove_set.add(i)

        remove_list = list(remove_set)
        remove_list.sort(reverse=True)
        for i in remove_list:
            dictionary.pop(i)

        result, words = [], sentence.split(" ")
        for word in words:
            found = False
            for d in dictionary:
                if word.startswith(d):
                    result.append(d)
                    found = True
            if not found:
                result.append(word)

        return " ".join(result)


if __name__ == '__main__':
    r = ReplaceWords()
    print(r.replaceWords(["catt", "cat", "bat", "rat"], "the catt cat was rat by the bat"))
    print(r.replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
    print(r.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
    print(r.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
