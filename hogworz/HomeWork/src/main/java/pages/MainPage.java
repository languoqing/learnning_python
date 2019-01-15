package pages;

import driver.Driver;
import org.openqa.selenium.By;

import java.net.MalformedURLException;
import java.sql.Time;
import java.util.concurrent.TimeUnit;

public class MainPage extends BasePage {

    By SeacherBar = useLoc("tv_search");

    /**
     * 启动driver ,到主页面
     * @return
     */
    public static MainPage goMainPage(){
        try{
            Driver.start();
            Driver.getdriver().manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        }catch (MalformedURLException e){
            e.printStackTrace();
        }
        return new MainPage();
    }

    /**
     * 从主页点击搜索框到搜索页面
     */
    public SearchPage goSearchPage(){
        find(SeacherBar).click();
        return new SearchPage();
    }

}
