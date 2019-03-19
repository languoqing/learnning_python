
import driver.Driver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.OrganizationsPage;
import pages.SingleOrganizationPage;
import pages.TieziDetailesPage;

public class ReadTieZiTest {

    static HomePage homePage;
    @BeforeClass
    void setup(){
        homePage = HomePage.goHomePage();
    }


    @Test
    void readTieziTest(){
        OrganizationsPage organizationsPage = homePage.goOrganizations();
        SingleOrganizationPage singleOrganizationPage = organizationsPage.goSigleOriganzationPage();
        singleOrganizationPage.goTieziPage();
        try{
            Thread.sleep(2000);
        }catch (Exception e){
            System.out.println("addff");
        }
        Assert.assertTrue(Driver.getDriver().getTitle().contains("登录"));

    }

    @AfterClass
    void teraDown(){
        Driver.getDriver().quit();
    }
}
