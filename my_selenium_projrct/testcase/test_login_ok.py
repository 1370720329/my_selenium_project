# -*- coding:utf-8 -*-


from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from common.basePage import BasePage
from util.log import logs





class Test_login(BasePage) :

    def setup_class(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.log = logs()
        self.log.info('初始化浏览器')

        sleep(1)

    def teardown_class(self) :
        self.driver.quit()
    # 测试报告中的场景名称
    @allure.feature('测试登录成功')
    # 测试登录成功的用例
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()  # 这是依赖关系装饰器

    def test_login_ok(self) :
        # 测试数据
        loc = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[1]/div/div/input')  # 输入用户
        loc2 = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[2]/div/div/input')  # 输入密码
        loc3 = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[3]/div/button/span')  # 登录按钮
        self.driver.implicitly_wait(5)
        url = 'http://192.168.101.101:7061/login'
        user = '1370720329'
        pwd = '1370720329'

        # 测试代码
        # 测试报告中的步骤
        with allure.step('登录页面') :
            self.driver.get(url)

        with allure.step('输入账号') :
            self.input_text(user, *loc)

        with allure.step('输入密码') :
            self.input_text(pwd, *loc2)

        with allure.step('点击登录') :
            self.clicks(*loc3)
        sleep(5)
        # 日志信息
        self.log.debug('test1登录的URL是：%s', format(url))
        self.log.debug('test1登录的账号是：%s', format(user))
        self.log.debug('test1登录的密码是：%s', format(pwd))

        # 根据登录后的页面标题判断是否登录成功
        try :
            # a = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div/span').text

            a = self.get_title()
            print(a)
            assert '高校大数据治理业务平台' == a

        except Exception as b :
            self.log.error('登录失败，请检查！', b)
            sleep(1)
            self.driver.get_screenshot_as_file('E:\Python脚本文件夹\my_selenium_projrct\screenshots\error.png')
            allure.attach.file('E:\Python脚本文件夹\my_selenium_projrct\screenshots\error.png', name='error', attachment_type=allure.attachment_type.PNG)


# if __name__ == '__main__':
#     pytest.main(['test_login_ok.py'])
