class Item:

    def __init__(self, name, cost, tax, tip):
        self.name = name
        self.cost = cost
        self.real_cost = self._get_real_cost(tax, tip)

    # --- helper methods --- #

    def _get_perc_fee(amount, perc_fee):
        """
        Returns perc_fee% of amount
        """
        return perc_fee*amount

    def _get_real_cost(self, tax, tip):
        """
        float tax: amount tax levied on this item as a float.
        float tip: amount to tip
        """
        return self.cost + _get_perc_fee(self.cost, tax) + 
            _get_perc_fee(self.cost, tip)

class Bill:

    """
    Collection of items that share the same tax and tip.
    """

    def __init__(self, tax, tip, items=[]):
        self.tax = tax
        self.tip = tip
        self.items = items

    def add_item(self, name, cost):
        new_item = Item(name, cost, self.tax, self.tip)
        self.items.append(new_item)

    def get_total_cost(self):
        return sum([item.real_cost for item in self.items])