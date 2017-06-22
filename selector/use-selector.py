from scrapy.http import HtmlResponse

response = HtmlResponse(url='http://doc.scrapy.org/en/latest/_static/selectors-sample1.html')

# querying with xpath
print('with xpath: ', response.xpath('//title/text()'))
# querying with css selector
print('with css: ', response.css('title::text'))
# querying with css and xpath
print('with css & xpath: ', response.css('img').xpath('@src').extract())
# extract text only
print('extract text only|xpath: ', response.xpath('//title/text()').extract())
print('extract text only|css: ', response.css('title::text'))
# extract the first
print('extract the first: ', response.xpath('//title/text()').extract_first())
print('extract the first with default: ', response.xpath('//title/p/text()').extract_first(default='not-found'))

