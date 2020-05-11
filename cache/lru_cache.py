from typing import Union


class Node:

    __slots__ = ['result', 'next', 'prev']

    def __init__(self, result: int, next: int, prev: int) -> None:
        self.result = result
        self.next = next
        self.prev = prev


class LRUCache:
    '''Yep, I know about OrderedDict.
    Here I tried something like dict + circular doubly linked list'''

    __slots__ = ['capacity', 'cache', 'head', 'tail']

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head: int = 0
        self.tail: int = 0

    def _unlink_node(self, node: Node, key: int):
        prev_, next_ = node.prev, node.next
        if self.tail == key:
            # change tail
            self.tail = next_
        else:
            # remove from the middle
            self.cache[next_].prev = prev_
            self.cache[prev_].next = next_

    def get(self, key: int) -> int:
        existed = self.cache.get(key)
        if existed:
            if self.head == key:
                return existed.result
            self._unlink_node(existed, key)
            self.cache[key].prev = self.head
            self.cache[key].next = self.tail
            self.cache[self.head].next = key
            self.head = key
            self.cache[self.tail].prev = key
            return existed.result
        else:
            return -1

    def put(self, key: int, result: int) -> None:
        if not self.head or self.capacity == 1:
            self.head = key
            self.tail = key
            self.cache = {key: Node(result=result,
                                    prev=self.head,
                                    next=self.tail)}
            return

        existed = self.cache.get(key)
        if existed:
            if self.head == key:
                # just update head
                self.cache[key].result = result
                return
            self._unlink_node(existed, key)
        else:
            if len(self.cache) == self.capacity:
                self.tail = self.cache.pop(self.tail).next
        value = Node(result=result, prev=self.head, next=self.tail)
        self.cache[self.head].next = key
        self.head = key
        self.cache[self.tail].prev = key
        self.cache[key] = value
