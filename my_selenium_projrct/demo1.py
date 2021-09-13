# -*- coding:utf-8 -*-
# 这是主页
def info() :
    str1 = '-------------欢迎进入校园管理系统-------------------'
    print(str1)


# 定义一个列表
list1 = []
dict1 = {}
# 添加的功能
def add_info() :
    add_name = input('请输入姓名：')
    add_age = input('请输入年龄：')
    add_sex = input('请输入性别：')
    # cit = print('name:', add_name, 'age:', add_age,'sex:' , add_sex)
    list1.append({add_name, add_age, add_sex})
add_info()
print(list1)


# while True :
#     info()
#     input_info = int(input('请输入序号：'))
#     if input_info == 1 :
#         # 添加的功能
#         add_info()
#     elif input_info == 2:
#         # 删除的功能
#
#         break
# print(list1)