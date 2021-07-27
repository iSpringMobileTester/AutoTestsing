from appium import webdriver
import time

desired_caps = dict(
    platformName='Android',
    platformVersion='10',
    # automationName='uiautomator2',
    deviceName='Google Pixel',
    autoGrantPermissions='true',
    # appPackage="com.ispring.islearn",
    # appActivity=".activity.MainTabActivity"
    # app='C:/Users/danila.urvantsev/Downloads/Cal.apk'
)

desired_caps2 = dict(
    platformName='Android',
    platformVersion='11',
    # automationName='uiautomator2',
    deviceName='Google Pixel 4 XL',
    autoGrantPermissions='true',
    # appPackage="com.ispring.islearn",
    # appActivity=".activity.MainTabActivity"
    # app='C:/Users/danila.urvantsev/Downloads/Cal.apk'
)


def test_sum_of_two_integers(acc_name):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # driver.launch_app()
    driver.startActivity("com.ispring.islearn", ".activity.MainTabActivity")
    # assert result['stdout'] == 'arg1 arg2'
    el2 = driver.find_element_by_id("com.ispring.islearn:id/accountUrl")
    el2.send_keys("roadsandpits.ispringlearn.ru")
    el3 = driver.find_element_by_id("com.ispring.islearn:id/enterAccountUrlButton")
    el3.click()
    time.sleep(1)
    el4 = driver.find_element_by_id("com.ispring.islearn:id/login")
    el4.send_keys(acc_name)
    el5 = driver.find_element_by_id("com.ispring.islearn:id/password")
    el5.send_keys("12345Q")
    el6 = driver.find_element_by_id("com.ispring.islearn:id/loginButton")
    el6.click()
    time.sleep(1)
    el7 = driver.find_element_by_id("com.ispring.islearn:id/placeForAvatar")
    el7.click()
    time.sleep(1)
    el8 = driver.find_element_by_id("com.ispring.islearn:id/userEmail")
    assert el8.get_attribute('text') == acc_name

    # driver.find_element_by_name('9').click()
    # driver.find_element_by_name('+').click()
    # driver.find_element_by_name('1').click()
    # driver.find_element_by_name('=').click()
    # numbers_field = driver.find_element_by_xpath('//XCUIElementTypeStaticText')
    # assert int(numbers_field.text) == 10
    # driver.quit()


# test_sum_of_two_integers("testlearn")

def chek_notifications():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps2)

    driver.open_notifications()

    findElementByName('iSpring Learn', driver)

    scrollAndClick('iSpring', driver)  # Можно не полное название

    # el2 = driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[4]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")
    # el2.click()


def scrollAndClick(visibleText, driver):
    driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                               "0)).scrollIntoView(new UiSelector().textContains(\"" + visibleText +
                                               "\").instance(0))").click()


def findElementByName(visibleText, driver):
    driver.find_element_by_xpath(
        "//android.widget.TextView[@text='" + visibleText + "']").click()  # Обязательно полное, идентичное название


chek_notifications()
