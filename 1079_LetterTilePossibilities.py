# Problem 1079
import itertools


class LetterTilePossibilities:

    def numTilePossibilities(self, tiles: str) -> int:
        st = set()
        for i in range(1, len(tiles) + 1):
            st.update(list(itertools.permutations(list(tiles), i)))
        return len(st)


if __name__ == '__main__':
    l = LetterTilePossibilities()
    print(l.numTilePossibilities("AAB"))
    print(l.numTilePossibilities("AAABBC"))
    print(l.numTilePossibilities("V"))
