package pages;

import driver.Driver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;


import java.util.List;
import java.util.Random;

public class SingleOrganizationPage {
    //所有帖子
    By TieZi = By.xpath("//div[@class='panel topics']/div[@class='panel-body']/div[@class='topic media topic-17904']/div[@class='infos media-body']/div[@class='title media-heading']");

    public TieziDetailesPage goTieziPage(){
        try{
            Thread.sleep(2000);
        }catch (Exception e){
            System.out.println("addff");
        }
        Driver.getDriver().findElement(TieZi).click();
        //随机取一个帖子
//        Random random = new Random();
//        int n = random.nextInt(locTieZi.size());
//        locTieZi.get(n).click();
        return new TieziDetailesPage();
    }
}

