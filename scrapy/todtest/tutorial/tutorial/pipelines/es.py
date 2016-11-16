import json
import treq

from twisted.internet import defer
from scrapy.exceptions import NotConfigured


class ESWriter(object):

	@classmethod
	def from_crawler(cls,crawler):
		print(' ======$$$$  ENTER pipeline==== ' )
        
		es_url=crawler.settings.get('ES_PIPELINE_URL',None)
		if not es_url:
			raise NotConfigured

		return cls(es_url)

	def __init__(self,es_url):
		self.es_url=es_url

	@defer.inlineCallbacks
	def process_item(self,item,spider):
		try:
			data=json.dumps(dict(item),ensure_ascii=true).encode("utf-8")
			self.log(' ======2222  data is {}==== '.format(data) )
			yield treq.post(self.es_url,data)
		finally:
			defer.returnValue(item)