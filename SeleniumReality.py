import time
import subprocess, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeReality:

    def __init__(self):
        # 配置真实浏览器环境
        self.chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # 1. 指定本地浏览器绝对路径
        self.remote_debugging_port = random.randint(9222, 9999)  # 2. 指定浏览器启动端口
        self.user_data_dir = r'C:\Users\xxx\Desktop\SeleniumUserData'  # 3. 指定浏览器的UserDataDir
        # 启动真实浏览器
        subprocess.Popen([
            self.chrome_path,
            f'--remote-debugging-port={self.remote_debugging_port}',
            f'--user-data-dir={self.user_data_dir}'
        ], shell=True)
        # 初始化浏览器参数以及接管真实浏览器
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{self.remote_debugging_port}")
        self.browser = webdriver.Chrome(options=self.chrome_options)


class SeleniumReality(ChromeReality):

    def __init__(self):
        super(SeleniumReality, self).__init__()
        self.url = 'https://passport.taobao.com/ac/password_find.htm?from_site=0'  # 淘宝找回验证码界面
        self.xiaoji_url = 'https://passport.taobao.com/ac/password_find.htm?from_site=2'  # 淘宝找回验证码界面 小鸡

    def taobao_slider(self):
        '''淘宝滑块'''
        for index in range(1):
            self.browser.get(self.url)
            # 定位滑块元素
            source = self.browser.find_element_by_id("nc_1_n1z")
            # 定义鼠标拖放动作并执行
            ActionChains(self.browser).drag_and_drop_by_offset(source, 280, 0).perform()

            # 延迟一下
            time.sleep(1)


if __name__ == '__main__':
    seleniumReality = SeleniumReality()
    # seleniumReality.taobao_slider()
