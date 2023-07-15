'''
Given a nums array: nums = [1, 2, 3]
Return all possible subsets
We start with an empty array: result = [[]]
We use recursion: def recurse(index, currArr)
Index: current index keeping track of current number
currArr to build up the subset
'''
def subsets(nums):
    result = [[]]    
    def recurse(index, currArr):        
        for i in range(index, len(nums)):
            currArr.append(nums[i])
            result.append(currArr.copy())
            recurse(i+1, currArr)
            currArr.pop()

    recurse(0, [])
    return result

from unittest import TestCase
import unittest

# Test cases
class PowersetTest(TestCase):
    def test1(self):        
        result1 = subsets([1, 2, 3])
        expected1 = [[], [1], [1,2], [1,2,3], [1, 3], [2], [2,3], [3]] 
        self.assertEqual(expected1, result1)

unittest.main()
