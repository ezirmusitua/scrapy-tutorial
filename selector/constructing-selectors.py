from scrapy.selector import Selector
from scrapy.http import HtmlResponse


# construct from text
body = '<html><body><span>good</span></body></html>'
print(Selector(text=body).xpath('//span/text()').extract())

# construct from response
response = HtmlResponse(url='http://doc.scrapy.org/en/latest/_static/selectors-sample1.html')
print(Selector(response=response).xpath('//title/text()').extract())
