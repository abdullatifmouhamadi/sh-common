#!/usr/bin/python
from .core_model import CoreModel
class ProductImage(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._image = None
        self._product_tmpl_id = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "product.image"

    def get_name(self):
        return self._name
    def get_image(self):
        return self._image
    def get_product_tmpl_id(self):
        return self._product_tmpl_id

    
    def set_name(self, value):
        self._name = value
    def set_image(self, value):
        self._image = value
    def set_product_tmpl_id(self, value):
        self._product_tmpl_id = value


    name = property(get_name, set_name, None, "I'm a property.")
    image = property(get_image, set_image, None, "I'm a property.")
    product_tmpl_id = property(get_product_tmpl_id, set_product_tmpl_id, None, "I'm a property.")

    