package leetcode;

import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
    	int [] re = null;
    	int [] sortArr = nums.clone();
        for(int i=0;i<nums.length;i++) {
        	int reNum;
        	reNum = target - nums[i];
        	if(findNum(0,sortArr.length-1,reNum,sortArr)) {
        		if(i == indexOf(reNum,nums)) {
        			continue;
        		}else {
        		int[] reTemp = {i,indexOf(reNum,nums)};
        		re = reTemp;
        		return re;
        			}
        		}
        	
        }
        return re;
    }
    /*
     * 	二分查找  binarySearch
     */
    public static boolean findNum(int min,int max,int targetNum,int[] nums) {
		System.out.println("接收参数：min++"+min+"+++max++++"+max+"tragetNum"+targetNum);
		Arrays.sort(nums);
		System.out.println("nums+++++++"+Arrays.toString(nums));
		
		while(min<=max){
		int middle = (min + max) / 2;
		System.out.println("min++"+min+"+++max++++"+max+"++++middle+++++"+middle);
		if (targetNum == nums[middle]) {
			System.out.println("got it");
			return true;
		}else if(targetNum < nums[middle]) {
			max = middle - 1;
			findNum(min,max,targetNum,nums);
		}else if(targetNum > nums[middle]){
			min = middle + 1;
			findNum(min,max,targetNum,nums);
		}
		
		}
		return false;
	}
    
    /*
     *	 返回元素索引
     */
    public static int indexOf(int tar,int[] arr) {
    	System.out.println("接收参数：tar++"+tar+"arr{}+==="+Arrays.toString(arr));
    		for(int i=0;i<arr.length;i++) {
        		if(arr[i] == tar) {
        			System.out.println("index++"+i);
        			return i;
        		}
        	}
    		return -1;
    }
    
    public static void main(String[] asrgs) {
    	int[] nums = {3,3};
    	Solution obj = new Solution();
    	int[] re = obj.twoSum(nums, 6);
    	System.out.println(Arrays.toString(re));
    }
}
