# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

import yaml
from scrapy import signals
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
import scrapy
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MaoflymanhuaSpiderMiddleware:
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


class MaoflymanhuaDownloaderMiddleware:
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


class SeleniumDownloadMiddleware(MaoflymanhuaDownloaderMiddleware):

    def __init__(self):
        yaml_config = open(os.path.join(os.path.dirname(__file__), "config_url.yaml"), encoding="utf-8")
        self.page_dict = yaml.load(yaml_config.read(), Loader=yaml.FullLoader)
        yaml_config.close()

    def process_request(self, request, spider):
        driver = webdriver.Chrome()
        driver.get(request.url)
        driver.add_cookie({"name": "is_pull", "value": "true"})
        js = "return action=document.body.scrollHeight"
        height = driver.execute_script(js)
        # 将滚动条调整至页面底部
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        # 定义初始时间戳（秒）
        t1 = int(time.time())
        # 定义循环标识，用于终止while循环
        status = True
        # 重试次数
        num = 0
        while status:
            # 获取当前时间戳（秒）
            t2 = int(time.time())
            # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
            if t2 - t1 < 10:
                new_height = driver.execute_script(js)
                if new_height > height:
                    time.sleep(1)
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    # 重置初始页面高度
                    height = new_height
                    # 重置初始时间戳，重新计时
                    t1 = int(time.time())
            elif num < 1:  # 当超过30秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待30秒
                time.sleep(1)
                num = num + 1
            else:  # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
                print("滚动条已经处于页面最下方！")
                status = False
                # 滚动条调整至页面顶部
                driver.execute_script('window.scrollTo(0, 0)')
                break
        # 打印页面源码
        html = driver.page_source
        next_item = driver.find_element(By.XPATH, "//div[@class='form-inline']//a[5]")
        h1 = driver.find_element(By.XPATH, "//h1").text
        try:
            ActionChains(driver).click(next_item).perform()
            time.sleep(3)
            next_url = driver.current_url
        except Exception as e:
            print(e)
            self.page_dict[h1] = request.url
            fp_yaml_config = open(os.path.join(os.path.dirname(__file__), "config_url.yaml"), "w", encoding="utf-8")
            yaml.safe_dump(self.page_dict, fp_yaml_config, encoding="utf-8", allow_unicode=True)
            fp_yaml_config.close()
            next_url = ""

        driver.close()
        return HtmlResponse(url=next_url, body=html.encode('utf-8'), encoding='utf-8', request=request)


