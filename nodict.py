#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = '???'


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = None
        # Your code here

    def __repr__(self):
        # Your code here
        return

    def add(self, key, value):
        # Your code here
        return

    def get(self, key):
        # Your code here
        return

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return
