package pages;

import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.By;
import driver.Driver;
import org.openqa.selenium.NoSuchElementException;

import java.util.ArrayList;
import java.util.List;

public class SearchPage extends BasePage{
    //搜索框
    By seacherInput = useLoc("search_input_text");
    //搜索展示结果
    By seacherHitory = useLoc("stockName");
    //自选按钮:未选中、已选中
    By Select = useLoc("follow_btn");
    By Selected = useLoc("followed_btn");

    /**
     * 通过关键字查找股票
     * @param key
     * @return List<AndroidElement>
     */
    public List<AndroidElement> findStock(String key){
        find(seacherInput).sendKeys(key);
        List<AndroidElement> seacheResult = Driver.getdriver().findElements(seacherHitory);
        System.out.print(seacheResult.get(0).getText());
        return seacheResult;
    }

    /**
     * 股票查找出来后自选操作
     */
    public ArrayList<String> isSelected(String key){
        this.findStock(key);
        ArrayList<String> Elements = new ArrayList<String>();
        /*if(find(Select) == null){
            find(Selected).click();
            Elements.add(find(Select).getAttribute("resourceId"));
            find(Select).click();
            Elements.add(find(Selected).getAttribute("resourceId"));
        }else {
            find(Select).click();
            Elements.add(find(Selected).getAttribute("resourceId"));
            find(Selected).click();
            Elements.add(find(Select).getAttribute("resourceId"));
        }*/
        try{
            find(Selected).click();
            Elements.add(find(Select).getAttribute("resourceId"));
            find(Select).click();
            Elements.add(find(Selected).getAttribute("resourceId"));
        }catch (NoSuchElementException e){
            System.out.printf("有元素未找到");
            find(Select).click();
            Elements.add(find(Selected).getAttribute("resourceId"));
            find(Selected).click();
            Elements.add(find(Select).getAttribute("resourceId"));
        }
        return Elements;
    }

    /**
     * 去股票详情页
     */
    public DetailsPage goDetailsPage(String StockName){
         List<AndroidElement> SearchResult = this.findStock(StockName);
         SearchResult.get(0).click();
         return new DetailsPage();
    }
}

