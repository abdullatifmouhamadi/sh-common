#!/usr/bin/python
from .core_model import CoreModel
class Location(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._company_id = None
        self._active = None
        self._usage = 'supplier'                                      
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "stock.location"

    def get_name(self):
        return self._name
    def get_company_id(self):
        return self._company_id
    def get_usage(self):
        return self._usage
    def get_active(self):
        return self._active
    
    def set_name(self, value):
        self._name = value
    def set_company_id(self, value):
        self._company_id = value
    def set_usage(self, value):
        self._usage = value
    def set_active(self, value):
        self._active = value


    name = property(get_name, set_name, None, "I'm a property.")
    company_id = property(get_company_id, set_company_id, None, "I'm a property.")
    usage = property(get_usage, set_usage, None, "I'm a property.")
    active = property(get_active, set_active, None, "I'm a property.")

