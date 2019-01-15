package driver;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.net.MalformedURLException;
import java.net.URL;

public class Driver {
    private static AndroidDriver<AndroidElement> driver;

    public static void start() throws MalformedURLException {
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

    public static AndroidDriver<AndroidElement> getdriver(){
        return driver;
    }

    public static void quit() {
        driver.quit();
    }
}
