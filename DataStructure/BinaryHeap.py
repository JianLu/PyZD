"""
We implement Binary Heap as a complete complete binary tree, which can be represented by using a single list.
We use the list L[0,..,n] to represent a complete binary tree (or heap) with n nodes,
where L[0] is the number of elements, and L[1,...,n] represents the nodes, and L[1] should be the tree root.

Therefore, for a node L[p] (p>0), its left child should be L[2*p] and its right child should be L[2*p+1];
and its parent should be L[floor(p/2)]

Reference:
http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""


class MinHeap:
    def __init__(self):
        self.lst = [0]

    def is_empty(self):
        return self.lst[0] == 0

    def get_num(self):
        return self.lst[0]

    def __merge_up(self, i):
        # Trace up the parent until root
        while i // 2 > 0:
            p = i // 2
            if self.lst[i] < self.lst[p]:
                self.lst[i] = self.lst[i] ^ self.lst[p]
                self.lst[p] = self.lst[i] ^ self.lst[p]
                self.lst[i] = self.lst[i] ^ self.lst[p]
            else:
                break
            # Continue going up
            i = p

    def __merge_down(self, i):
        while i * 2 <= self.lst[0]:
            c = i * 2
            if i * 2 + 1 <= self.lst[0] and self.lst[i * 2 + 1] < self.lst[c]:
                c = i * 2 + 1
            if self.lst[i] > self.lst[c]:
                self.lst[i] = self.lst[i] ^ self.lst[c]
                self.lst[c] = self.lst[i] ^ self.lst[c]
                self.lst[i] = self.lst[i] ^ self.lst[c]
            else:
                break
            i = c

    def insert(self, x):
        if self.lst[0] == len(self.lst) - 1:
            self.lst.append(x)
        else:
            self.lst[self.lst[0] + 1] = x
        self.lst[0] += 1
        self.__merge_up(self.lst[0])

    def pop(self):
        if self.lst[0] == 0:
            return None
        ret = self.lst[1]
        self.lst[1] = self.lst[self.lst[0]]
        self.lst[0] -= 1
        self.__merge_down(1)
        return ret

    def build(self, arr):
        self.lst = [len(arr)] + arr[:]
        i = len(arr) // 2
        while i > 0:
            self.__merge_down(i)
            i -= 1


class MaxHeap:
    def __init__(self):
        self.lst = [0]

    def is_empty(self):
        return self.lst[0] == 0

    def get_num(self):
        return self.lst[0]

    def __merge_up(self, i):
        # Trace up the parent until root
        while i // 2 > 0:
            p = i // 2
            if self.lst[i] > self.lst[p]:
                self.lst[i] = self.lst[i] ^ self.lst[p]
                self.lst[p] = self.lst[i] ^ self.lst[p]
                self.lst[i] = self.lst[i] ^ self.lst[p]
            else:
                break
            # Continue going up
            i = p

    def __merge_down(self, i):
        while i * 2 <= self.lst[0]:
            c = i * 2
            if i * 2 + 1 <= self.lst[0] and self.lst[i * 2 + 1] > self.lst[c]:
                c = i * 2 + 1
            if self.lst[i] < self.lst[c]:
                self.lst[i] = self.lst[i] ^ self.lst[c]
                self.lst[c] = self.lst[i] ^ self.lst[c]
                self.lst[i] = self.lst[i] ^ self.lst[c]
            else:
                break
            i = c

    def insert(self, x):
        if self.lst[0] == len(self.lst) - 1:
            self.lst.append(x)
        else:
            self.lst[self.lst[0] + 1] = x
        self.lst[0] += 1
        self.__merge_up(self.lst[0])

    def pop(self):
        if self.lst[0] == 0:
            return None
        ret = self.lst[1]
        self.lst[1] = self.lst[self.lst[0]]
        self.lst[0] -= 1
        self.__merge_down(1)
        return ret

    def build(self, arr):
        self.lst = [len(arr)] + arr[:]
        i = len(arr) // 2
        while i > 0:
            self.__merge_down(i)
            i -= 1

if __name__ == "__main__":
    import random
    x = [i for i in range(10)]
    random.shuffle(x)

    print("Input: %s" % x)

    # Test 1
    h1 = MaxHeap()
    for n in x:
        h1.insert(n)

    print(h1.lst)
    while not h1.is_empty():
        print(h1.pop(), end=" ")
    print()

    # Test 2
    h2 = MaxHeap()
    h2.build(x)

    print(h2.lst)
    while not h2.is_empty():
        print(h2.pop(), end=" ")
    print()

