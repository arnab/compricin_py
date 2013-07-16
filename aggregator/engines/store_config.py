class StoreConfig(object):
    CONFIG = {
        'flipkart': {
            'search_url': "http://www.flipkart.com/search/a/all?query=%s",
            'item_css_path': ".browse-product",
            'title_css_path': "a.fk-display-block",
            'price_css_path': ".pu-price .pu-final",
            'max_items': 5,
        },
        'junglee': {
            'search_url': "http://www.junglee.com/mn/search/junglee?field-keywords=%s",
            'item_css_path': ".result.product",
            'title_css_path': ".data a.title",
            'price_css_path': ".data .price",
        },
        'ebay.in': {
            'search_url': "http://search.ebay.in/%s",
            'item_css_path': "#ResultSetItems *[itemprop=offers]",
            'title_css_path': "a.vip",
            'price_css_path': "*[itemprop=price]",
        },
        'infibeam': {
            'search_url': "http://www.infibeam.com/search?q=%s",
            'item_css_path': "#search_result li",
            'title_css_path': ".title",
            'price_css_path': ".price .normal",
        },
    }

    @classmethod
    def stores(self):
        return StoreConfig.CONFIG.keys()

    @classmethod
    def info(self, store):
        return StoreConfig.CONFIG[store]

    #TODO: The remaining methods here can be dynamically generated
    @classmethod
    def search_url(self, store):
        return self.info(store)['search_url']

    @classmethod
    def item_css_path(self, store):
        return self.info(store)['item_css_path']

    @classmethod
    def title_css_path(self, store):
        return self.info(store)['title_css_path']

    @classmethod
    def price_css_path(self, store):
        return self.info(store)['price_css_path']
