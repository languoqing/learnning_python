import java.util.Arrays;

import comm.RPrint;

public class Hw{
	
	public boolean findNum(int min,int max,int targetNum,int[] nums) {
		System.out.println("接收参数：min++"+min+"+++max++++"+max);
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
	


	public static void main(String[] args) {
		int [] a = {2,3,1,7,9,44,32};
		int [] b = a.clone();
		Hw h = new Hw();
		boolean T;
		T= h.findNum(0,a.length-1,32,a);
		System.out.println(T);
		System.out.println("a++++++"+Arrays.toString(a));
		System.out.println("b++++++"+Arrays.toString(b));
	}
}
	

