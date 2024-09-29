# Problem 432

"""
The code is a big unorganized. I will rework on cleaning this up soon.
"""


class Node:
    def __init__(self, val: int):
        self.prev = None
        self.next = None
        self.count = 0
        self.value = val
        self.keys = set()


class AllOne:

    def __init__(self):
        self.head = None
        self.rev_head = None
        self.mp = {}  # count to Node mapping
        self.key_mp = {}  # key to count mapping

    def fetch(self, cnt):
        is_new = False
        if cnt not in self.mp:
            self.mp[cnt] = Node(cnt)
            is_new = True
        return self.mp[cnt], is_new

    def ins_to_head(self, node: Node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
        else:
            self.head = node

    #
    # def rem_head(self):
    #     if self.head:
    #         new_head = self.head.next
    #         new_head.prev = None
    #         self.head = new_head

    # def ins_to_tail(self, node: Node):
    #     if self.rev_head:
    #         node.next = None
    #         node.prev = self.rev_head
    #         self.rev_head.next = node
    #         self.rev_head = node
    #     else:
    #         self.rev_head = node

    def rem_tail(self):
        if self.rev_head:
            new_rev = self.rev_head.prev
            if new_rev:
                new_rev.next = None
            else:
                self.head = None
            self.rev_head = new_rev

    def ins_to_right(self, old_left: Node, new_right: Node):
        new_right.next = old_left.next
        if old_left.next:
            old_left.next.prev = new_right
        else:
            self.rev_head = new_right
        new_right.prev = old_left
        old_left.next = new_right

    def ins_to_left(self, new_left: Node, old_right: Node):
        if old_right.prev:
            if old_right.prev.value != new_left.value:
                new_left.prev = old_right.prev
            old_right.prev.next = new_left
        else:
            self.head = new_left
        new_left.next = old_right
        old_right.prev = new_left

    def rem_node(self, node: Node):
        left = node.prev
        right = node.next
        if left:
            left.next = right
        else:
            # node is head
            self.head = right
            self.head.prev = None
        if right:
            right.prev = left
        else:
            self.rev_head = left
            self.rev_head.next = None

    def inc(self, key):
        is_new = key not in self.key_mp
        new_cnt = 1 if is_new else self.key_mp[key] + 1
        self.key_mp[key] = new_cnt

        if is_new:
            this_node, is_new2 = self.fetch(new_cnt)
            this_node.count += 1
            this_node.keys.add(key)
            if not self.head:
                self.head = self.rev_head = this_node
            elif self.head and self.head.value > 1:
                self.ins_to_head(this_node)
        else:
            this_node, is_new2 = self.fetch(new_cnt)

            self.fetch(new_cnt - 1)[0].count -= 1
            self.fetch(new_cnt - 1)[0].keys.remove(key)
            self.mp[new_cnt].count += 1
            self.mp[new_cnt].keys.add(key)

            if is_new2:
                self.ins_to_right(self.fetch(new_cnt - 1)[0], self.fetch(new_cnt)[0])

            if self.fetch(new_cnt - 1)[0].count == 0:
                self.rem_node(self.fetch(new_cnt - 1)[0])
                del self.mp[new_cnt - 1]

    def dec(self, key):
        new_cnt = self.key_mp[key] - 1
        if new_cnt == 0:
            del self.key_mp[key]
        else:
            self.key_mp[key] = new_cnt

        self.mp[new_cnt + 1].count -= 1
        self.mp[new_cnt + 1].keys.remove(key)

        if new_cnt > 0:
            new_node, is_new = self.fetch(new_cnt)
            self.mp[new_cnt].count += 1
            self.mp[new_cnt].keys.add(key)
            self.ins_to_left(self.mp[new_cnt], self.mp[new_cnt + 1])
            # if self.head.value > new_cnt:
            #     self.head = self.mp[new_cnt]

        if self.mp[new_cnt + 1].count == 0:
            if self.rev_head.value == new_cnt + 1:
                self.rem_tail()
            else:
                self.rem_node(self.mp[new_cnt + 1])
            del self.mp[new_cnt + 1]

    def getMinKey(self):
        if not self.head or len(self.head.keys) == 0:
            return ""
        for i in self.head.keys:
            return i

    def getMaxKey(self):
        if not self.rev_head or len(self.rev_head.keys) == 0:
            return ""
        for i in self.rev_head.keys:
            return i


if __name__ == '__main__':
    a = AllOne()
    print(a.inc("hello"))
    print(a.inc("hello"))
    print(a.getMaxKey())
    print(a.getMinKey())
    print(a.dec("hello"))
    print(a.dec("hello"))
    print(a.getMinKey())
    print(a.inc("hello"))
    print(a.getMinKey())
