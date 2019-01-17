package pages;

import org.openqa.selenium.By;

public class ZiXuanPage extends BasePage{


    /**
     * 到股票详情页
     *
     * @return
     */
    public DetailsPage goDetailsPage(String StockName){
        By Stock = useLoc("//*[text="+StockName+"]");
        find(Stock).click();
        return new DetailsPage();
    }

}
