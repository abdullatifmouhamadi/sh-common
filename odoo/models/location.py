#!/usr/bin/python
from models.core_model import CoreModel
class Location(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._partner_id = None
        self._usage = 'supplier'                                      
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "stock.location"

    def get_name(self):
        return self._name
    def get_partner_id(self):
        return self._partner_id
    def get_usage(self):
        return self._usage
    
    def set_name(self, value):
        self._name = value
    def set_partner_id(self, value):
        self._partner_id = value
    def set_usage(self, value):
        self._usage = value
        
    name = property(get_name, set_name, None, "I'm a property.")
    partner_id = property(get_partner_id, set_partner_id, None, "I'm a property.")
    usage = property(get_usage, set_usage, None, "I'm a property.")
