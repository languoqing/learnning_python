package PageTest;

import DataParams.SearchData;
import DataParams.SelectData;
import driver.Driver;
import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import pages.MainPage;
import pages.SearchPage;

import java.util.ArrayList;

import java.util.List;

public class SearchTest {

    static MainPage mainPage;
    static SearchPage seacherPage;
    @BeforeClass
    public static void beforAll(){
        mainPage = MainPage.goMainPage();
        seacherPage = mainPage.goSearchPage();
    }

    @Test(dataProvider = "seacherData",dataProviderClass = SearchData.class)
    public void findStockTest(String Stockname, String excpt){
        ArrayList<String> re = new ArrayList<String>();
        List<AndroidElement> stocks = seacherPage.findStock(Stockname);
        for(int i=0;i<stocks.size();i++){
            String ElementText = stocks.get(i).getText();
            re.add(ElementText);
        }
        Assert.assertTrue(re.contains(excpt));

    }

    @Test(dataProvider = "selectedTest",dataProviderClass = SelectData.class)
    public void isSelectedTest(String StockName,String excpt){
        ArrayList<String> Elements = seacherPage.isSelected(StockName);
        Assert.assertTrue(Elements.contains(excpt));

    }

    @AfterClass
    public static void afterAll(){
        Driver.quit();
    }
}
