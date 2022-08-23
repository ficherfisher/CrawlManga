[English](README.md) | 简体中文

<p align="center">
 <img src="./doc/img/index.png" align="middle" width = "600"/>
<p align="center">
------------------------------------------------------------------------------------------

<p align="left">
    <a href=""><img src="https://img.shields.io/badge/release-1.1.0-red"></a>
    <a href=""><img src="https://img.shields.io/badge/python-3.7+-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/os-linux%2C%20win-pink.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/scrapy-2.6.1-green.svg"></a>
</p>


## 简介

CrawlManga 包含多个漫画爬虫，以及将下载的漫画上传到远端服务器

**近期更新**

- 添加针对maofly漫画网站的爬虫maoflyManga (https://www.maofly.com/)
- 添加针对xingqiu漫画网站的爬虫xingqiuManga (http://m.mhxqiu1.com/)
- 添加将本地文件上传到服务器的代码(https://github.com/ficherfisher/CrawlManga/blob/master/uploadServer/uploadServer.md)
- [More](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/doc/doc_ch/update.md)

## 特性

- 全自动更新漫画网站
- 支持断点续爬网站
    - 包括断点重传文件
- 可运行于Linux、Windows等多种系统


## 效果展示

<div align="center">
    <img src="./doc/img/show1.png" width="400">
    <img src="./doc/img/show2.png" width="400">
</div>

上图是通用PP-OCR server模型效果展示，更多效果图请见[效果展示页面](http://fisherficher.xyz:3000/)。

## 快速体验
- fisher漫画网站

<div align="center">
<img src="./doc/img/index.png"  width = "800" height = "400" />
</div>

## 漫画列表（更新中）

|漫画|更新时间|最新话|是否更新|下次更新时间|网址|
|------------|---------------|----------------|----|----------|----------|
|传武漫画|2022-08-15|306 | ×|2022-09-01|[最新话306](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E4%BC%A0%E6%AD%A6)|
|从前有座灵剑山漫画|2022-08-21 17:43:08|806 | ×|2022-09-18|[最新话806](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E4%BB%8E%E5%89%8D%E6%9C%89%E5%BA%A7%E7%81%B5%E5%89%91%E5%B1%B1)|
|斗罗大陆漫画|2022-08-22 17:31:54|505 | ×|2022-09-19|[最新话505](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86)|
|斗破苍穹漫画|2022-08-21 17:42:56|532 | ×|2022-09-01|[最新话532](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9)|
|一人之下漫画|2022-08-12|618| ×|2022-09-01|[最新话618](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B)|
|ONE PIECE航海王|2022-08-06|1057 | ×|2022-09-01|[最新话1057](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E6%B5%B7%E8%B4%BC%E7%8E%8B)|
|国王排名|2022-08-09|104 | ×|2022-09-01|[最新话104](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E5%9B%BD%E7%8E%8B%E6%8E%92%E5%90%8D)|
|间谍过家家|2022-08-09|77 | ×|2022-09-01|[最新话77](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E9%97%B4%E8%B0%8D%E8%BF%87%E5%AE%B6%E5%AE%B6)|
|一拳超人|2022-08-21|234 | ×|2022-09-18|[最新话234](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E4%B8%80%E6%8B%B3%E8%B6%85%E4%BA%BA)|
|咒术回战|2022-08-21|195 | ×|2022-09-01|[最新话195](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E5%92%92%E6%9C%AF%E5%9B%9E%E6%88%98)|
|重生之都市修仙漫画|2022-08-21|815 | ×|2022-09-01|[最新话815 ](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E9%87%8D%E7%94%9F%E4%B9%8B%E9%83%BD%E5%B8%82%E4%BF%AE%E4%BB%99%E6%BC%AB%E7%94%BB)|
|三月的狮子|2021-11-15|185 | ×|2022-09-01|[最新话185](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E4%B8%89%E6%9C%88%E7%9A%84%E7%8B%AE%E5%AD%90)|
|镇魂街|2022-07-15|375 | ×|2022-09-01|[最新话375](http://fisherficher.xyz:3000/cartoon.html?cartoon=%E9%95%87%E9%AD%82%E8%A1%97)|




更多漫画可以联系作者(yupengxiong87@gmail.com)


## 文档教程
- [运行环境准备](./doc/environment.md)
- [快速开始](./doc/quickstart.md)
- 漫画网址爬虫
    - [xingqiuManga爬虫]()
        - [scrapy](./xingqiuManga/xingManga.md)
    - [maoflyManga爬虫]()
        - [scrapy](./maoflyManga/maoflyManga.md)
- 上传文件服务器
    - [uploadServer]()
        - [上传文件](./uploadServer/uploadServer.md)
        - [断点重传]()
- [联系作者](yupengxiong87@gmail.com)


## PP-OCRv2 Pipeline
<div align="center">
    <img src="./doc/ppocrv2_framework.jpg" width="800">
</div>

[1] PP-OCR是一个实用的超轻量OCR系统。主要由DB文本检测、检测框矫正和CRNN文本识别三部分组成。该系统从骨干网络选择和调整、预测头部的设计、数据增强、学习率变换策略、正则化参数选择、预训练模型使用以及模型自动裁剪量化8个方面，采用19个有效策略，对各个模块的模型进行效果调优和瘦身(如绿框所示)，最终得到整体大小为3.5M的超轻量中英文OCR和2.8M的英文数字OCR。更多细节请参考PP-OCR技术方案 https://arxiv.org/abs/2009.09941

[2] PP-OCRv2在PP-OCR的基础上，进一步在5个方面重点优化，检测模型采用CML协同互学习知识蒸馏策略和CopyPaste数据增广策略；识别模型采用LCNet轻量级骨干网络、UDML 改进知识蒸馏策略和Enhanced CTC loss损失函数改进（如上图红框所示），进一步在推理速度和预测效果上取得明显提升。更多细节请参考PP-OCRv2[技术报告](https://arxiv.org/abs/2109.03144)。






