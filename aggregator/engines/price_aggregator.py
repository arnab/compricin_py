class PriceAggregator(object):
    """finds prices of given items acorss sites"""
    def __init__(self, search_term, stores):
        super(PriceAggregator, self).__init__()
        self.search_term = search_term
        self.stores = stores

    def aggregated_prices(self):
        raise NotImplementedError("TODO")
