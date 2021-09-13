# -*- coding:utf-8 -*-

from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from common.basePage import BasePage
from util.log import logs


log = logs()
class aTest_Download(BasePage) :

    def setup_class(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        log.info('初始化浏览器')

        sleep(1)

    def teardown_class(self) :
        self.driver.quit()


    # 测试报告中的场景名称
    @allure.feature('测试登录成功')
    # 测试登录成功的用例
    @pytest.mark.run(order=3)
    @pytest.mark.dependency()  # 这是依赖关系装饰器
    # 校情概况-疫情打卡
    def test_download(self):
        """
        疫情打卡的下载
        :return:
        """
        pass