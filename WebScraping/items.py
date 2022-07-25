# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FullWebsite(scrapy.Item):
    blue_mercury = scrapy.Field()


class WebsiteCategories(scrapy.Item):
    skincare = scrapy.Field()
    hair = scrapy.Field()
    body = scrapy.Field()
    fragrances = scrapy.Field()
    tools_accessories = scrapy.Field()
    home = scrapy.Field()
    suncare = scrapy.Field()
    men = scrapy.Field()
    gifts = scrapy.Field()
    best_seller = scrapy.Field()


class WebscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    Product_ID = scrapy.Field()
    Product_Category = scrapy.Field()
    # Product_Sub_category = scrapy.Field()
    Product_Name = scrapy.Field()
    Product_URL = scrapy.Field()
    Product_Image = scrapy.Field()
    Product_Rating = scrapy.Field()
    Product_Price = scrapy.Field()
    Product_Description = scrapy.Field()
    Number_Of_Ratings = scrapy.Field()
    scrap = scrapy.Field()


class DataHandler(scrapy.Item):
    # Reviews = scrapy.Field()
    Review_Author = scrapy.Field()
    Review_Title = scrapy.Field()
    Author_ID = scrapy.Field()
    Author_Name = scrapy.Field()
    Review_Date = scrapy.Field()
    Rating = scrapy.Field()
    Review_Text = scrapy.Field()
