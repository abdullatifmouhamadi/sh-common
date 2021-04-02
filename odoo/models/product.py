from .product_template import ProductTemplate
from .core_model import CoreModel

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




class ProductCategory(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._child_id = None
        self._parent_id = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "product.category"

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

    

class ProductPOSCategory(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._display_name = None
        self._child_id = None
        self._parent_id = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "pos.category"

    def get_name(self):
        return self._name
    def get_display_name(self):
        return self._display_name
    def get_child_id(self):
        return self._child_id
    def get_parent_id(self):
        return self._parent_id

    
    def set_name(self, value):
        self._name = value
    def set_display_name(self, value):
        self._display_name = value
    def set_child_id(self, value):
        self._child_id = value
    def set_parent_id(self, value):
        self._parent_id = value


    name = property(get_name, set_name, None, "I'm a property.")
    display_name = property(get_display_name, set_display_name, None, "I'm a property.")
    child_id = property(get_child_id, set_child_id, None, "I'm a property.")
    parent_id = property(get_parent_id, set_parent_id, None, "I'm a property.")



class ProductAccountTax(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None
        self._amount = None
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "account.tax"

    def get_name(self):
        return self._name
    def get_amount(self):
        return self._amount
    
    def set_name(self, value):
        self._name = value
    def set_amount(self, value):
        self._amount = value

    name = property(get_name, set_name, None, "I'm a property.")
    amount = property(get_amount, set_amount, None, "I'm a property.")
