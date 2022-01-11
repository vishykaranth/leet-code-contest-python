# https://leetcode.com/contest/weekly-contest-247/problems/maximum-product-difference-between-two-pairs/

class Solution:
    def maxProductDifference(self, nums) : int
        nums
        Arrays.sort(nums);
        int n = nums.length;
        return nums[n-1]*nums[n-2] - nums[0] * nums[1];


