package PageTest;

import org.junit.Test;
import driver.Driver;

import java.net.MalformedURLException;

public class DriverTest {
    @Test
    public void DriverTest(){
        try {
            Driver.start();
        }catch (MalformedURLException e){
            e.printStackTrace();
        }
        finally {
            Driver.quit();
        }
    }
}
