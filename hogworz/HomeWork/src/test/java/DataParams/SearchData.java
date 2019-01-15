package DataParams;


import org.testng.annotations.DataProvider;

public class SearchData {

    @DataProvider
    public Object[][] seacherData(){
        return new Object[][]{
                {"pdd","拼多多"},
                {"al","阿里"}
        };
    }
}
