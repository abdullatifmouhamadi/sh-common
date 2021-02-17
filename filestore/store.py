import urllib.request
# http://sametmax.com/fichiers-temporaires-avec-tempfile-en-python/
import uuid
import os, io
from pprint import pprint
import base64
from pathlib import Path
import requests

from .config import IMAGES_CACHE_DIR

def ensure_dir(file_path):
    #print(file_path)
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)



class FileStore(object):
    def __init__(self, dirname = None):
        self.dirname = dirname

        ensure_dir(IMAGES_CACHE_DIR)
        
    # https://www.scivision.dev/python-switch-urlretrieve-requests-timeout/
    def urlretrieve3(self, url: str, fn: Path):
        with fn.open('wb') as f:
            f.write(requests.get(url, allow_redirects=True, timeout=1).content)


    """
    def process_filepath(self, url):
        #filename = self.process_filename(url)
        filepath = IMAGES_CACHE_DIR# + filename
        return filepath

    def process_filename(self, url):
        filename = str(uuid.uuid5(uuid.NAMESPACE_URL, url)) + '.jpg'
        return filename
    """

    def process_compressed_filename(self, url, extension):
        filename = str(uuid.uuid5(uuid.NAMESPACE_URL, url)) +'_compressed'+ '.' + extension
        filepath = IMAGES_CACHE_DIR + filename
        return filepath
        

    def retrive_url(self, url):
        filename = str(uuid.uuid5(uuid.NAMESPACE_URL, url)) + '.jpg'
        filepath = IMAGES_CACHE_DIR + filename
        if not os.path.exists( filepath ) or not os.path.getsize( filepath ) > 0:
            try:
                self.urlretrieve3( url , Path(filepath) )
            except requests.exceptions.ReadTimeout:
                return None
            except requests.exceptions.ConnectTimeout:
                return None
            except requests.exceptions.ConnectionError:
                return None

            if os.path.getsize( filepath ) == 0:
                return None

        return filepath

    def file_content(self, filepath):
        if filepath == None:
            return None
        else:
            fd = io.open(filepath, "rb")
            content = fd.read()
            fd.close()
            return content#base64.b64encode(content)

    def file_content_base64(self, filepath):
        if filepath == None:
            return None
        else:
            fd = io.open(filepath, "rb")
            content = fd.read()
            fd.close()
            return base64.b64encode(content)

    def urlretrieve(self, url):
        filepath = self.retrive_url(url)
        content  = self.file_content(filepath)

        if content != None:
            return content.decode("latin-1")
        else:
            return None

    def urlretrieve_base64(self, url):
        filepath = self.retrive_url(url)
        content  = self.file_content_base64(filepath)

        if content != None:
            return content.decode("utf-8")
        else:
            return None