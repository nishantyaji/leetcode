# Problem 1223
from typing import List


class TreeNode:

    def __init__(self, val: str, arr: list[str]):
        self.end_flag = False
        self.is_root = False
        self.children = []
        self.val = val
        if arr:
            self.children.append(TreeNode(arr[0], arr[1:]))
        else:
            self.end_flag = True

    def add(self, arr: list[str]):
        if arr:
            exists = False
            for c in self.children:
                if c.val == arr[0]:
                    if arr[1:]:
                        c.add(arr[1:])
                    else:
                        c.end_flag = True
                    exists = True
            if not exists:
                self.children.append(TreeNode(arr[0], arr[1:]))

    def trim(self):
        if self.end_flag:
            self.children = []
            return
        for c in self.children:
            c.trim()

    def traverse(self, running: list[str], res: list[str]):
        if self.end_flag and not self.is_root:
            running.append(self.val)
            res.append("/".join(running))
            return
        for c in self.children:
            if c:
                c.traverse(running + [self.val], res)
        return


class RemoveSubfoldersFromTheFilesystem:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def trim_(s: str):
            return s.split("/")

        folder = list(map(trim_, folder))
        root = TreeNode("", [])
        root.end_flag = False
        root.is_root = True
        for f in folder:
            root.add(f[1:])

        root.trim()
        res = []
        root.traverse([], res)
        return res


if __name__ == '__main__':
    r = RemoveSubfoldersFromTheFilesystem()
    print(r.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
