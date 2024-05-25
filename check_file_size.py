# -*- coding: utf-8 -*-
"""
@Version: python3.9
@Date   : 2024/5/25
@Author : shenBF
@Desc   : 判断URL文件的大小
"""

import requests


def get_file_size(_url):
    # 发送HEAD请求以获取文件大小
    response = requests.head(_url)
    # 获取Content-Length头部来确定文件大小（单位：字节）
    file_size = response.headers.get('Content-Length')
    return int(file_size) if file_size else None


if __name__ == '__main__':
    # 示例URL
    url = 'https://lw-sycdn.kuwo.cn/2e5e89abdf5eb4510fca449911a27bc4/6651e2a2/resource/30106/trackmedia/M500001qpzVa16eFhO.mp3?from=vip'
    # 获取文件大小
    size = get_file_size(url)
    if size:
        print(f'The file size is: {size} bytes')
    else:
        print('Unable to retrieve file size')
