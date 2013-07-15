class StoreConfig(object):
    CONFIG = {
        'flipkart': {
            'search_url': "http://www.flipkart.com/search/a/all?query=%s",
            'item_css_path': ".fk-product-thumb",
            'title_css_path': "a.fk-anchor-link",
            'price_css_path': ".fk-price .price",
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
            'price_css_path': ".price .price",
        },
    }

    @classmethod
    def stores(self):
        return StoreConfig.CONFIG.keys()
