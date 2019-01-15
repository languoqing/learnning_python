package pages;

import driver.Driver;
import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class BasePage {

    /**
     * 把findElement封装一下
     * @param loc
     * @return WebElement
     */
    public AndroidElement find(By loc){
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
