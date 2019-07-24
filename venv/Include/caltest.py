import time
from appium import webdriver

def setUp(self):
    desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '8.0',  # 系统版本号
                        'deviceName': '864f0d23',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.zui.calculator',  # apk的包名
                        'appActivity': 'com.zui.calculator.Calculator'  # activity 名称
                 }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
    driver.implicitly_wait(8)

if __name__ =="__main__":
    desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '8.0.0',  # 系统版本号
                        'deviceName': '864f0d23',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.zui.calculator',  # apk的包名
                        'appActivity': 'com.zui.calculator.Calculator'  # activity 名称
                 }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
    driver.implicitly_wait(8)


    driver.find_element_by_name('7').click();
    driver.find_element_by_name('+').click();
    driver.find_element_by_name('9').click();
    driver.find_element_by_name('=').click();

    time.sleep(3);

    driver.quit();