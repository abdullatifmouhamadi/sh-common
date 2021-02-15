#!/usr/bin/python
import base64 #file encode
from urllib.request import urlopen #file download from url
import numbers
from urllib.error import HTTPError

class Helper(object):
    
    api = None
    
    @staticmethod
    def set_client(client):
        Helper.api = client
    
    @staticmethod
    def exists(model,domain):
        if Helper.api.count(model, domain) > 0:
            return True
        else:
            return False
    
    """
    @staticmethod
    def read_if_exists(model, domain, fields=[]):
        if Helper.exists(model, domain) == True:
            return Helper.api.read(model, domain, fields)
        else:
            return False 
    """
        
    
    @staticmethod
    def image_url_to_base64(link):
        try:
            return base64.b64encode(urlopen(link).read()).decode('utf-8')
            
        except HTTPError as err:
            if err.code == 404:
                return False
            else:
                return False
                #raise
                       

        
        
        
        

    @staticmethod
    def save(file_name, stream):
        text_file = open(file_name, "w")
        text_file.write(stream)
        text_file.close()


    @staticmethod
    def numFloat(val):
        return float(val.replace(',','.'))


    @staticmethod
    def numInt(val):
        return int(val)




def exists(api, model,domain):
    if api.count(model, domain) > 0:
        return True
    else:
        return False


def read_if_exists(api, model, domain, fields=[]):
    if exists(api, model, domain) == True:
        return api.read(model, domain, fields)
    else:
        return False 