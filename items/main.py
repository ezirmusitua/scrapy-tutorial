import scrapy

'''
Scrapy Items
dictionary like API
trackref to help finding memory leaks
'''


# declare Items
class Product(scrapy.Item):
    # Field use to set meta data
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)


product = Product(name='Desktop PC', price=1000)
print('init Product: ', product)

print('get field by []: ', product['name'])
print('get field by get: ', product.get('name'))
print('name `in` product: ', 'name' in product)

product['stock'] = 20
print('you can only set field value that the item actually have: ', product['stock'])

product2 = Product(product)
print('Product(product) to copy: ', product2)
product3 = product2.copy()
print('product.copy to copy: ', product3)
product_dict = dict(product)
print('create dict: dict(product)', product_dict)
product_from_dict = Product({ 'name': 'Laptop PC', 'price': 1500 })
print('create product from dict: ', product_from_dict)


class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()
