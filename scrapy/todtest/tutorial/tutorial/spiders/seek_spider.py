import scrapy


class SeekJavaSpider(scrapy.Spider):
    name = "seekJava"

    start_urls=[
       # 'https://www.seek.com.au/jobs-in-information-communication-technology?salary=150000-&HighPay=True',
        # 'https://www.seek.com.au/jobs-in-information-communication-technology?highpay=True&salaryrange=150000-999999&salarytype=annual'
        'http://quotes.toscrape.com'
    ]


    def parse(self, response):
        title = response.css('title::text').extract()
        author= response.css('small.author::text').extract_first()
        self.log(' ------ author is : %s ' % author)
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        self.log('Title is %s' % title)