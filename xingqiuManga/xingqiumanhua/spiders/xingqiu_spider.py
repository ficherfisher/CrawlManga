import scrapy
from xingqiumanhua.items import XingqiumanhuaItem
import re
from xingqiumanhua.get_start_next_url import get_start


class XingqiuSpiderSpider(scrapy.Spider):
    name = 'xingqiu_spider'
    allowed_domains = ['m.mhxqiu1.com']
    get_start_ = get_start()
    tmp_start = get_start_.get_start_url()
    init = []  # 新的漫画url
    start_urls = tmp_start + init

    def parse(self, response, **kwargs):

        chapter = response.xpath("//*[@class='swiper-chapter']/p/text()").extract()
        chapter = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str(chapter))
        title_tmp = response.xpath("/html/head/title/text()").extract()
        title = str(title_tmp).split("_")[1]
        title = title.split("-")[0]
        title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", title)
        image_urls = response.xpath("//*[@class='chapter-img-box']/img/@data-original").getall()
        items = XingqiumanhuaItem(title=title, chapter=chapter, image_urls=image_urls)
        yield items
        next_url = response.url
        yield scrapy.Request(url=next_url, dont_filter=True)

