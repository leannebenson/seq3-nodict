#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'LeanneBenson'


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])


    def add(self, key, value=None):
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for key_value in bucket:
            if key_value == new_node:
                bucket.remove(key_value)
                break
        bucket.append(new_node)

    def get(self, key):
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for each in bucket:
            if each == key_val:
                return each.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        self.add(key, value)
