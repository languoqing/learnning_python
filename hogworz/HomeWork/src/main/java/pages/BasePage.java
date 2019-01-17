package pages;

import driver.Driver;
import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.By;


public class BasePage {

    /**
     * 把findElement封装一下
     * @param loc
     * @return WebElement
     */
    public AndroidElement find(By loc){
        /*System.out.println("查找+++++"+loc);
        System.out.printf("元素："+loc+"=========="+Driver.getdriver().findElement(loc));*/
        return Driver.getdriver().findElement(loc);
    }

    /**
     * 确认查找xpth or id
     * @param loc
     * @return
     */
    public By useLoc(String loc){
        if(loc.matches("/.*")){
            return By.xpath(loc);
        }else{
            return By.id(loc);
        }
    }

}
