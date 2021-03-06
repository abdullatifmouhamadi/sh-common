#!/usr/bin/python
from models.core_model import CoreModel
class SupplierInfo(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._company_id = None
        self._currency_id = None
        self._delay = None
        self._min_qty = None
        self._price = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "product.supplierinfo"
        

    def get_name(self):
        return self._name
    def get_company_id(self):
        return self._company_id
    def get_currency_id(self):
        return self._currency_id
    def get_delay(self):
        return self._delay
    def get_min_qty(self):
        return self._min_qty
    def get_price(self):
        return self._price
    
    def set_name(self, value):
        self._name = value
    def set_company_id(self, value):
        self._company_id = value
    def set_currency_id(self, value):
        self._currency_id = value
    def set_delay(self, value):
        self._delay = value
    def set_min_qty(self, value):
        self._min_qty = value
    def set_price(self, value):
        self._price = value
    
    name = property(get_name, set_name, None, "I'm a property.")
    company_id = property(get_company_id, set_company_id, None, "I'm a property.")
    currency_id = property(get_currency_id, set_currency_id, None, "I'm a property.")
    delay = property(get_delay, set_delay, None, "I'm a property.")
    min_qty = property(get_min_qty, set_min_qty, None, "I'm a property.")
    price = property(get_price, set_price, None, "I'm a property.")
    