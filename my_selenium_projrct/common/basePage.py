# -*- coding:utf-8 -*-
"""
创建一个公共的基类提高代码重用
"""
from selenium import webdriver

from util.log import logs


class BasePage() :
    # 初始化浏览器
    def setup_class(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    # 查找元素  *loc定位器是一个多参需要放在最后
    def get_element(self, *loc) :
        return self.driver.find_element(*loc)

    # 输入文本
    def input_text(self, text, *loc) :
        self.get_element(*loc).send_keys(text)

    # 点击
    def clicks(self, *loc) :
        self.driver.find_element(*loc).click()

    # 清空
    def clear(self, *loc) :
        self.driver.find_element(*loc).clear()

    # 获取标题
    def get_title(self) :
        return self.driver.title

    # 后置退出浏览器
    # def teardown_class(self):
    #     self.driver.quit()

    # 封装登录后的方法
    def log_dl_file(self, url, user, pwd) :
        self.driver.get(url)
        self.driver.find_element('').send_keys(user)
        self.driver.find_element('').send_keys(pwd)
        self.clicks('')
