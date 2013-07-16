import logging
log = logging.getLogger(__name__)

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
        for store in self.stores:
            log.info("Searching %s for [%s]" % (store, self.search_term))
            search_results_page = Scraper().scrape(store, self.search_term)
            parser = Parser(store, search_results_page)
            for item in parser.items():
                title_elem = parser.title(item)
                title = len(title_elem) > 0 and title_elem[0].text_content()

                price_elem = parser.price(item)
                price = len(price_elem) > 0 and price_elem[0].text_content()

                log.debug("%s: '%s' [%s]" % (store, title, price))
