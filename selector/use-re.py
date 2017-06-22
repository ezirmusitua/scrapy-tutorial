from scrapy.http import HtmlResponse

response = HtmlResponse(url='http://doc.scrapy.org/en/latest/_static/selectors-sample1.html')

print('use re: ', response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)'))
