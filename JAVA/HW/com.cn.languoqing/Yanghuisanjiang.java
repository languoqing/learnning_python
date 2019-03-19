
public class Yanghuisanjiang {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//定义一个多维数组，控制行和行里面的单个元素
		getResult(6);
	
	}
	
	
	/**
	 * @param arg
	 */
	
	//需要给数组初始化数据
	public static void getResult(int arg){
		
		int [][] arry = new int [arg][arg];
		
		//遍历行数
		for(int hang =0;hang <arg;hang++){
			
			//取行里面的元素
			for(int yuansu=0;yuansu<=hang;yuansu++){
				if(yuansu == 0){
					arry[hang][yuansu] = 1;
				}else if(hang == yuansu){
					arry[hang][yuansu] = 1;
				}else {
					arry[hang][yuansu] = arry[hang-1][yuansu-1] + arry[hang-1][yuansu];
				}
				System.out.print(arry[hang][yuansu]+" ");
				
			}
			System.out.println();
		}
	}	

}