""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
"""
from __future__ import annotations
from hashlib import new
from http.client import CONFLICT
__author__ = 'Brendon Taylor. Modified by Graeme Gange, Alexey Ignatiev, and Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'


from referential_array import ArrayR
from typing import TypeVar, Generic
from primes import LargestPrimeIterator
T = TypeVar('T')



class LinearProbeTable(Generic[T]):
    """
        Linear Probe Table.

        attributes:
            count: number of elements in the hash table
            table: used to represent our internal array
            tablesize: current size of the hash table
            conflict_count: the number of times an insertion of an element met a conflict
            probe_total: the total number of elements traversed by linear probing
            probe_max: the largest number of elements in a chain
            rehash_count: the number of times that the table has been rehashed

    """

    def __init__(self, expected_size: int, tablesize_override: int = -1) -> None:
        
        """
            Initialiser for the hash table:

            Best case: O(1)
            Worst case: O(P), where P is the complexity of finding the next prime
        """

        self.count = 0
        self.conflict_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0

        if tablesize_override == -1:
            self.primeIterator = LargestPrimeIterator(expected_size*3,3)
            self.tableSize = self.primeIterator.__next__()
        else:
            self.primeIterator = LargestPrimeIterator(tablesize_override,3)
            self.tableSize = tablesize_override
        self.table = ArrayR(self.tableSize)
           
        
        

    def hash(self, key: str) -> int:
        """
            Hash a key for insertion into the hashtable.
            Complexity: O(N), where n is the length of the key
        """
        hashKey = 0
        for index in range(len(key)):
            hashKey += ord(key[index])*29**index
            hashKey = hashKey % self.tableSize
        return int(hashKey)

    def statistics(self) -> tuple:
        """
            Returns various statistics about the table
            Complexity: O(1)
        """
        return (self.conflict_count,self.probe_total,self.probe_max,self.rehash_count)

    def __len__(self) -> int:
        """
            Returns number of elements in the hash table
            :complexity: O(1)
        """
        return self.count

    def _linear_probe(self, key: str, is_insert: bool) -> int:
        """
            Find the correct position for this key in the hash table using linear probing
            :complexity best: O(K) first position is empty
                            where K is the size of the key
            :complexity worst: O(K + N) when we've searched the entire table
                            where N is the tablesize
            :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash

        if is_insert and self.is_full():
            raise KeyError(key)

        chainStart = self.probe_total
        conflicted = False
        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    self.probe_max=max(self.probe_max,self.probe_total - chainStart)
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                self.probe_max=max(self.probe_max,self.probe_total - chainStart)
                return position
            else:  # there is something but not the key, try next
                if not conflicted:
                    self.conflict_count += 1
                    conflicted = True
                position = (position + 1) % len(self.table)
                self.probe_total += 1

        raise KeyError(key)

    def keys(self) -> list[str]:
        """
            Returns all keys in the hash table.
            Complexity: O(N)
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][0])
        return res

    def values(self) -> list[T]:
        """
            Returns all values in the hash table.
            Complexity: O(N)
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][1])
        return res

    def __contains__(self, key: str) -> bool:
        """
            Checks to see if the given key is in the Hash Table
            :see: #self.__getitem__(self, key: str)

            Complexity: O(1)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
            Get the item at a certain key
            :see: #self._linear_probe(key: str, is_insert: bool)
            :raises KeyError: when the item doesn't exist

            Best case: O(1)
            Worst case: O(N)
        """
        position = self._linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
            Set an (key, data) pair in our hash table
            :see: #self._linear_probe(key: str, is_insert: bool)
            :see: #self.__contains__(key: str)

            Best case: O(1)
            Worst case: O(N)
        """
        if self.count > 0.5*self.tableSize:
            self._rehash()

        position = self._linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1

        self.table[position] = (key, data)

    def is_empty(self):
        """
            Returns whether the hash table is empty
            :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
            Returns whether the hash table is full
            :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
            Utility method to call our setitem method
            :see: #__setitem__(self, key: str, data: T)

            Best case: O(1)
            Worst case: O(N)
        """
        self[key] = data

    def _rehash(self) -> None:
        
        """
            Method to rehash the table

            Complexity: O(N)
        """

        newTable = LinearProbeTable(self.primeIterator.__next__())
        for index in range(self.tableSize):
            if self.table[index] != None:
                (key,data) = self.table[index]
                newTable[str(key)] = data
        self.count = newTable.count
        self.table = newTable.table
        self.tableSize = newTable.tableSize
        self.rehash_count += 1
        self.conflict_count += newTable.conflict_count
        self.probe_total += newTable.probe_total
        self.probe_max = max(self.probe_max,newTable.probe_max)
        



    def __str__(self) -> str:
        """
            Returns all they key/value pairs in our hash table (no particular
            order).
            :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

if __name__ == "__main__":
    with open('aust_cities.txt') as f:
        table = LinearProbeTable(100,1000)
        lines = f.readlines()
        for line in lines:
            line = line[0:-2]
            table[line] = line
        print(table.statistics())