# -*- coding:utf-8 -*-
from pathlib import Path
import allure
import pytest
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By

from common.basePage import BasePage
from util.log import logs


class Test_login_error(BasePage) :

    def setup_class(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.log = logs()
        self.log.info('初始化浏览器')

        sleep(1)

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_o
    # ptions = chrome_options)
    # self.driver.maximize_window()
    # sleep(1)

    @pytest.mark.run(order=2)  # 运行先后顺序
    # @pytest.mark.dependency(depends=['test_login_ok'])  # 这是依赖关系装饰器

    # 测试登录失败的用例
    def test_login_error_2(self) :
        # 测试数据
        url = 'http://192.168.101.101:7061/login'
        user = '1370720329'
        pwd = '为空'
        print('1111')
        loc = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[1]/div/div/input')  # 输入用户
        loc2 = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[2]/div/div/input')  # 输入密码
        loc3 = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[3]/div/button/span')  # 登录按钮
        self.log.debug('test2登录的URL是：%s', format(url))
        self.log.debug('test2登录的账号是：%s', format(user))
        self.log.debug('test2登录的密码是：%s', format(pwd))
        try :
            # 测试步骤
            self.driver.get(url)
            self.input_text(user, *loc)
            self.input_text(pwd, *loc2)
            self.clicks(*loc3)
            self.clear(user)
            sleep(6)
            # 日志信息
            # self.log.error('test2登录的URL是：%s', format(url))
            # self.log.error('test2登录的账号是：%s', format(user))
            # self.log.error('test2登录的密码是：%s', format(pwd))

        except Exception as ae :
            print('测试错误的账户或者密码登录失败', ae)

        else :
            print('错误的密码登录成功，请测试人员检查！')
            # 截图
            self.driver.get_screenshot_as_file('E:\Python脚本文件夹\my_selenium_projrct\screenshots\error.png')
            # self.driver.save_screenshot('./screenshots/1.png')
            allure.attach.file('E:\Python脚本文件夹\my_selenium_projrct\screenshots\error.png', name='error',
                               attachment_type=allure.attachment_type.PNG)

    def teardown_class(self) :
        self.driver.quit()
