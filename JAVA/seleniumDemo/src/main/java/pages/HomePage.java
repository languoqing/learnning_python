package pages;
import driver.Driver;
import org.openqa.selenium.By;

public class HomePage {
    static String HomeUrl = "https://testerhome.com/";
    //社区定位
    By locOrganizations = By.xpath("//*[@id=\"main-nav-menu\"]/ul/li[4]");
    public static HomePage goHomePage(){
        Driver.initDriver();
        Driver.getDriver().get(HomeUrl);
        return new HomePage();
    }

    public OrganizationsPage goOrganizations(){

        Driver.getDriver().findElement(locOrganizations).click();
        return new OrganizationsPage();
    }
}

