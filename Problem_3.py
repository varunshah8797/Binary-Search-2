# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:26:29 2021

@author: User
"""



def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums)==0):
        return -1
    low=0
    high=len(nums)-1
    while(low<=high):
        mid=int(low+(high-low)/2)
        
        if((mid == 0 or nums[mid]>nums[mid-1]) and (mid == (len(nums)-1) or nums[mid]>nums[mid+1])):
            print(mid)
            return mid
        elif(mid!=0 and nums[mid]<nums[mid-1]):
            high=mid-1
        else:
            low=mid+1
    return 1112

