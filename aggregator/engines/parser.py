import lxml.html
from cssselect import HTMLTranslator

from aggregator.engines.store_config import StoreConfig

class Parser(object):
    def __init__(self, store, page):
        super(Parser, self).__init__()
        self.store = store
        self.doc = lxml.html.document_fromstring(page)

    def items(self):
        return self.doc.cssselect(StoreConfig.item_css_path(self.store))[0:5]

    def title(self, doc):
        return doc.cssselect(StoreConfig.title_css_path(self.store))

    def price(self, doc):
        return doc.cssselect(StoreConfig.price_css_path(self.store))
