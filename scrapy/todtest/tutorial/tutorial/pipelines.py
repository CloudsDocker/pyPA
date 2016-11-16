# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


@defer .inlineCallbacks
class JobESPipeline(object):
    def process_item(self, item, spider):
    	data=json.dumps(dict(item),ensure_ascii=true).encode("utf-8")
        yield treq.post(self.es_url,data)
