#!/usr/bin/python
from models.product_template import ProductTemplate
class Product(ProductTemplate):
    def __init__(self, *initial_data, **kwargs):
        self._product_tmpl_id = None
        ProductTemplate.__init__(self, *initial_data, **kwargs)
        self._model = "product.product"
        
    def get_product_tmpl_id(self):
        return self._product_tmpl_id

    def set_product_tmpl_id(self, value):
        self._product_tmpl_id = value
    
    product_tmpl_id = property(get_product_tmpl_id, set_product_tmpl_id, None, "I'm a property.")

        

    
    