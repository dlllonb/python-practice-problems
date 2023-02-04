class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self
    
    def inorder(self):
        """
        Returns list of all items in tree, ascending
        """
        lst = [self.value]
        cue = [self.left, self.right]
        while cue:
            for node in cue:
                lst.append(node.value)
                cue.remove(node)
                if not node.left.is_empty():
                    cue.append(node.left)
                if not node.right.is_empty():
                    cue.append(node.right)
        return sorted(lst)

    def min_item(self):
        if self.is_empty():
            return None
        lst = self.value
        cue = [self.left]
        while cue:
            for node in cue:
                if node.value < lst:
                    lst = node.value
                else:
                    return lst
                cue.remove(node)
                if not node.left.is_empty():
                    cue.append(node.left)
        return lst

    def max_item(self):
        if self.is_empty():
            return None
        lst = self.value
        cue = [self.right]
        while cue:
            for node in cue:
                if node.value > lst:
                    lst = node.value
                else:
                    return lst
                cue.remove(node)
                if not node.right.is_empty():
                    cue.append(node.right)
        return lst

    def max_item2(self):
        if self.right.is_empty():
            return self.value
        return self.right.max_item2()

    def min_item2(self):
        if self.left.is_empty():
            return self.value
        return self.left.min_item2()

    def balance_factor(self):
        return self.left.height() - self.right.height()

    def balanced_everywhere(self):
        cue = [self]
        while cue:
            for node in cue:
                if not (-1 <= node.balance_factor() <= 1):
                    return False
                cue.remove(node)
                if not node.left.is_empty():
                    cue.append(node.left)
                if not node.right.is_empty():
                    cue.append(node.right)
        return True

    def add_to_all(self, val):
        cue = [self]
        while cue:
            for node in cue:
                node.value += val
                cue.remove(node)
                if not node.left.is_empty():
                    cue.append(node.left)
                if not node.right.is_empty():
                    cue.append(node.right)
        return self

    def path_to_cue(self, val):
        path = []
        nex = self
        while not nex.is_empty():
            if val > nex.value:
                path.append(nex.value)
                nex = nex.right
            elif val < nex.value:
                path.append(nex.value)
                nex = nex.left
            else:
                path.append(val)
                return path
        return None

if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
