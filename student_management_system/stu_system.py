#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/9
@Author : shenBF
@Desc   : 学生管理系统

eval()函数用来执行一个字符串表达式，并返回表达式的值。可以将str转换为list、dict、tuple。
该项目中用于将str转换为dict。如果想要将list、dict、tuple转换为str，可以使用str()函数
"""

import os

filename = 'student.txt'


def insert():
    student_list = []
    while True:
        stu_id = input('请输入ID（如1001）：')
        if not stu_id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except ValueError:
            print('输入无效')
            continue
        student = {
            'id': stu_id,
            'name': name,
            'python': python,
            'java': java
        }
        student_list.append(student)
        # y or n
        if y_or_n('是否继续添加？'):
            continue
        else:
            break
    # 保存
    stu_save(student_list)
    print('学生信息录入完毕！')


def stu_save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except BaseException as e:
        print(e)
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    stu_query = []
    while True:
        stu_id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按id查找请输入1，按name查找请输入2：')
            if mode == '1':
                stu_id = input('请输入学生id：')
            elif mode == '2':
                name = input('请输入学生name：')
            else:
                print('输入有误')
                search()
            with open(filename, 'r', encoding='utf-8') as file:
                stu_list = file.readlines()
                for item in stu_list:
                    d = eval(item)
                    if stu_id:
                        if d['id'] == stu_id:
                            stu_query.append(d)
                    elif name:
                        if name in d['name']:
                            stu_query.append(d)
            show_stu(stu_query)
            stu_query.clear()
            if y_or_n('是否要继续查询？'):
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


def show_stu(lst):
    if len(lst) == 0:
        print('没有查询到学生信息')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', '姓名', 'Python', 'Java', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(
            item['id'],
            item['name'],
            item['python'],
            item['java'],
            int(item['python']) + int(item['java'])
        ))


# 先把文件中的学生信息都读出来，然后再把ID不匹配的内容写入，从而实现删除
def delete():
    while True:
        stu_id = input('请输入要删除的学生ID（如1001）：')
        if stu_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    stu_list = file.readlines()
            else:
                stu_list = []
            flag = False  # 标记是否删除
            if stu_list:
                with open(filename, 'w', encoding='utf-8') as file:
                    for item in stu_list:
                        d = eval(item)  # 将字符串转换为字典
                        if d['id'] != stu_id:
                            file.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{stu_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{stu_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后要重新显示所有学生信息
            if y_or_n('是否继续删除？'):
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_list = rfile.readlines()
    else:
        return
    stu_id = input('请输入要修改的学生ID（如1001）：')
    with open(filename, 'w', encoding='utf-8') as file:
        flag = False
        for item in stu_list:
            d = eval(item)  # 将字符串转换为字典
            if d['id'] == stu_id:
                flag = True
                print('找到学生信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['python'] = input('请输入Python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except ValueError:
                        print('输入有误')
                    else:
                        break
                file.write(str(d) + '\n')
                print('修改成功！')
            else:
                file.write(str(d) + '\n')
            # 重点：及时刷新缓冲区，否则会写入异常
            file.flush()
        if not flag:
            print('未找到学生信息')
        if y_or_n('是否继续修改？'):
            modify()
        else:
            return


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            stu_list = file.readlines()
        stu_new = []
        for item in stu_list:
            d = eval(item)
            stu_new.append(d)
    else:
        return
    asc_or_desc = input('请选择（0.升序，1.降序）：')
    if asc_or_desc == '0':
        flag = False
    elif asc_or_desc == '1':
        flag = True
    else:
        print('输入有误')
        sort()
        return
    mode = input('请选择排序方式（1.按Python成绩排序，2.按Java成绩排序，3.按照总成绩排序）')
    if mode == '1':
        stu_new.sort(key=lambda it: int(it['python']), reverse=flag)
    elif mode == '2':
        stu_new.sort(key=lambda it: int(it['java']), reverse=flag)
    elif mode == '3':
        stu_new.sort(key=lambda it: int(it['python']) + int(it['java']), reverse=flag)
    else:
        print('输入有误')
        sort()
        return
    show_stu(stu_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            stu_list = file.readlines()
            if stu_list:
                print(f'一共有{len(stu_list)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息...')


def show():
    stu_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            for item in students:
                stu_list.append(eval(item))
            if stu_list:
                show_stu(stu_list)
    else:
        print('暂未保存数据信息...')


def main():
    while True:
        menu()
        choice = get_choice()
        if choice in range(8):
            if choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
            else:
                if y_or_n('确定退出吗？'):
                    print('感谢使用')
                    break
                else:
                    continue
        else:
            print('不支持，请重新选择')
            continue


def get_choice():
    try:
        return int(input('请选择：'))
    except ValueError:
        return -1


def y_or_n(suffix):
    answer = input(suffix + 'y/n')
    if answer == 'y' or answer == 'Y':
        return True
    else:
        return False


def menu():
    print('=======学生管理系统=======')
    print('--------功能菜单--------')
    print('\t1. 录入学生信息')
    print('\t2. 查找学生信息')
    print('\t3. 删除学生信息')
    print('\t4. 修改学生信息')
    print('\t5. 排序学生信息')
    print('\t6. 统计学生总人数')
    print('\t7. 显示所有学生信息')
    print('\t0. 退出')
    print('------------------------')


if __name__ == '__main__':
    main()
