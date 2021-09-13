# -*- coding:utf-8 -*-
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from common.basePage import BasePage
from testcase import test_login_ok
from util.log import logs

import os

# 学生基本信息下载和下钻
class Test_Student_info_download(BasePage) :

    def setup_class(self,test_login_ok):
        self.login = test_login_ok
        # 0禁止弹出下载窗口
        self.chromeOptions  = test_login_ok.ChromeOptions()
        self.prefs = {
            "profile.default_content_settings.popups" : 0,
            "download.default_directory" : 'D:\download'}
        self.chromeOptions.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(chrome_options=self.chromeOptions )




        self.log = logs()
        self.log.debug('初始化浏览器')
        sleep(3)

    def teardown_class(self) :
        self.login.quit()

    @pytest.mark.dependency(test_login_ok)  # 这是依赖关系装饰器
    def test_sex(self):
        try:
            loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/aside/div[1]/ul/li[2]/div/span') # 点击思政大数据

            loc1 = (By.XPATH,'/html/body/div/div/div[2]/div[1]/aside/div[1]/ul/li[2]/ul/li/ul/li[1]/span') # 点击基本信息

            loc2 = (By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/span') # 模块：男女比例,下载按钮
            self.clicks(loc)

            self.clicks(loc1)
            sleep(2)
            self.clicks(loc2)
        except Exception as ae:
            print('定位元素失败，出错了',ae)






if __name__ == '__main__':
    pytest.main(['-sv'])