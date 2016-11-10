# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:47:55 2016

@author: Jian
"""


class TrieNode(object):
    """
    Class for Trie tree node
    """
    def __init__(self, value, word = None):
        self.value = value
        self.word = word
        self.children = {}


class Trie(object):
    """
    Class for Trie tree
    """
    def __init__(self):
        self.root = TrieNode(None)
        
    def add_string(self, s):
        p = self.root
        for c in s:
            if c in p.children:
                p = p.children[c]
            else:
                child = TrieNode(None)
                p.children[c] = child
                p = child
        p.word = s
    
    def find(self, s):
        p = self.root
        for c in s:
            if c in p.children:
                p = p.children[c]
            else:
                return False
        return p.word is not None

    def start_with(self, prefix):
        ret = []
        p = self.root
        for c in prefix:
            if c in p.children:
                p = p.children[c]
            else:
                return ret
        stack = [p]
        while stack:
            node = stack.pop()
            if node.word is not None:
                ret.append(node.word)
            for p in node.children.values():
                stack.append(p)
        return ret

    def smallest__subset_prefix(self):
        """
        Find the smallest subset of the dictionary, which contains prefixes of all words in the dictionary
        :return: a list of strings
        """
        ret = []
        # DFS
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.word is not None:
                ret.append(node.word)
            else:
                for p in node.children.values():
                    stack.append(p)

        return ret


if __name__ == "__main__":
    t = Trie()
    t.add_string("foo")
    t.add_string("food")
    t.add_string("foot")
    t.add_string("zzzdevil")

    print("==== Find all strings start with the given prefix ===")
    prefix = "f"
    print("Prefix: %s" % prefix)
    print("Result: %s" % t.start_with('f'))
    print()

    print("==== Find smallest subset contains prefixes of all words ===")
    print("Result: %s" % t.smallest__subset_prefix())
