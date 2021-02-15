#!/usr/bin/python
import erppeek
import csv
from helper import Helper
from product_import import ProductImport


from models.product import Product
from models.supplierinfo import SupplierInfo
from models.partner import Partner
from models.location import Location


from models.product import Product
from models.product_template import ProductTemplate

from models.product_image import ProductImage
from models.product_public_category import ProductPublicCategory


from helpers.attr_dict import AttrDict



def main():

     
    auth = {'user':'bourou01@gmail.com',
            'pwd':'afandi',
            'dbname':'TEST2',
            'server':'http://92.222.94.3:8069/'}
     
#     auth = {'user':'bourou01@gmail.com',
#             'pwd':'zzzzaaaa',
#             'dbname':'TEST6',
#             'server':'http://localhost:8069'}
     
#     auth = {'user':'bourou01@gmail.com',
#             'pwd':'afandi',
#             'dbname':'HOUDA2',
#             'server':'http://localhost:8069'}
    

    
    # http://www.firstclasscomputerconsulting.com/OpenERP/OpenERP70Videos/tabid/145/articleType/ArticleView/articleId/2/Import-data-into-OpenERP-7-using-XML-RPC.aspx
    api = erppeek.Client(auth['server'], auth['dbname'],auth['user'],auth['pwd'])
    Helper.set_client(api)
    
    
#     p = api.read('product.template', [23],[])
#     print(p)
#     return


    productImport = ProductImport(api)





    def importCdiscountPro():
        reader = csv.reader(open('catalogue_CdiscountPro.CSV','r', newline='', encoding='iso8859-1'), delimiter=';')
        
        limite = 1000000
        counter = 0
        start = 20450
        
        vendor = "CdiscountPro"
        
        # S'il n'existe pas on crée un nouveau fournisseur sinon on le récupère en fonction de son nom
        partner = productImport.get_or_create_partner(Partner(name      =vendor,
                                                              is_company=True,
                                                              customer  =False,
                                                              supplier  =True))
        location = productImport.get_or_create_location(Location(name       =vendor,
                                                                 partner_id =partner.id,
                                                                 usage      ='supplier'))
    
        mainCategory = productImport.get_or_create_product_public_category(ProductPublicCategory(name='Cdiscount'))
    
        for row in reader:
            
            if (counter>0 and counter>=start):
                
                o = rowToDictCdiscoutPro(row)
                
                if (o.Categorie_Niveau_2 not in ['VIN', 'ALCOOL']):
                
                    print(str(counter) + '-' + o.References_Cdiscount)
    
                    productCategories = []
                    # Categ stream 1
                    manufacturerCat = productImport.get_or_create_product_public_category(ProductPublicCategory(name = o.Categorie_Niveau_2,
                                                                                                                parent_id = mainCategory.id)) 
                    
                    productCategories.append(manufacturerCat.id)
                    
                    image_urls = {}
    
                    codebar = o.References_Cdiscount+'@'+o.Code_EAN
                    vendor_price = o.Prix_HT
                    
                
                    
                    # Calcul prix de vente
                    fret = ( o.Poids*(10.5) + (vendor_price * 5/100) )
                    cout_produit = vendor_price + fret
                    octroi_de_mer_1 = cout_produit * (27.5/100)        
                    octroi_de_mer_2 = cout_produit * (2.5/100)
                    prix_de_revient = cout_produit + octroi_de_mer_1 + octroi_de_mer_2 # prix avant marge
                    marge = prix_de_revient * (25/100)
                    prix_vente = prix_de_revient + marge

                    newSupplierInfo = SupplierInfo( name = partner.id,
                                                    company_id = 1,
                                                    currency_id = 1,
                                                    delay = 7,
                                                    min_qty = 1,
                                                    price = vendor_price)
                    supplierinfo = newSupplierInfo.provide(['name', 'company_id', 'currency_id','delay','min_qty','price'])
    
                    productTemplate = ProductTemplate(name = o.Libelle,
                                                      type = 'product',
                                                      valuation = 'real_time',
                                                      cost_method = 'standard',
                                                      website_published = True,
                                                      sale_ok = True,
                                                      purchase_ok = True,
                                                      location_id = location.id,
                                                      barcode = codebar,
                                                      standard_price = prix_de_revient,
                                                      list_price = prix_vente,
                                                      categ_id = 6, #Tous / En vente / Physique
                                                      weight = o.Poids,
                                                      public_categ_ids = [(6,False,productCategories)],
                                                      image = Helper.image_url_to_base64(o.Liens_Images),
                                                      seller_ids = [(0,False,supplierinfo)],
                                                      description_sale = o.Description_principale)
                    
                    print(productTemplate)
                    productImport.get_or_create_product(productTemplate, newSupplierInfo, partner, location, image_urls, 0);
                
                
            if counter >= limite:
                break 
            counter+=1
    
        


    def rowToDictCdiscoutPro(row):

        # Formattage
        res = { 'References_Cdiscount':row[0],
                'Code_EAN':row[1],
                'Categorie_Niveau_1':row[2],
                'Categorie_Niveau_2':row[3],
                'Categorie_Niveau_3':row[4],
                'Categorie_Niveau_4':row[5],
                'Mode_de_livraison':row[6],
                'Marque':row[7],
                'Libelle':row[8],
                'Description_principale':row[9],
                'prix_barre':row[10],
                'Prix_HT':Helper.numFloat(row[11]),
                'Prix_TTC':row[12],
                'EcoTaxe_TTC':row[13],
                'Taux_de_TVA':row[14],
                'Liens_Images':row[15],
                'Poids':Helper.numFloat(row[16]) / 1000}
        return AttrDict(res)
    
    


    
    
    

    def importFKAutomotive():
        reader = csv.reader(open('ALL_FK_ARTICLE_fr.csv','r'), delimiter=';')
        
        limite = 100000
        counter = 0
        start = 0
        
        vendor = "FK-Automotive"
        # S'il n'existe pas on crée un nouveau fournisseur sinon on le récupère en fonction de son nom
        partner = productImport.get_or_create_partner(Partner(name      =vendor,
                                                              is_company=True,
                                                              customer  =False,
                                                              supplier  =True))
        location = productImport.get_or_create_location(Location(name       =vendor,
                                                                 partner_id =partner.id,
                                                                 usage      ='supplier'))
        mainCategory = productImport.get_or_create_product_public_category(ProductPublicCategory(name='Automobiles'))

        for row in reader:
            if (row[1].isdigit() and counter>=start):
                
                o = rowToDictFKAutomotive(row)
                print(str(counter) + '-' + o.article_nr)
                
                
                productCategories = []
                 
                # Categ stream 1
                manufacturerCat = productImport.get_or_create_product_public_category(ProductPublicCategory(name = o.car_manufacturer,
                                                                                                            parent_id = mainCategory.id))
                productCategories.append(manufacturerCat.id)
                # Categ stream 2
                cats2 = [x.strip() for x in o.category.split('>')]
                if len(cats2) == 1:
                    aCat = productImport.get_or_create_product_public_category(ProductPublicCategory(name = cats2[0]))
                    productCategories.append(aCat.id)
                elif len(cats2) == 2:
                    mainCat = productImport.get_or_create_product_public_category(ProductPublicCategory(name = cats2[0]))
                    subCat = productImport.get_or_create_product_public_category(ProductPublicCategory(name = cats2[1],
                                                                                                       parent_id = mainCat.id))
                    productCategories.append(subCat.id)
                else:
                    print ("ERROR")
                    raise ValueError("Taille Catégorie non gerée")
                
                
                
                #urls = {row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27]}
                image_urls = {o.picture2,o.picture3,o.picture4,o.picture5,o.picture6,o.picture7,o.picture8}

                codebar = o.article_nr+'@'+o.ean
                vendor_price = o.dealer_price_a_netto
                
                # Calcul prix de vente
                fret = ( o.Weight*(10.5) + (vendor_price * 5/100) )
                cout_produit = vendor_price + fret
                octroi_de_mer_1 = cout_produit * (27.5/100)        
                octroi_de_mer_2 = cout_produit * (2.5/100)
                prix_de_revient = cout_produit + octroi_de_mer_1 + octroi_de_mer_2 # prix avant marge
                marge = prix_de_revient * (25/100)
                prix_vente = prix_de_revient + marge


                
                newSupplierInfo = SupplierInfo( name = partner.id,
                                                company_id = 1,
                                                currency_id = 1,
                                                delay = 7,
                                                min_qty = 1,
                                                price = vendor_price)
                supplierinfo = newSupplierInfo.provide(['name', 'company_id', 'currency_id','delay','min_qty','price'])


                 
                productTemplate = ProductTemplate(name = o.title,
                                                  type = 'product',
                                                  valuation = 'real_time',
                                                  cost_method = 'standard',
                                                  website_published = True,
                                                  sale_ok = True,
                                                  purchase_ok = True,
                                                  location_id = location.id,
                                                  barcode = codebar,
                                                  standard_price = prix_de_revient,
                                                  list_price = prix_vente,
                                                  categ_id = 6, #Tous / En vente / Physique
                                                  weight = o.Weight,
                                                  public_categ_ids = [(6,False,productCategories)],
                                                  #image = Helper.image_url_to_base64(o.picture1),
                                                  seller_ids = [(0,False,supplierinfo)],
                                                  description_sale = o.short_desc)
                
                #print(productTemplate)
                productImport.get_or_create_product(productTemplate, newSupplierInfo, partner, location, image_urls, o.stock);
    
            if counter >= limite:
                break 
            counter+=1
            
            
    def rowToDictFKAutomotive(row):
        # Formattage
        row[6] = Helper.numFloat(row[6])
        row[9] = Helper.numFloat(row[9])
        row[10] = Helper.numInt(row[10])

        res = { 'article_nr':row[0],
                'ean':row[1],
                'Brand':row[2],
                'Color':row[3],
                'car_manufacturer':row[4],
                'car_model':row[5],
                'dealer_price_a_netto':row[6],
                'dealer_price_b_netto':row[7],
                'dealer_price_c_netto':row[8],
                'Weight':row[9],
                'stock':row[10],
                'uvp_price':row[11],
                'shop_price':row[12],
                #
                #
                #
                #
                'title':row[17],
                'short_desc':row[18],
                'long_desc':row[19],
                'picture1':row[20],
                'picture2':row[21],
                'picture3':row[22],
                'picture4':row[23],
                'picture5':row[24],
                'picture6':row[25],
                'picture7':row[26],
                'picture8':row[27],
                'category':row[28]}
        return AttrDict(res)
            
    importCdiscountPro()  
    #importFKAutomotive()



if __name__ == '__main__':
    main()
    
    
    