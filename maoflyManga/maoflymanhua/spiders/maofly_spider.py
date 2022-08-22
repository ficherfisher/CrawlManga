import scrapy
from maoflymanhua.items import MaoflymanhuaItem
from maoflymanhua.get_start_next_url import get_start


class MaoflySpiderSpider(scrapy.Spider):
    name = 'maofly_spider'
    allowed_domains = ['www.maofly.com']
    get_start_ = get_start()
    tmp_start = get_start_.get_start_url()
    init = []    # 新的漫画url
    start_urls = tmp_start + init

    def parse(self, response, **kwargs):
        a = response.url
        pictures = response.xpath("//*[@class='img-content']//img/@src").getall()
        title = response.xpath("//h1/a/text()").extract()
        chapter = response.xpath("//h2/text()").extract()
        items = MaoflymanhuaItem(title=title[0], chapter=chapter[0], image_urls=pictures)
        yield items
        yield scrapy.Request(url=a, dont_filter=True)
