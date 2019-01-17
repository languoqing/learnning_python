package PageTest;

import DataParams.ZiXuanData;
import driver.Driver;
import org.testng.Assert;
import org.testng.annotations.*;
import pages.DetailsPage;
import pages.MainPage;
import pages.SearchPage;
import pages.ZiXuanPage;

public class ZiXuanTest {

    public static MainPage mainPage;
    public static SearchPage searchPage;
    public static DetailsPage detailsPage;
    @BeforeClass
     static void Pags(){
        mainPage = MainPage.goMainPage();
        searchPage = mainPage.goSearchPage();
    }

    /**
     * 添加自选
     *
     */
    @Test(dataProvider = "ziXuanData",dataProviderClass = ZiXuanData.class)
     void addZiXuanTest(String Stock){
        DetailsPage detailsPage = searchPage.goDetailsPage(Stock);
        boolean b = detailsPage.addZixuan();
        Assert.assertTrue(b);
    }

    @Test(dataProvider = "ziXuanData",dataProviderClass = ZiXuanData.class)
     void deleteZiXuanTest(String Stock){
        DetailsPage detailsPage = searchPage.goDetailsPage(Stock);
        boolean b = detailsPage.deleteZixuan();
        Assert.assertTrue(b);

    }

    @AfterClass
     static void closeDriver(){
        Driver.quit();
    }
}