#!/usr/bin/python
from models.core_model import CoreModel
class Partner(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._is_company = True
        self._customer = False
        self._supplier = True
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "res.partner"

    def get_name(self):
        return self._name
    def get_is_company(self):
        return self._is_company
    def get_customer(self):
        return self._customer
    def get_supplier(self):
        return self._supplier
    
    def set_name(self, value):
        self._name = value
    def set_is_company(self, value):
        self._is_company = value
    def set_customer(self, value):
        self._customer = value
    def set_supplier(self, value):
        self._supplier = value

    name = property(get_name, set_name, None, "I'm a property.")
    is_company = property(get_is_company, set_is_company, None, "I'm a property.")
    customer = property(get_customer, set_customer, None, "I'm a property.")
    supplier = property(get_supplier, set_supplier, None, "I'm a property.")
    

    