package com.languoqing;

public class Getdays {

	
/**
 * �ж��Ƿ�������
 * @param year
 * @return
 */
	public static boolean isRunnian(int year){
		if (year % 400 == 0 || (year % 4 == 0 && year % 100 !=0)){
			return true;
		}
		return false;
	}

/**
 * ��ȡ�·ݵ�����
 *
 */
   public static int getMonthDays(int year,int month){
	   
	   int months [] = new int []{1,3,5,7,8,10,12};
	   for (int i = 0; i < months.length; i++) {
		if (month == months[i]){
			return 31;
		}
		}
	   if (month == 2 && isRunnian(year) == true){
			return 29;
		}else if (month == 2 && isRunnian(year) == false){
			return 28;
		}else{
			return 30;
	}
   }
   
   /**��ȡ��ݵ�����
    * 
    * @param year
    * @return
    */
   public static int getYearDays(int year){
	   
	   if(isRunnian(year)){
		   return 366;
	   }
	   return 365;
	   
   }
 
   /**
    *��ȡ����δ��һ�²�ȫ������
    */
   public static int restDays(int year,int month,int day){
	   int rest_Days =0;
	   rest_Days = getMonthDays(year, month) - day;
	   return rest_Days;
   }
   
   
   /**
    * ��ȡ����һ�������
    */
   public static int getNotFulldays(int year,int month,int day){
	   
	   int rest_fullDays = 0;
	   for(int m = 1 ; m<month; m++){
		   rest_fullDays = rest_fullDays + getMonthDays(year, m);
	   }
	   rest_fullDays = rest_fullDays + day;
	   return rest_fullDays;
   }
   
   
  /**
   * ��ȡ����δ��һ�겹ȫ�µ�����
   */
   public static int restMonthDays(int year,int month,int day){
	   //��ȡ����ʣ������
	   int restMonth = 0;
	   restMonth = 12 - month ;
	   
	   //��ʣ������������
	   int rest_MonthDays =0;
	   for (int m = 0;m <restMonth;m++,month++){
		   rest_MonthDays = rest_MonthDays + getMonthDays(year, month);
	   }
	   return rest_MonthDays;
	   
   }
   
 
   
   
/**
 * ��ȡ���,����ʱ���м�Ĳ�ֵ
 */
   
   
   public static int getdays(int year1,int month1,int day1,int year2,int month2,int day2){
	   //year1 ��ȫ����
	   int year1_Days = 0;
	   year1_Days = restMonthDays(year1,month1,day1) + restDays(year1,month1,day1);
	   
	   //year2��ȫ����
	   int year2_Days = 0;
	   year2_Days = restMonthDays(year2,month1,day1) + restDays(year2,month1,day1);
	   
	   //�м侭����ݵ�����
	   int CountYear = year1 - year2+1;
	   int CountYearDays = 0;
	   //System.out.println("year2"+year2+",year1"+year1);
	   for (int y = 0; y < CountYear; y++,year2++) {
		   
		   CountYearDays = CountYearDays + getYearDays(year2);
	} 
//	   if (year1 > year2){
	   //ʵ��������ȫ��������ȥ�ಹȫ������
	   //�ж��·�
		   System.out.println("CountYearDays"+CountYearDays);
		   System.out.println("year1_Days"+year1_Days);
		   return CountYearDays-year1_Days-getNotFulldays( year2, month2, day2);
//	   }
//	   else {
		   
		   //System.out.println("CountYearDays"+CountYearDays);
		   //System.out.println("year2_Days"+year2_Days);
		   //return CountYearDays-year2_Days-getNotFulldays( year1, month1, day1);
	  
	   //}
	   
	   
   }
   
   
   
   
   
   
   public static void main(String [] args){
	   
	   System.out.println("�м��"+getdays(2016,6,5,1805,2,1));
	   System.out.println("С���ڲ�ȫ������"+getNotFulldays( 2015,12,20));
	   System.out.println("�����ڲ�ȫ������"+restMonthDays(2016,1,5));
	   
	   System.out.println("������������"+restDays(2019,1,5));
	   //System.out.println(getdays(2012,1,3,2011,12,29));
	   //System.out.println(getdays(2012,1,3,2011,12,29));
   }
   
   
}