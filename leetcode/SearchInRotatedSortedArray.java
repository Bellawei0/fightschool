// Leecode 33. Search in Rotated Sorted Array
// You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
// Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

// If target is found in the array return its index, otherwise, return -1.
// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

// recursion
class Solution {
    public int search(int[] nums, int target) {
        return search(nums,target,0,nums.length-1);    
    }
    
    private int search(int[] nums, int target,int left, int right){
       if(right < left) 
           return -1;
        
        int middle = left +(right -left) /2;
        
        if (nums[middle] == target)
            return middle;
        
        if(nums[middle] >= nums[left]){
            if(target >= nums[left] && target < nums[middle])
                return search(nums,target,left,middle-1);
            return search(nums,target,middle+1,right);    
        }else{
            if(target <= nums[right] && target > nums[middle])
                return search(nums,target,middle+1, right);
            return search(nums,target,left,middle-1);
        }              
    }
}


// Iteration 
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length-1;
        
        while(left <= right){
            int middle = left + (right-left)/2;
            
            if(nums[middle] == target)
                return middle;
            
            if(nums[middle] >= nums[left]){
                if(target >= nums[left] && target < nums[middle])
                    right = middle -1;
                else
                    left  = left +1; 
            }else{
                if(target <= nums[right] && target > nums[middle])
                    left = middle+1;
                else
                    right = middle -1;
            }
        }      
        return -1; 
    }
}