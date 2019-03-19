package comm;
import java.util.Arrays; 

public class RPrint {
	/*
	 * 把打印方法封装一遍，
	 */
	
	public static void rPrint(int i) {
		System.out.print(i);
	}
	
	public static void rPrint(String i) {
		System.out.print(i);
	}
	
	public static void rPrint(int[] i) {
		System.out.print(Arrays.toString(i));
	}
}
