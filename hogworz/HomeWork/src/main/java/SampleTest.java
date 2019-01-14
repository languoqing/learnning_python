import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import junit.framework.TestCase;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import java.net.MalformedURLException;
import java.net.URL;
import org.openqa.selenium.remote.DesiredCapabilities;

public class SampleTest {

    private AndroidDriver driver;

    @Before
    public void setUp() throws MalformedURLException {
        DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
        desiredCapabilities.setCapability("platformName", "ANDROID");
        desiredCapabilities.setCapability("platformVersion", "8.1.0");
        desiredCapabilities.setCapability("deviceName", "vivo Y85A");
        desiredCapabilities.setCapability("app", "com.xueqiu.android");
        desiredCapabilities.setCapability("noReset", true);
        desiredCapabilities.setCapability("udid", "7bff6865");
        desiredCapabilities.setCapability("appActivity", ".view.WelcomeActivityAlias ");

        URL remoteUrl = new URL("http://172.21.12.105:4723/wd/hub");

        driver = new AndroidDriver(remoteUrl, desiredCapabilities);
    }

    @Test
    public void sampleTest() {
        MobileElement undefined = (MobileElement) driver.findElementByAccessibilityId("转到上一层级");
        undefined.clear();
    }

    @After
    public void tearDown() {
        driver.quit();
    }
}
