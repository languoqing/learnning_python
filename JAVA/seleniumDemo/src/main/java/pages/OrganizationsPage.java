package pages;

import driver.Driver;
import org.openqa.selenium.By;

public class OrganizationsPage {
    //单个社区的定位
    By locSingleOrganization = By.xpath("//*[@id=\"hot_teams\"]/div[2]/div/div[1]/div/div[1]/a/img");
    public SingleOrganizationPage goSigleOriganzationPage(){
        try{
            Thread.sleep(2000);
        }catch (Exception e){
            System.out.println("sddd");
        }

        Driver.getDriver().findElement(locSingleOrganization).click();
        return new SingleOrganizationPage();
    }
}
