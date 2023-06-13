# -*-coding:utf8-*-
#!/usr/bin/python3

# 依赖：python -m pip install retrying -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

import os
import urllib.request
import time
from retrying import retry
import random
import re

# 全局变量定义
txt_path = '图片.txt'    # 要下载的文件
save_path = 'C:/Users/gwj11/Desktop/img/'  # 保存的目录

#定义爬虫方法
current_file_number = 1
@retry(stop_max_attempt_number=7,stop_max_delay=10000,wait_fixed=30000)
def save_img(url,name):
    global current_file_number
    file_path = save_path+str(name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_suffix= os.path.splitext(url)[1]
    file_name = str(current_file_number)
    current_file_number += 1
    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, ".jfif")
    urllib.request.urlretrieve(url,filename=filename)

#获取图片链接
def get_url(file_path):
    url_pool = []

    regex = r'https?://[^\s]+'
    current_date = None
    current_text = None
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cnt = 0
        for line in lines:
            if line.startswith('发布日期:'):
                # 提取发布日期
                date = line.split(':')[1].strip().split(' ')[0]
                current_date = date
                current_text = None
            elif line.startswith('正文:'):
                # 提取正文
                text = line.split(':', 1)[1].strip()
                current_text = text
                
                # 创建日期文件夹
                folder_path = os.path.join(save_path+current_date)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # 保存正文到文件
                text_file_path = os.path.join(folder_path, '正文.txt')
                with open(text_file_path, 'a', encoding='utf-8') as text_file:
                    text_file.write("正文"+str(cnt)+": "+text+"\n\n")
                cnt = cnt+1
                    
            elif line.startswith('图片链接:'):
                if current_date and current_text:
                    # 提取链接
                    urls = re.findall(regex, line)
                    
                    # 添加到url_pool列表中
                    for url in urls:
                        url_pool.append([url, current_date])
    return url_pool

#爬取图片到本地
url_pool = get_url(txt_path);
print(url_pool)

for url,name in url_pool:
    save_img(url,name)
    time.sleep(0.1)
    print('%s下载成功' % name)

