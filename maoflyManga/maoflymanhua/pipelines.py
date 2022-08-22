# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import json
import time
import urllib

import requests
import scrapy
from itemadapter import ItemAdapter
import os
from urllib import request

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import yaml


class MaoflymanhuaPipeline:
    def __init__(self):
        self.wheather_tag = ["√", "×"]
        self.path = os.path.join(os.path.dirname(__file__), "images")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        yaml_config = open(os.path.join(os.path.dirname(__file__), "config.yaml"), encoding="utf-8")
        self.page_dict = yaml.load(yaml_config.read(), Loader=yaml.FullLoader)
        yaml_config.close()

        update_inf = open(r"D:\programmeProject\pycharmProject\scrapy\1_test_selenium_request\update_inf.json",
                          encoding="utf-8")
        update_inf_ = json.load(update_inf)
        update_inf.close()
        for j in update_inf_:
            j['wheather'] = self.wheather_tag[1]
        update_inf = open(r"D:\programmeProject\pycharmProject\scrapy\1_test_selenium_request\update_inf.json",
                          'w', encoding="utf-8")
        json.dump(update_inf_, update_inf, indent=1, ensure_ascii=False)
        update_inf.close()

    def process_item(self, item, spider):
        update_inf = open(r"D:\programmeProject\pycharmProject\scrapy\1_test_selenium_request\update_inf.json",
                          encoding="utf-8")
        update_inf_ = json.load(update_inf)
        mange_lists = [i["manga"] for i in update_inf_]
        update_inf.close()

        title = item['title']
        title_path = os.path.join(self.path, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        if title not in self.page_dict:
            self.page_dict[title] = 0
        self.page_dict[title] = self.page_dict[title] + 1
        chapter_tmp = str(self.page_dict[title])
        chapter_path = os.path.join(title_path, chapter_tmp)

        if not os.path.exists(chapter_path):
            os.mkdir(chapter_path)
        image_urls = item['image_urls']
        for index, i in enumerate(image_urls):
            headers = {
                "Referer": "https://www.maofly.com/",
                "sec-ch-us": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/104.0.0.0 Safari/537.36"
            }
            html = requests.get(i, headers=headers)
            with open(chapter_path + '/' + str(index) + '.jpg', 'wb') as file:
                file.write(html.content)

        fp_yaml_config = open(os.path.join(os.path.dirname(__file__), "config.yaml"), "w", encoding="utf-8")
        yaml.safe_dump(self.page_dict, fp_yaml_config, encoding="utf-8", allow_unicode=True)
        fp_yaml_config.close()

        update_inf_1 = open(r"D:\programmeProject\pycharmProject\scrapy\1_test_selenium_request\update_inf.json",
                            "w", encoding="utf-8")
        if title not in mange_lists:
            tmp_dict = {
                'manga': title,
                "updatetime": str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                "latest": str(self.page_dict[title]),
                "wheather": "√",
                "nexttime": str(datetime.date.today() + datetime.timedelta(days=28))
            }
            update_inf_.append(tmp_dict)
        else:
            index_tmp = mange_lists.index(title)
            update_inf_[index_tmp]["updatetime"] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            update_inf_[index_tmp]["latest"] = str(self.page_dict[title])
            update_inf_[index_tmp]["nexttime"] = str(datetime.date.today() + datetime.timedelta(days=28))
            update_inf_[index_tmp]["wheather"] = "√"
        json.dump(update_inf_, update_inf_1, indent=1, ensure_ascii=False)
        update_inf_1.close()
        return item

