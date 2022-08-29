# 漫画网站爬虫快速开始


- [快速开始](#paddleocr)

  + [1. 安装scrapy包以及相关配置包](#1)
  * [2. 便捷使用](#2)
    + [2.1 命令行使用](#21)
      - [2.1.1 maoflyManga](#211)
      - [2.1.2 xingqiuManga](#212)

<a name="1"></a>

## 1. 安装scrapy包

```bash
pip install "scrapy>=2.5.1" # 推荐使用2.5.1+版本
```

- 对于Windows环境用户：

  直接通过pip安装的scrapy库可能出现`[winRrror 126] 找不到指定模块的问题`。原因是安装twist模块出现问题，建议从[这里]()下载twist安装包完成安装(注意版本匹配)

- 安装其他库

  ```bash
  pip install -r requirement.txt
  """
  itemadapter==0.3.0
  PyYAML==6.0
  requests==2.27.1
  Scrapy==2.6.1
  selenium==4.4.3
  """
  ```
- 安装chrome浏览器和driverchrome驱动
  安装教程可以参考[这里](https://blog.csdn.net/zhoukeguai/article/details/113247342) 或者 [more](https://zhuanlan.zhihu.com/p/373688337)


<a name="2"></a>
## 2. 便捷使用
<a name="21"></a>
### 2.1 命令行使用

CrawlManaga提供了一系列测试网站及其测试的url，点击[这里](/xingqiuManga/xingqiumanhua/config_url.yaml)查看信息

<a name="211"></a>
#### 2.1.1 maoflyManaga使用
```
cd maoflyManga
conda activate env
python start_maofly_spider.py
```

如果不使用提供的测试url，可以修改config_url.yaml文件，添加对应的漫画名及其开始的url
例如：

```
ONE PIECE航海王: https://www.maofly.com/manga/5668/612445.html
一拳超人: https://www.maofly.com/manga/7054/612375.html
咒术回战: https://www.maofly.com/manga/32670/612664.html
国王排名: https://www.maofly.com/manga/41341/610373.html
间谍过家家: https://www.maofly.com/manga/10127/610509.html
漫画名：url
```

<a name="212"></a>
#### 2.1.2 xingqiuManaga使用
```
cd xingqiuManga
conda activate env
python start_xingqiu_spider.py
```
如果不使用提供的测试url，可以修改config_url.yaml文件，添加对应的漫画名及其开始的url(同上)


# 上传文件快速开始


- [快速开始](#paddleocr)
  + [1. 相关配置包](#1)
  * [2. 便捷使用](#2)
    + [2.1 命令行使用](#21)
      - [2.1.1 上传至服务器](#211)


<a name="1"></a>

## 1. 相关配置

- 安装相关库

  ```bash
  pip install -r requirement.txt
  """
  paramiko==2.8.1
  PyYAML==6.0
  requests==2.27.1
  selenium==4.4.3
  tqdm==4.64.0
  """
  ```
- 安装chrome浏览器和driverchrome驱动
  安装教程可以参考[这里](https://blog.csdn.net/zhoukeguai/article/details/113247342) 或者 [more](https://zhuanlan.zhihu.com/p/373688337)


<a name="2"></a>
## 2. 便捷使用
<a name="21"></a>
### 2.1 命令行使用

uploadServer提供了一系列测试文件夹，点击[这里](/xingqiuManga/xingqiumanhua/config_url.yaml)查看信息

<a name="211"></a>
#### 2.1.1 maoflyManaga使用
```
cd uploadServer
conda activate env
python upload_server.py
```

如果不使用提供的测试文件夹，可以修改config_url.yaml文件，添加对应的漫画名及其开始的url
例如：

```
ONE PIECE航海王: https://www.maofly.com/manga/5668/612445.html
一拳超人: https://www.maofly.com/manga/7054/612375.html
咒术回战: https://www.maofly.com/manga/32670/612664.html
国王排名: https://www.maofly.com/manga/41341/610373.html
间谍过家家: https://www.maofly.com/manga/10127/610509.html
漫画名：url
```





