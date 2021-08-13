import scrapy
from bs4 import BeautifulSoup

class FoodDataSpider(scrapy.Spider):
	name = "food_data_spirder"
	start_urls = ['https://www.igenewiki.com/%E9%A3%9F%E7%89%A9%E5%98%8C%E5%91%A4%E5%90%AB%E9%87%8F']
	

	def parse(self, response, **kwargs):
		soup = BeautifulSoup(response.text)
		table = soup.find('table',{'id':'tablepress-5'})
		for row in table.find_all('tr')[1:]:
			datas = row.find_all('td')
			name,value,alias = [e.get_text() for e in datas]
			yield {'name':name,'value':value,'alias':alias}
