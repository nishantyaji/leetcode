from typing import List


class CrawlerLogFolder:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if depth > 0:
                    depth -= 1
            else:
                depth += 1
        return depth if depth > 0 else 0
