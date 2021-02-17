#!/usr/bin/python


# Update quantity of a product
# https://www.odoo.com/fr_FR/forum/aide-1/question/update-quantity-on-hand-via-xmlrpc-and-php-82281
# https://stackoverflow.com/questions/35968674/update-a-product-field-quantity-on-hand-with-xmlrpc

from ..helpers.helper import Helper, read_if_exists

from ..models.product import Product, ProductCategory
from ..models.supplierinfo import SupplierInfo
from ..models.partner import Partner
from ..models.location import Location
from ..models.product_image import ProductImage
from ..models.product import Product
from ..models.product_template import ProductTemplate
from ..models.product_public_category import ProductPublicCategory
from ..models.supplierinfo import SupplierInfo

from pprint import pprint


class ProductImport:

    def __init__(self, client):
        self.api = client
        #self.product = "product.product"
        #self.template = "product.template"
        #self.supplierinfo = "product.supplierinfo"
        #self.image = "product.image"
        self.stock = "stock.move"
        #self.partner = "res.partner"
        self.company = "res.company"
        #self.location = "stock.location"
        self.stock_change_product_qty = "stock.change.product.qty"
            
        self.product_public_category = "product.public.category"
        #self.product_image = "product.image"


    def __process_images_urls(self,codebar, urls, product_tmpl_id):
        count=1
        for url in urls:
            count+=1
            self.get_or_create_image_url(ProductImage(name=codebar+'@'+str(count),
                                                      image = Helper.image_url_to_base64(url),
                                                      product_tmpl_id = product_tmpl_id))
    
    
    
    
    def get_or_create_image_url(self, imageObj):
        domain = [('name','=',imageObj.name)]
        model = Helper.read_if_exists(imageObj.model, domain, ['id']) # nom unique
        if model == False: # Create a new one
            model = self.api.model(imageObj.model).create(imageObj.provide(['name','image','product_tmpl_id']))
        else: # then update and return it
            self.api.write(imageObj.model, [model[0]['id']],imageObj.provide(['name','image','product_tmpl_id']))
        return ProductImage(Helper.read_if_exists(imageObj.model, domain, imageObj.props())[0])
    
    
    

    def get_or_create_product_public_category(self, productPublicCategoryObj):
        domain = [('name','=',productPublicCategoryObj.name)]
        model = read_if_exists(api=self.api, model=productPublicCategoryObj.model, domain=domain, fields=['id']) # nom unique
        if model == False: # Create a new one
            model = self.api.model(productPublicCategoryObj.model).create(productPublicCategoryObj.provide(['name','child_id','parent_id']))
        else: # then update and return it
            self.api.write(productPublicCategoryObj.model, [model[0]['id']],productPublicCategoryObj.provide(['name','child_id','parent_id']))
        return ProductPublicCategory(read_if_exists(api=self.api, model=productPublicCategoryObj.model, domain=domain, fields=productPublicCategoryObj.props())[0])

    def get_or_create_product_category(self, productCategoryObj):
        domain = [('name','=',productCategoryObj.name)]
        model = read_if_exists(api=self.api, model=productCategoryObj.model, domain=domain, fields=['id']) # nom unique
        if model == False: # Create a new one
            model = self.api.model(productCategoryObj.model).create(productCategoryObj.provide(['name','child_id','parent_id']))
        else: # then update and return it
            self.api.write(productCategoryObj.model, [model[0]['id']],productCategoryObj.provide(['name','child_id','parent_id']))
        return ProductCategory(read_if_exists(api=self.api, model=productCategoryObj.model, domain=domain, fields=productCategoryObj.props())[0])





    def __update_quantity(self, product_id, location_id, new_quantity):
        change_id = self.api.model(self.stock_change_product_qty).create({
                'product_id': product_id,
                'location_id': location_id,
                'new_quantity': new_quantity})
        change_id = change_id.read()['id']        
        self.api.execute(self.stock_change_product_qty, 'change_product_qty',[change_id])
        return change_id




    def __get_product_by_product_tmpl_id(self, tmpl_id):
        dummyProduct = Product()
        domain = [('product_tmpl_id','=',tmpl_id)]
        return Product(self.api.model(dummyProduct.model).read(domain, dummyProduct.props())[0])
    


    
    
    
    
    def get_or_create_partner(self, partnerObj):
        domain = [('name','=',partnerObj.name)]
        model = read_if_exists(api=self.api, model=partnerObj.model, domain=domain, fields=['id']) # nom unique
        if model == False: # Create a new one
            model = self.api.model(partnerObj.model).create(partnerObj.provide(['name','is_company','customer','supplier']))
        else: # then update and return it
            self.api.write(partnerObj.model, [model[0]['id']],partnerObj.provide(['name','is_company','customer','supplier']))
        return Partner(read_if_exists(api = self.api, model=partnerObj.model, domain=domain, fields=partnerObj.props())[0])



    def get_or_create_location(self, locationObj):
        domain = [('name','=',locationObj.name)]
        model = read_if_exists(api=self.api, model=locationObj.model, domain=domain, fields=[]) # nom unique

        #print(model)
        if model == False: # Create a new one
            model = self.api.model(locationObj.model).create(locationObj.provide(['name','usage','active']))
        else: # then update and return it
            self.api.write(locationObj.model, [model[0]['id']],locationObj.provide(['name','usage','active']))
        return Location(read_if_exists(api=self.api, model=locationObj.model, domain=domain, fields=locationObj.props())[0])










    def get_supplierinfo_by(self, partner_id, product_tmpl_id):
        dummySupplierInfo = SupplierInfo()
        domain = [('name','=',partner_id),('product_tmpl_id','=',product_tmpl_id)]
        model = read_if_exists(api=self.api, model=dummySupplierInfo.model, domain=domain, fields=dummySupplierInfo.props()) # nom unique
        if model == False: # Create a new one
            return False
        else:
            return SupplierInfo(model[0])
    
        
    def get_or_create_product(self, productTemplate, newSupplierInfo, partner, location, image_urls, product_stock):
        domain = [('barcode','=',productTemplate.barcode)]
        # On vérifie si un produit existe en fonction d'un codebar donné
        template = read_if_exists(api=self.api, model=productTemplate.model, domain=domain, fields=['id','seller_ids']) #id, seller_ids, product_tmplt_id

        pprint(template[0])

        if (template == False): # Le produit n'existe pas du tlout donc on le crée immédiatement
            print("cas1")
            self.__create_product(productTemplate, image_urls)
        else: # Le produit existe
            tmpProductTemplate = ProductTemplate(template[0])
            if (len(tmpProductTemplate.seller_ids) > 0): # Le produit a au moin un supplierinfo (Fournisseur)
                tmpSupplierInfo = self.get_supplierinfo_by(partner.id, tmpProductTemplate.id)
                if (tmpSupplierInfo != False): # Ce supplierinfo correspond à celui du produit - On fait donc une simple mise à jour
                    print("cas2")
                    #Update ProductTemplate
                    template = self.api.read(productTemplate.model, domain, productTemplate.props())
                    tmpProductTemplate = ProductTemplate(template[0])
                    self.api.write(productTemplate.model, [tmpProductTemplate.id], productTemplate.provide(['valuation','type','standard_price', 'name', 'weight', 'list_price', 'categ_id', 'description_sale', 'available_in_pos']))#,'public_categ_ids']))
                    # Update SupplierInfo
                    tmpProduct = self.__get_product_by_product_tmpl_id(tmpProductTemplate.id)
                    
                    
                    self.api.write(newSupplierInfo.model, [tmpSupplierInfo.id], newSupplierInfo.provide(['name', 'company_id', 'currency_id','delay','min_qty','price']))
                    
                    if (False):
                        self.__update_quantity(tmpProduct.id, location.id, product_stock)
                    # Mise à jour des images - pas forcement
                    if (False):
                        self.__process_images_urls(productTemplate.barcode, image_urls, tmpProductTemplate.id)
                else: # Ce supplierinfo ne correspond pas à celui du produit - On crée un autre produit avec le fournisseur
                    print("cas3")
                    print("ERREUR : codebarre existe déjà")
                    #self.__create_product(params)
            else: # Le produit n'a pas de supplierinfo - On crée un autre produit avec le Fournisseur
                print("cas4")
                self.__create_product(productTemplate, image_urls)
        return None
    def __create_product(self, productTemplate, image_urls):
        template = self.api.model(productTemplate.model).create(productTemplate.provide( ['seller_ids',
                                                                                  'location_id',
                                                                                  'name',
                                                                                  'barcode',
                                                                                  'weight',
                                                                                  'purchase_ok',
                                                                                  #'image',
                                                                                  'sale_ok',
                                                                                  #'website_published',
                                                                                  'cost_method',
                                                                                  'list_price',
                                                                                  'categ_id',
                                                                                  'image_1920', 
                                                                                  'available_in_pos'
                                                                                  #'public_categ_ids',
                                                                                  'standard_price'
                                                                                  'description_sale']))

        productTemplObjCreated = template.read()
        self.__process_images_urls(productTemplate.barcode, image_urls, productTemplObjCreated['id'])
        
        
        