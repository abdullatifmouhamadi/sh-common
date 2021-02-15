
from .core_model import CoreModel

class PartnerCategory(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None

        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "res.partner.category"
    
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value

    name = property(get_name, set_name, None, "I'm a property.")

    

class Partner(CoreModel):
    def __init__(self, *initial_data, **kwargs):
        self._name = None

        self._is_company = True
        self._siret = None
        self._siren = None
        self._nic = None
        self._street = None
        self._city = None
        self._zip = None
        self._category_id = None
        self._nace_id = None
        self._secondary_nace_ids = None
        self._child_ids = None
        self._title = False
        self._function = False
        self._parent_id = False
        self._type = False
        self._country_id = False


        CoreModel.__init__(self, *initial_data, **kwargs)
        self._model = "res.partner"

    def get_name(self):
        return self._name
    def get_is_company(self):
        return self._is_company
    def get_siret(self):
        return self._siret
    def get_siren(self):
        return self._siren
    def get_nic(self):
        return self._nic
    def get_street(self):
        return self._street
    def get_city(self):
        return self._city
    def get_zip(self):
        return self._zip
    def get_category_id(self):
        return self._category_id
    def get_nace_id(self):
        return self._nace_id
    def get_secondary_nace_ids(self):
        return self._secondary_nace_ids
    def get_child_ids(self):
        return self._child_ids
    def get_title(self):
        return self._title
    def get_function(self):
        return self._function
    def get_parent_id(self):
        return self._parent_id
    def get_type(self):
        return self._type
    def get_country_id(self):
        return self._country_id
        


    def set_name(self, value):
        self._name = value
    def set_is_company(self, value):
        self._is_company = value
    def set_siret(self, value):
        self._siret = value
    def set_siren(self, value):
        self._siren = value
    def set_nic(self, value):
        self._nic = value
    def set_street(self, value):
        self._street = value
    def set_city(self, value):
        self._city = value
    def set_zip(self, value):
        self._zip = value
    def set_category_id(self, value):
        self._category_id = value
    def set_nace_id(self, value):
        self._nace_id = value
    def set_secondary_nace_ids(self, value):
        self._secondary_nace_ids = value
    def set_child_ids(self, value):
        self._child_ids = value
    def set_title(self, value):
        self._title = value
    def set_function(self, value):
        self._function = value
    def set_parent_id(self, value):
        self._parent_id = value
    def set_type(self, value):
        self._type = value
    def set_country_id(self, value):
        self._country_id = value


    name = property(get_name, set_name, None, "I'm a property.")
    is_company = property(get_is_company, set_is_company, None, "I'm a property.")
    siret = property(get_siret, set_siret, None, "I'm a property.")
    siren = property(get_siren, set_siren, None, "I'm a property.")
    nic = property(get_nic, set_nic, None, "I'm a property.")
    street = property(get_street, set_street, None, "I'm a property.")
    city = property(get_city, set_city, None, "I'm a property.")
    zip = property(get_zip, set_zip, None, "I'm a property.")
    category_id = property(get_category_id, set_category_id, None, "I'm a property.")
    nace_id = property(get_nace_id, set_nace_id, None, "I'm a property.")
    secondary_nace_ids = property(get_secondary_nace_ids, set_secondary_nace_ids, None, "I'm a property.")
    child_ids = property(get_child_ids, set_child_ids, None, "I'm a property.")
    title = property(get_title, set_title, None, "I'm a property.")
    function = property(get_function, set_function, None, "I'm a property.")
    parent_id = property(get_parent_id, set_parent_id, None, "I'm a property.")
    type = property(get_type, set_type, None, "I'm a property.")
    country_id = property(get_country_id, set_country_id, None, "I'm a property.")
