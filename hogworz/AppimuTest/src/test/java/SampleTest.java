import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;

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
            MobileElement el1 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout");
            el1.click();
            MobileElement el2 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView");
            el2.click();
            MobileElement el3 = (MobileElement) driver.findElementById("com.xueqiu.android:id/image");
            el3.click();
        }

        @After
        public void tearDown() {
            driver.quit();
        }

}
