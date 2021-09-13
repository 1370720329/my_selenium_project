# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
"""
 INDEX:

 Name:LiLiangWei
"""
import datetime
import logging
import logging.handlers
import os
from pathlib import Path


"""
封装日志
"""

def logs() :
    # 创建一个日志器
    logger = logging.getLogger()

    # 解决了日志重复的问题=====这是个大坑
    logger.handlers.clear()
    # 设置日志等级
    logger.setLevel(logging.DEBUG)

    # 获取当前位置，拼接一个存放地址
    file = Path(__file__).resolve().parent.parent
    b = os.path.join(file, r"logs", 'debug.log')

    # 定义日志格式模板
    fm = '%(asctime)s %(filename)s %(levelname)s %(message)s %(levelno)s  %(lineno)d %(threadName)s'


    # 输出日志的文件路径或者地方，控制台、文件、邮件等
    fh = logging.FileHandler(b, 'a', encoding='utf-8')    # 把定义的模板放在创建的handler

    fh.setFormatter(logging.Formatter(fm))
    logger.addHandler(fh)

    #  创建handler添加到控制台
    ch = logging.StreamHandler()

    ch.setFormatter(logging.Formatter(fm))
    logger.addHandler(ch)

    # 避免日志重复
    # logger.removeHandler(ch)
    # logger.removeHandler(fh)

    # 指定要输出的方式
    # logger.propagate = False
    # logger.fatal(datetime.datetime.now().strftime('%Y-%m-%d')) #在新日志中写上当天的日期
    # logger.handlers.pop()
    return logger
# a = logs()
# a.debug('test')
