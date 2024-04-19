#Problem 2946

from typing import List

class MatrixSimilarityAfterCyclicShifts:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        if k % cols == 0:
            return True
        for r in range(0, len(mat)):
            for c in range(0, len(mat[0])):
                new_c = (c + k) % cols if r % 2 == 0 else (c + cols - k) % cols
                if mat[r][new_c] != mat[r][c]:
                    return False
        return True
