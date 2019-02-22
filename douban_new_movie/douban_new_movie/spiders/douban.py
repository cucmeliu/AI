# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ["www.moive.douban.com"]
    start_urls = ['http://movie.douban.com']

    def parse(self, response):
        sel = Selector(response)

        movie_name = sel.xpath("//div[@class='pl2']/a/text()").extract()
        movie_url = sel.xpath("//div[@class='pl2']/a/@href").extract()
        movie_star = sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()

        item = DoubanNewMovieItem()

        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['movie_star'] = [n for n in movie_star]
        item['movie_url'] = [n for n in movie_url]

        yield item
        
        print(movie_name, movie_star, movie_url)



