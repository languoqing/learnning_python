package DataParams;

import org.testng.annotations.DataProvider;

public class SelectData {

    @DataProvider
    public Object[][] selectedTest(){
        return new Object[][]{
                {"pdd","com.xueqiu.android:id/follow_btn"}
        };
    }
}
