package com.languoqing;

public class Dengyao {
	
	public static void main(String [] args){
		//getZhijiao(4,1);
		printXing(4);
	}
	
/**
 * ��ӡ **
 */
	public static void printXing(int changdu){
		int m = 0;
		for ( m = 1; m<changdu;m++){
			
			for(int xing = 0; xing<m;xing++){
				//��ӡ�ո�
				System.out.print("*");
				System.out.print("m"+m);
			}
			System.out.println();
		}
		
	}
	
	/**
	 * ��ӡ�ո�
	 */
	
	public static void printSpace(int changdu){
		
		for (int m = changdu; m>0;m--){
			
			for(int space = m-1; space>0;space--){
				//��ӡ�ո�
				System.out.print("+");
			}
			System.out.println();
		}
	}
	/**
	 * 
	 * @param changdu
	 * @param type 1:ֱ�ǣ�2����ֱ��
	 */
	public static void getZhijiao(int changdu,int type){
		
		//���������� 4*4
		//����ѭ������ ->��
		if(type == 1){
			for (int m = 1; m<=changdu;m++){
				//��ӡ*
				for(int xing=m;xing>0;xing--){
					System.out.print("*");
				}
				System.out.println("");
			}
		}
		if(type == 2){
			for (int m = changdu; m>0;m--){
				//��ӡ*
				for(int xing=0;xing<m;xing++){
					System.out.print("*");
				}
				System.out.println("");
			}
		}
	}
	
	/**
	 * �ȱ�
	 * @param changdu
	 * @param type 1:���ȱߣ�2���ȱ�
	 */
	
	public static void getDengyao(int changdu,int type){
		
		if(type == 1){
			//����ѭ������->��
			for(int high=0;high<=changdu;high++){
				//��ӡÿ�пո�
				for(int a =changdu-high;a>0;a--){
					System.out.print(" ");
				
				}
				//��ӡ*
				for(int xing =high;xing>0;xing--){
				System.out.print("*"+" ");
	
				}
			System.out.println();
			}
		}
		if (type == 2){
			for(int high=changdu;high>0;high--){
				for(int a =changdu-high;a>0;a--){
					System.out.print(" ");
				
				}
				for(int xing =high;xing>0;xing--){
				System.out.print("*"+" ");
	
				}
			System.out.println();
			}
			
		}
	}
			
		/**
		 * 
		 * @param changdu
		 * @param type ����ȥ���ø��ȱ������ε��ر�
		 */
	public static void getLengxing(int changdu,int type){
		//���ȱ�������
		getDengyao(changdu,type);
		//���ȱ������Σ����ظ���ȥ��
		for(int high=changdu-1;high>0;high--){
			for(int a =changdu-high;a>0;a--){
				System.out.print(" ");
			
			}
			for(int xing =high;xing>0;xing--){
			System.out.print("*"+" ");

			}
		System.out.println();
		}
		
	}
	
	
	
	public static void getPingxingSibian(int changdu) {
		//���Ƹ߶�
		for(int high = changdu ; high>0;high-- ){
			//��ӡ�ո�
			for(int space = high;space >0;space--){
				System.out.print(" ");
				
			}
			for(int xing = changdu;xing>0;xing--){
				System.out.print("*"+" ");
			}
			System.out.println();
		}
		
	}		
		
		
		
	}
	
	
	
	
	
	
	
	
	

