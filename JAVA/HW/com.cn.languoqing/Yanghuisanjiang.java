
public class Yanghuisanjiang {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//����һ����ά���飬�����к�������ĵ���Ԫ��
		getResult(6);
	
	}
	
	
	/**
	 * @param arg
	 */
	
	//��Ҫ�������ʼ������
	public static void getResult(int arg){
		
		int [][] arry = new int [arg][arg];
		
		//��������
		for(int hang =0;hang <arg;hang++){
			
			//ȡ�������Ԫ��
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