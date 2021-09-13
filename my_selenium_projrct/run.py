# -*- coding:utf-8 -*-
import pytest
# import testcase
import os


if __name__ == '__main__' :
    pytest.main(['-sv', './testcase','--alluredir', 'rusult'])
    os.system('allure generate ./rusult/ -o ./reports --clean')










#


# 用os模块运行#方法一
# pytest run.py -s -q --alluredir=./reports 这是默认浏览器生成测试报告
# allure serve ./reports 这是获取在线报告
#方法二
# allure generate ./reports/ -o ./rusult --clean 从结果生成报告

# 发现问题，单个文件执行没问题。run执行会找不到日志的错误。原因定位：因为logging日志不支持多线程

