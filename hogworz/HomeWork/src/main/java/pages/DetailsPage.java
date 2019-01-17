package pages;

import driver.Driver;
import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.By;

import java.util.List;

public class DetailsPage extends BasePage{

    //底部bar
    By Bar = useLoc("floating_action_view");
    //加自选成功 设自选
    By SetZixuan = useLoc("//*[@text='设自选']");
    By AddZixuan = useLoc("//*[@text='加自选']");
    By DeleteZixuan = useLoc("//*[@text='删除自选']");

    /**
     * 添加自选(需要确保定位元素操作没问题，不然会有bug)
     */
    public boolean addZixuan(){
        boolean re = false;

        try{
            find(AddZixuan).click();
            if(find(SetZixuan) != null){
                re = true;
            }else {re = false;}
        }catch (Exception e){
            System.out.println("AddZixuan元素查找有问题");
        }
        return re;
    }

    public boolean deleteZixuan(){

        boolean re = false;
        try{
            find(SetZixuan).click();
            find(DeleteZixuan).click();
            if(find(AddZixuan) != null){
                re = true;
            }else {re = false;}
        }catch (Exception e){
            System.out.print("AddZixuan元素查找有问题");
        }
        return re;
    }

}
