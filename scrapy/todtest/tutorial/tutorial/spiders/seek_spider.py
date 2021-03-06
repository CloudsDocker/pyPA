import scrapy
import datetime
from tutorial.items import JobItem 
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose,Join
from w3lib.html import remove_tags
import time

class SeekJavaSpider(scrapy.Spider):
    name = "seekJava"

    start_urls=[
       # 'https://www.seek.com.au/jobs-in-information-communication-technology?salary=150000-&HighPay=True',
        # 'https://www.seek.com.au/jobs-in-information-communication-technology?highpay=True&salaryrange=150000-999999&salarytype=annual'
        # 'http://quotes.toscrape.com'
        'https://www.seek.com.au/jobs-in-information-communication-technology/in-All-Sydney-NSW?page=7&salaryrange=120000-999999&salarytype=annual',
        # 'https://ms.taleo.net/careersection/2/moresearch.ftl'
        # 'scrapy shell -s USER_AGENT="Mozilla/5.0" 'https://www.gumtree.com/computing-it-jobs''
    ]
    

    def parse(self, response):
        # title = response.css('title::text').extract()
        # author= response.css('small.author::text').extract_first()
        # self.log(' ------ author is : %s ' % author)
        pagesToViewDetails=[]
        self.log(' =========   ENTER method parses ' )
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Title is %s' % title)
        # going to parse each jobs
        for idx,item in enumerate(response.css("a._1OFaluu::attr(href)")):
            nextPage=item.extract()
            self.log('------ {}:{}'.format(idx,nextPage))
            print nextPage
            # yield {
            #     'url':nextPage,
            # }

            if nextPage is not None:
                nextPage=response.urljoin(nextPage)
                self.log('~~~~~ new link is : '+nextPage)
                # time.sleep(1)
                pagesToViewDetails.append(nextPage)
                # yield scrapy.Request(nextPage,callback=self.parse)


        self.log('----- the first pagesToViewDetails:'+pagesToViewDetails[0])
        yield scrapy.Request(pagesToViewDetails[0],callback=self.parseDetails)
        # self.log('------ : '+ response.css("a._1OFaluu::attr(href)").extract_first())
            # self.log('------ : '+ item)

    def parseDetails(self, response):
        self.log('------------ ender parseDetails------------')
        # jobTitle=response.css('h1.jobtitle::text').extract_first().strip()
        # self.log('---- details: job title is : '+jobTitle)
        

        # yield jobtitle
        # jobDesc=response.css('div.templatetext').extract_first()
        # self.log('---- details: job description is : '+jobDesc)
        # for theTitle in jobTitle:   
        #     self.log('---- details: job title is : '+theTitle)

        # job=JobItem()
        # job['title']=jobTitle
        # job['description']=jobDesc

        il=ItemLoader(item=JobItem(),response=response)
        il.add_xpath('title','//h1[@class="jobtitle"]/text()',MapCompose(lambda i:remove_tags(i)))
        il.add_css('description','div.templatetext')
        il.add_value('url',response.url)
        il.add_value('indexTime',datetime.datetime.now())

        return il.load_item()
