# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import re

import yaml
from scrapy import signals
from selenium import webdriver
import urllib.request

from scrapy.http import HtmlResponse

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver.common.by import By


class XingqiumanhuaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class XingqiumanhuaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumDownloadMiddleware(XingqiumanhuaDownloaderMiddleware):

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # 设置无界面
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        self.options.add_argument('lang=zh_CN.UTF-8')
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')
        yaml_config = open(os.path.join(os.path.dirname(__file__), "config_url.yaml"), encoding="utf-8")
        self.page_dict = yaml.load(yaml_config.read(), Loader=yaml.FullLoader)
        yaml_config.close()

    def process_request(self, request, spider):
        driver = webdriver.Chrome(options=self.options)
        driver.get(request.url)
        html = driver.page_source
        try:
            next_page = driver.find_element(By.XPATH, "//*[@class='swiper-chapter']/a[2]")
            next_url = next_page.get_property("href")
            if not next_url.endswith(".html"):
                title_tmp = driver.title
                title = str(title_tmp).split("_")[1]
                title = title.split("-")[0]
                title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", title)
                self.page_dict[title] = driver.current_url
                fp_yaml_config = open(os.path.join(os.path.dirname(__file__), "config_url.yaml"), "w", encoding="utf-8")
                yaml.safe_dump(self.page_dict, fp_yaml_config, encoding="utf-8", allow_unicode=True)
                fp_yaml_config.close()
                next_url = ""
        except Exception as e:
            print(e)
            next_url = ""

        return HtmlResponse(url=next_url, body=html.encode('utf-8'), encoding='utf-8', request=request)

