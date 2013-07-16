import urllib2

from aggregator.engines.store_config import StoreConfig

class Scraper(object):
    def scrape(self, store, search_term):
        search_term = urllib2.quote(search_term)
        search_url = StoreConfig.search_url(store)
        search_url = search_url.replace('%s', search_term)
        return urllib2.urlopen(search_url).read()
