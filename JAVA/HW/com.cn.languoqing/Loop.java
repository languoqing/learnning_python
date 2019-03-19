import java.util.Arrays;
import comm.RPrint;


public class Loop{
	/*
	 * ц╟ещеепР
	 */
	int[] c = {2,4,1,6,3,9};
	int[] maoPaoSort(int[] arr) {
		for(int i=0;i<=arr.length-1;i++) {
			for(int j=0;j<=i;j++) {
				if(arr[j] > arr[i]) {
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		return arr;
	}
	
	/*
	 * main()
	 * 
	 */
	public static void main(String[] args) {
		Loop a = new Loop();
		int[] b;
		b = a.maoPaoSort(a.c);
		RPrint.rPrint(b);
		/* System.out.print(Arrays.toString(b)); */
		/*
		 * for(int i=0;i<b.length;i++) { System.out.print(b[i]); }
		 */
		
	}
}

