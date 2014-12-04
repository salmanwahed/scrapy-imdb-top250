from bs4 import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from imdbtops.items import Movie

class ImdbtopSpider(CrawlSpider):
    name = 'imdbtops'
    # allowed_domains = ['imbd.com']
    start_urls = ['http://www.imdb.com/chart/top', ]

    linkExtractor = LxmlLinkExtractor(allow=(r'/title/tt\d+/[\w?=]+'), tags=('a', 'title'), attrs=('href',), unique=True)

    rules = [Rule(linkExtractor, callback="parse_items", follow=False)]

    def get_text(self, tag):
        if tag:
            return tag.text.strip()
        else:
            return ''

    def parse_items(self, response):
        soup = BeautifulSoup(response.body)
        movie = Movie()
        movie['name'] = soup.h1.span.text
        movie['rating'] = self.get_text(soup.find('div', attrs={'class': 'titlePageSprite'}))
        movie['users_rated'] = self.get_text(soup.find('span', attrs={'itemprop': 'ratingCount'}))
        movie['duration'] = self.get_text(soup.find('time', attrs={'itemprop': 'duration'}))
        movie['short_description'] = self.get_text(soup.find('p', attrs={'itemprop': 'description'}))
        movie['release_date'] = self.get_text(soup.find('a', attrs={'title': 'See all release dates'}))
        movie['genre'] = [gnr.text for gnr in soup.find_all('span', attrs={'itemprop': 'genre'})]

        director_div = soup.find('div', attrs={'itemprop': 'director'})
        movie['directors'] = [itm.text for itm in director_div.find_all('a', attrs={'itemprop': 'url'})]

        writers_div = soup.find('div', attrs={'itemprop': 'creator'})
        movie['writers'] = [itm.text for itm in writers_div.find_all('a', attrs={'itemprop': 'url'})]

        actors_div = soup.find('div', attrs={'itemprop': 'actors'})
        movie['actors'] = [itm.text for itm in actors_div.find_all('a', attrs={'itemprop': 'url'})[:-1]]

        awards_ranks_div = soup.find('div', attrs={'id': 'titleAwardsRanks'})
        movie['ranking'] = awards_ranks_div.strong.text.split('#')[1]
        movie['awards'] = ''.join(filter(None, [itm.string for itm in awards_ranks_div.find_all('span')]))

        return movie
