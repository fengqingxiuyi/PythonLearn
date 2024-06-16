# -*- coding: utf-8 -*-
"""
@Version: python3.9
@Date   : 2024/5/7
@Author : shenBF
@Desc   : 爬虫 https://www.gequbao.com/music/1
"""

from bs4 import BeautifulSoup  # 网页解析，获取数据
import requests  # 请求
import urllib3
from requests.exceptions import RequestException
import json  # json解析
import os  # 执行操作系统命令

import time  # 模拟延迟

# import re  # 正则表达式

# 全局配置
MUSIC_ID_START = 1  # 第一个下载的音乐ID
MUSIC_ID_END = 300  # 最后一个需要下载的音乐ID
baseHtmlUrl = "https://www.gequbao.com/music/"  # 要爬取的网页链接
baseJsUrl = "https://www.gequbao.com/api/play_url?json=1&id="  # 要爬取的音乐地址链接
save_path = "/Users/fqxyi/Downloads/music_py/"  # 下载的音乐保存的文件夹
music_suffix = ".mp3"  # 下载的音乐的后缀名
MUSIC_DOWNLOAD_RETRY = 3  # 重试次数的全局常量，同时也是为了防止递归死循环
music_download_retry = MUSIC_DOWNLOAD_RETRY  # 重试次数的全局变量
filter_music_by_name = ["翻自", "Cover", "抖音", "伴奏", "Live", "剧情"]  # 过滤名字中符合条件的music
filter_music_size_min = 2 * 1024 * 1024  # 文件大小小于2MB的文件需要被过滤
filter_music_size_max = 10 * 1024 * 1024  # 文件大小大于10MB的文件需要被过滤
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 全局变量需要在方法内增加值
def remove_to_global_retry():
    global music_download_retry  # 声明是全局变量
    music_download_retry -= 1


# 重置全局变量
def reset_global_retry():
    global music_download_retry  # 声明是全局变量
    music_download_retry = MUSIC_DOWNLOAD_RETRY


# 获取文件大小
def get_file_size(_url):
    # 发送HEAD请求以获取文件大小
    response = requests.head(_url)
    # 获取Content-Length头部来确定文件大小（单位：字节）
    file_size = response.headers.get('Content-Length')
    return int(file_size) if file_size else 0


# 过滤文件内容太大或太小的文件
def filterFileSize(file_size):
    if file_size < filter_music_size_min:
        return True
    if file_size > filter_music_size_max:
        return True
    return False


# 过滤不想下载的音乐
def filterIllegalName(name):
    for condition in filter_music_by_name:
        if name.__contains__(condition):
            return True
    return False


# 获取音乐ID名称
def id_name(music_id):
    return "id_" + str(music_id)


# 得到指定一个URL的网页内容
def fetch_url(url):
    print("fetch url:", url)
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    try:
        response = requests.get(url, headers=head)
        if response.status_code == 200:
            response.encoding = "utf-8"
            content = response.text
            # print("fetch content:", content)
            return content
        else:
            print("fetch failed:", response.status_code, response.reason)
            return ""
    except RequestException as e:
        print("fetch failed:", e)
    return ""


# 爬取JS : 返回音乐下载地址 , 下面是示例地址和响应内容
# https://www.gequbao.com/api/play_url?id=9908271&json=1
# {
#     "code": 1,
#     "data": {
#         "url": "https://nc-sycdn.kuwo.cn/f0d5c95514e23cb1e2b10bd4bce0d28b/663cd315/resource/n2/30/14/1136317872.mp3?from=vip"
#     },
#     "msg": "操作成功"
# }
def fetch_music_url(index):
    complete_url = baseJsUrl + str(index)
    json_data = fetch_url(complete_url)  # 保存获取到的网页源码
    if json_data == "":
        return ""
    try:
        json_map = json.loads(json_data)
        url = json_map['data']['url']
        return "" if url is None else url
    except json.JSONDecodeError as e:
        print("fetch music url failed:", e)
        return ""


# 爬取HTML : 返回音乐的名称
def fetch_music_name(index):
    complete_url = baseHtmlUrl + str(index)
    html_data = fetch_url(complete_url)  # 保存获取到的网页源码
    if html_data == "":
        return ""
    # 逐一解析数据
    soup = BeautifulSoup(html_data, "html.parser")
    for item in soup.find_all('span', class_="form-control bg-light overflow-hidden"):  # 查找符合要求的字符串
        item = str(item)
        # print("item is ", item)
        if item.__contains__(music_suffix):
            name = item \
                .replace("<span class=\"form-control bg-light overflow-hidden\">", "") \
                .replace("</span>", "") \
                .strip()  # 去除空白符号
            return "" if name is None else name


# 返回可以当做文件名的音乐名称
def get_correct_music_name(_id, name):
    if name == "":
        name = id_name(_id) + music_suffix
    if name.__contains__("/"):
        name = name.replace("/", ",")
    return name


# 下载音乐
def download(_id, name, url):
    print("download " + id_name(_id) + " start:", name, url)

    # plan1
    # escaped_name = re.escape(name)
    # os.system("curl -o " + save_path + escaped_name + " " + url)

    # plan2
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 提取到全局配置中
    # 文件夹不存在，则创建文件夹
    folder = os.path.exists(save_path)
    if not folder:
        os.makedirs(save_path)
    # 获取文件地址
    file_path = os.path.join(save_path, name)
    if os.path.exists(file_path):
        print(name, "is exist!")
        time.sleep(5)  # 单位s，解决too many requests
        return
    # 读取MP3资源
    res = requests.get(url, stream=True, verify=False)
    # print('start write file:', file_path)
    # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
    with open(file_path, 'wb') as fd:
        for chunk in res.iter_content():
            fd.write(chunk)
    print("download " + id_name(_id) + " succeed:", file_path)


# 得到下载资源后下载
def prepare_download(music_ids):
    if music_download_retry == 0:
        reset_global_retry()
        return  # 跳出递归

    failed_music_ids = []  # 下载失败的音乐集合
    illegal_music_urls = {}  # 不合法的音乐集合，仅输出日志
    filter_music_names = {}  # 根据名字过滤掉的音乐集合
    filter_music_sizes = {}  # 根据大小过滤掉的音乐集合

    for _id in music_ids:
        url = fetch_music_url(_id)
        if not url.startswith("http") or url == "":
            illegal_music_urls.__setitem__(str(_id), url)
            continue
        file_size = get_file_size(url)
        if filterFileSize(file_size):
            filter_music_sizes.__setitem__(str(_id), str(file_size / 1024 / 1024) + "MB")
            continue
        remote_music_name = fetch_music_name(_id)
        if filterIllegalName(remote_music_name):
            filter_music_names.__setitem__(str(_id), remote_music_name)
            continue
        correct_music_name = get_correct_music_name(_id, remote_music_name)
        try:
            download(_id, correct_music_name, url)
        except OSError or RequestException as e:
            print("download " + id_name(_id) + " failed:", e)
            failed_music_ids.append(_id)

    print("download failed music ids:", failed_music_ids)
    print("download illegal music urls:", illegal_music_urls)
    print("download filter music names:", filter_music_names)
    print("download filter music sizes:", filter_music_sizes)

    remove_to_global_retry()
    if len(failed_music_ids) != 0:
        prepare_download(failed_music_ids)


def main():
    music_ids = []
    for index in range(MUSIC_ID_START, MUSIC_ID_END + 1):
        music_ids.append(index)
    # print("music_ids:", music_ids)
    prepare_download(music_ids)


# 当程序执行时调用
if __name__ == "__main__":
    main()
    print("爬取完毕！")
