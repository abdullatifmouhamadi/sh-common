# Update quantity of a product
# https://www.odoo.com/fr_FR/forum/aide-1/question/update-quantity-on-hand-via-xmlrpc-and-php-82281
# https://stackoverflow.com/questions/35968674/update-a-product-field-quantity-on-hand-with-xmlrpc

from .helper import Helper
from .models.partner import Partner, PartnerCategory
from pprint import pprint

"""
to write to one2many field use :

(0, 0,  { values })    link to a new record that needs to be created with the given values dictionary
(1, ID, { values })    update the linked record with id = ID (write *values* on it)
(2, ID)                remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
(3, ID)                cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
(4, ID)                link to existing record with id = ID (adds a relationship)
(5)                    unlink all (like using (3,ID) for all linked records)
(6, 0, [IDs])          replace the list of linked IDs (like using (5) then (4,ID) 
"""

class OdooConnector:

    def __init__(self, client):
        self.api = client

    # https://erppeek.readthedocs.io/en/latest/tutorial.html#browse-the-records



    def get_nace_bycode(self, code):
        obj = self.api.model('res.partner.nace').browse([('code', '=', code)])
        return obj[0] if len(obj) > 0 else False

    def get_all(self, model):
        return self.api.model(model).browse([], limit=None).read()

    def get_or_create_partner_category(self, obj):
        domain = [('name','=',obj.name)]
        model  = Helper.read_if_exists(obj.model, domain, ['id'])
        if model == False: # Create a new one
            model = self.api.model(obj.model).create(obj.provide(['name']))
        return PartnerCategory(Helper.read_if_exists(obj.model, domain, obj.props())[0])


    def get_or_create_entreprise(self, obj):
        domain = [('siren','=',obj.siren), ('nic','=',obj.nic), ('is_company','=',True)]
        model = Helper.read_if_exists(obj.model, domain, ['id']) # nom unique

        if model == False: # Create a new one
            model = self.api.model(obj.model).create(obj.provide(['name','is_company', 'category_id','nace_id', 'siren', 'nic', 'city', 'zip', 'street', 'child_ids', 'secondary_nace_ids', 'country_id']))
        else: # then update and return it
            self.api.write(obj.model, [model[0]['id']],obj.provide(['name','is_company', 'category_id','nace_id', 'siren', 'nic', 'city', 'zip', 'street', 'child_ids', 'secondary_nace_ids', 'country_id']))
        return Partner(Helper.read_if_exists(obj.model, domain, obj.props())[0])


    def get_or_create_contact(self, obj):
        domain = [('name','=',obj.name), ('is_company','=',False)]
        model = Helper.read_if_exists(obj.model, domain, ['id']) # nom unique

        if model == False: # Create a new one
            model = self.api.model(obj.model).create(obj.provide(['name','is_company', 'title', 'function', 'type']))
        else: # then update and return it
            self.api.write(obj.model, [model[0]['id']],obj.provide(['name','is_company', 'title', 'function', 'type']))
        return Partner(Helper.read_if_exists(obj.model, domain, obj.props())[0])

