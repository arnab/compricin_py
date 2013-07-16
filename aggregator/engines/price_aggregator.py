from aggregator.engines.store_config import StoreConfig
from aggregator.engines.scraper import Scraper
from aggregator.engines.parser import Parser

class PriceAggregator(object):
    """finds prices of given items acorss sites"""
    def __init__(self, search_term, stores):
        super(PriceAggregator, self).__init__()
        self.search_term = search_term
        self.stores = stores

    def aggregated_prices(self):
        for store in StoreConfig.stores():
            search_results_page = Scraper().scrape(store, self.search_term)
            parser = Parser(store, search_results_page)
            for item in parser.items():
                title = parser.title(item)
                price = parser.price(item)
                if len(title) > 0:
                    raise NotImplementedError([title[0].text_content()])
