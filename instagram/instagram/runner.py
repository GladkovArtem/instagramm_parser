from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from instagram.instagram.spiders.instagramcom import InstagramcomSpider
from instagram.instagram import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstagramcomSpider, users_list=['karelskaya_cakes','svetis'])
    process.start()