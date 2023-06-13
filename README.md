## bcy-spider

> 半次元个人图片信息，一键下载存档， [小白直达](https://github.com/gwj12345/bcy-spider#3无脑操作版) ，2023.06.13  

#### 1、项目背景

**2023-06-13 [半次元](https://bcy.net/)宣布下架**

+ 停服公告：[地址](https://bcy.net/item/detail/7243752692219124791)
![image-20230613230710293](README.assets/image-20230613230710293.png)


+ **官方给了个人数据下载**：

  ![image-20230613231321519](README.assets/image-20230613231321519.png)![image-20230613231359701](README.assets/image-20230613231359701.png)

+ 然而我获得的数据是这样的？？？

  还被告知6个月后图片过期无法下载。

  ![image-20230613231444513](README.assets/image-20230613231444513.png)

+ 作为7年老用户，就算是个小透明没发过多少东西。
  
  几十上百张的图（包括仅自己可见的）还是有的，总不能让我一张一张的下。。。
![image-20230613231234803](README.assets/image-20230613231234803.png)



#### 2、关于本项目

> 临时1-2小时造出来的，仅供自己存档留念，数据搞下来了就行，估计也不太会翻看，所以也没写的很仔细。
>
> 如果有小伙伴需要的话，可以自己加一些功能，欢迎提交pull request（最近期末可能消息看的不一定很及时）。

项目简介

+ 支持爬虫一键下载个人的图片信息，并按日期分类整理到文件夹
+ 当天文件夹：图片按全局顺序编号存入，然后有一个正文.txt，正文xxx的形式，存放当天所有动态的正文。

![image-20230613230642812](README.assets/image-20230613230642812.png)

![image-20230613230808827](README.assets/image-20230613230808827.png)

![image-20230613232158515](README.assets/image-20230613232158515.png)



**本地环境**

原生：[python](https://www.python.org/downloads/) >= 3.8

依赖：`python -m pip install retrying -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`



#### 3、无脑操作版

> 打包方案： `Pyinstaller -p C:\Users\gwj11\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\site-packages  -F  download_img.py `

1. 将`图片.txt`和`download_img.exe`放在同一个文件夹下
2. windows下运行`download_img.exe`， 即可自动运行程序。
3. 下载到的图片保存在C:\img中。

![image-20230614003157221](README.assets/image-20230614003157221.png)

