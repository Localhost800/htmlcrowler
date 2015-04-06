import scrapy
#Creating class for spider
class yoursitespider(scrapy.Spider):
    name = "sites"
    allowed_domains = ["yoursite.com"]
    start_urls = [
        "http://yoursite.com/"
    ]
    #you can change your addrs from sources :D 
    #Function for saving response

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)


            #scrapy crawl sites
