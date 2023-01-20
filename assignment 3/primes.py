""""""

from __future__ import annotations


__author__ = ''
__docformat__ = 'reStructuredText'


class LargestPrimeIterator():

    """
        An itteratable class to generate repeatedly higher primes within an increasing bound
    """

    def __init__(self,upper_bound,factor):
        """
            Initialises the attriubutes for the object
            
            Complexity: O(1)
        """

        self.upper_bound = upper_bound
        self.factor = factor
        self.highest_prime = 2
    
    def __next__(self):

        """
            Method for finding the next highest prime between two primes

            Complexity: O(N^2) where N is the upper bound
        """
        
        for number in range(self.highest_prime, self.upper_bound):
            is_prime = True
            for factor in range(2,number):
                if number % factor == 0:
                    is_prime = False
                    break
            if is_prime:
                self.highest_prime = number
        self.upper_bound = self.highest_prime * self.factor
        return self.highest_prime
    
    def __iter__(self):
        return self


if __name__ == "__main__":
    a = LargestPrimeIterator(10000,3)
    print(a.__next__())
