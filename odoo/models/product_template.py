#!/usr/bin/python
from models.core_model import CoreModel
class ProductTemplate(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._categ_id = None
        self._location_id = None
        self._public_categ_ids = None
        self._seller_ids= None
        self._name = None
        self._barcode = None
        self._weight = None
        self._purchase_ok = True
        self._image = None
        self._sale_ok = True
        self._website_published = True
        self._cost_method = 'standard'
        self._list_price = None
        self._standard_price = None
        self._description_sale = None
        self._type = None
        self._valuation = None
        
        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "product.template"
        
    def get_categ_id(self):
        return self._categ_id
    def get_location_id(self):
        return self._location_id
    def get_public_categ_ids(self):
        return self._public_categ_ids
    def get_seller_ids(self):
        return self._seller_ids
    def get_name(self):
        return self._name
    def get_barcode(self):
        return self._barcode
    def get_weight(self):
        return self._weight
    def get_purchase_ok(self):
        return self._purchase_ok
    def get_image(self):
        return self._image
    def get_sale_ok(self):
        return self._sale_ok
    def get_website_published(self):
        return self._website_published
    def get_cost_method(self):
        return self._cost_method
    def get_list_price(self):
        return self._list_price
    def get_standard_price(self):
        return self._standard_price
    def get_description_sale(self):
        return self._description_sale
    def get_type(self):
        return self._type
    def get_valuation(self):
        return self._valuation

    def set_categ_id(self, value):
        self._categ_id = value
    def set_location_id(self, value):
        self._location_id = value
    def set_public_categ_ids(self, value):
        self._public_categ_ids = value
    def set_seller_ids(self, value):
        self._seller_ids = value
    def set_name(self, value):
        self._name = value
    def set_barcode(self, value):
        self._barcode = value
    def set_weight(self, value):
        self._weight = value
    def set_purchase_ok(self, value):
        self._purchase_ok = value
    def set_image(self, value):
        self._image = value
    def set_sale_ok(self, value):
        self._sale_ok = value
    def set_website_published(self, value):
        self._website_published = value
    def set_cost_method(self, value):
        self._cost_method = value
    def set_list_price(self, value):
        self._list_price = value
    def set_standard_price(self, value):
        self._standard_price = value
    def set_description_sale(self, value):
        self._description_sale = value
    def set_type(self, value):
        self._type = value
    def set_valuation(self, value):
        self._valuation = value
    
    categ_id = property(get_categ_id, set_categ_id, None, "I'm a property.")
    location_id = property(get_location_id, set_location_id, None, "I'm a property.")
    public_categ_ids = property(get_public_categ_ids, set_public_categ_ids, None, "I'm a property.")
    seller_ids= property(get_seller_ids, set_seller_ids, None, "I'm a property.")
    name = property(get_name, set_name, None, "I'm a property.")
    barcode = property(get_barcode, set_barcode, None, "I'm a property.")
    weight = property(get_weight, set_weight, None, "I'm a property.")
    purchase_ok = property(get_purchase_ok, set_purchase_ok, None, "I'm a property.")
    image = property(get_image, set_image, None, "I'm a property.")
    sale_ok = property(get_sale_ok, set_sale_ok, None, "I'm a property.")
    website_published = property(get_website_published, set_website_published, None, "I'm a property.")
    cost_method = property(get_cost_method, set_cost_method, None, "I'm a property.")
    list_price = property(get_list_price, set_list_price, None, "I'm a property.")
    standard_price = property(get_standard_price, set_standard_price, None, "I'm a property.")
    description_sale = standard_price = property(get_description_sale, set_description_sale, None, "I'm a property.")
    type = property(get_type, set_type, None, "I'm a property.")
    valuation = property(get_valuation, set_valuation, None, "I'm a property.")
    
    
    
    