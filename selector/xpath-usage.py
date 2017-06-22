from scrapy.selector import Selector

EXAMPLE = '''
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1> This is an example </h1>
    <h2> This is an example </h2>
    <h3> This is an example </h3>
    <p>Hello World</p>
    <div id="1">
      <p>
        <a href="https://github.com/ezirmusitua">ezirmusitua</a>
        <img src="https://avatars3.githubusercontent.com/u/13930113" />
      </p>
    </div>
    <div id="2">
      <p>
        <a href="https://github.com/ezirmusitua">ezirmusitua</a>
        <img src="https://avatars3.githubusercontent.com/u/13930113" />
      </p>
    </div>
    <div id="3">
      <p>
        <a href="https://github.com/ezirmusitua">ezirmusitua</a>
        <img src="https://avatars3.githubusercontent.com/u/13930113" />
      </p>
    </div>
  </body>
'''
SELECTOR = Selector(text=EXAMPLE)
# use relative path with .
divs = SELECTOR.xpath('//div')
for p in divs.xpath('.//p'):
    print(p.extract())
for p in divs.xpath('p'):
    print(p.extract())

# use variable
print('use variable: ', SELECTOR.xpath('//div[@id=$val]/a/text()', val='1').extract_first())

# use re
RE_EXAMPLE_DOC = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
re_sel = Selector(text=RE_EXAMPLE_DOC, type="html")
print('use re in xpath: ', re_sel.xpath('//li//@href').extract())
print('use re in xpath: ', re_sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract())

# set operation
OPERATION_EXAMPLE_DOC = '''
<div itemscope itemtype="http://schema.org/Product">
  <span itemprop="name">Kenmore White 17" Microwave</span>
  <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
  <div itemprop="aggregateRating"
    itemscope itemtype="http://schema.org/AggregateRating">
   Rated <span itemprop="ratingValue">3.5</span>/5
   based on <span itemprop="reviewCount">11</span> customer reviews
  </div>

  <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
    <span itemprop="price">$55.00</span>
    <link itemprop="availability" href="http://schema.org/InStock" />In stock
  </div>

  Product description:
  <span itemprop="description">0.7 cubic feet countertop microwave.
  Has six preset cooking categories and convenience features like
  Add-A-Minute and Child Lock.</span>

  Customer reviews:

  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Not a happy camper</span> -
    by <span itemprop="author">Ellie</span>,
    <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1">
      <span itemprop="ratingValue">1</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">The lamp burned out and now I have to replace
    it. </span>
  </div>

  <div itemprop="review" itemscope itemtype="http://schema.org/Review">
    <span itemprop="name">Value purchase</span> -
    by <span itemprop="author">Lucas</span>,
    <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
    <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
      <meta itemprop="worstRating" content = "1"/>
      <span itemprop="ratingValue">4</span>/
      <span itemprop="bestRating">5</span>stars
    </div>
    <span itemprop="description">Great microwave for the price. It is small and
    fits in my apartment.</span>
  </div>
</div>
'''
operation_sel = Selector(text=OPERATION_EXAMPLE_DOC, type="html")
print('Set Operations::')
for scope in operation_sel.xpath('//div[@itemscope]'):
    print('current scope: ', scope.xpath('@itemtype').extract())
    props = scope.xpath('set:difference(./descendant::*/@itemprop, .//*[@itemscope]/*/@itemprop)')
    print('properties: ', props.extract())

