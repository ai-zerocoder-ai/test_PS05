import scrapy
import csv
class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        divans = response.css("div._Ud0k")

        with open('divan.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['название', 'цена', 'ссылка'])

            for divan in divans:
                name = divan.css("div.lsooF span::text").get()
                price = divan.css("div.pY3d2 span::text").get()
                relative_url = divan.css("a::attr(href)").get()
                url = response.urljoin(relative_url)

                writer.writerow([name, price, url])
