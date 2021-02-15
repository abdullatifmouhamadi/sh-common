#!/usr/bin/python
from .core_model import CoreModel
class ProductPublicCategory(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._child_id = None
        self._parent_id = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "product.public.category"

    def get_name(self):
        return self._name
    def get_child_id(self):
        return self._child_id
    def get_parent_id(self):
        return self._parent_id

    
    def set_name(self, value):
        self._name = value
    def set_child_id(self, value):
        self._child_id = value
    def set_parent_id(self, value):
        self._parent_id = value


    name = property(get_name, set_name, None, "I'm a property.")
    child_id = property(get_child_id, set_child_id, None, "I'm a property.")
    parent_id = property(get_parent_id, set_parent_id, None, "I'm a property.")

    