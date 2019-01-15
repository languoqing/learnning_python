package pages;

import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.By;
import driver.Driver;
import org.openqa.selenium.WebElement;

import java.util.List;

public class SearchPage extends BasePage{
    //搜索框
    By seacherInput = useLoc("search_input_text");
    By seacherHitory = useLoc("stockName");


    public List<AndroidElement> findStock(String key){
        find(seacherInput).sendKeys(key);
        List<AndroidElement> seacheResult = Driver.getdriver().findElements(seacherHitory);
        System.out.print(seacheResult.get(0).getText());
        return seacheResult;
    }
}
