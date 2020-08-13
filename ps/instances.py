 # /usr/bin/python

from .prestashop import copy_src, install
#from .config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD )
import sh, os
from sh import mysqldump, cp, mysql#, docker
from .utils import logi
from .config import INSTANCES_DIR, TEMPLATE_DOMAIN_NAME

"""
def _release_dir(release):
    return INSTANCES_DIR + release
"""



def _release_dir(release):
    return INSTANCES_DIR + release +'/'

def _install_dir(release):
    release_dir = _release_dir(release)
    return release_dir + 'app/'

def _image_name(release):
    return 'prestashop' + release.replace('.','')

def _database_name(release):
    release_name  = release.replace('.','')
    db_name = "prestashop" + release_name
    return db_name

# @deprecated
"""
def _dump_filename(release):
    database_name = _database_name(release)
    dump          = database_name + '.sql'
    return dump
"""


# @deprecated
"""
def dump_path( release ):
    filename    = _dump_filename(release)
    release_dir = _release_dir(release)
    path        = release_dir + filename
    return path
"""


def loge(msg):
    print( "[error] => " + msg )

def dump_database(release, db_user, db_password):
    database_name = _database_name(release)
    release_dir   = _release_dir(release)
    filename = _dump_filename(release)

    src_database = database_name
    target       = release_dir + '/' + filename
    mysqldump("-u", db_user, "-p" + db_password, src_database, '--result-file', target )


def remove_database(db_user, db_password, db_name):
    logi("Removing db '{}' ...".format(db_name))
    mysql("-u", db_user, "-p" + db_password , "-e", "DROP DATABASE IF EXISTS {}".format( db_name ) )


# @deprecated
"""
def copy_templates(release):
    release_dir   = _release_dir(release)
    cp("-arf", './images/files', release_dir)
    cp("./images/Dockerfile", release_dir)
"""

def setup(installDir, config):
    #install_dir   = _install_dir(release = config['SHOP_PRESTASHOP_RELEASE'])
    #database_name = _database_name(release = config['SHOP_PRESTASHOP_RELEASE'])

    if not os.path.isdir( installDir ):

        #remove_database(config['MYSQL_USER'], config['MYSQL_PASSWORD'], database_name)
        copy_src(installDir = installDir, release = config['SHOP_PRESTASHOP_RELEASE'])

        install(installDir  = installDir, 
                domain      = config['SHOP_HOST_DOMAIN'], #TEMPLATE_DOMAIN_NAME, 
                db_server   = config['MYSQL_HOST'],
                db_name     = config['SHOP_DB_NAME'],#database_name, 
                db_user     = config['MYSQL_USER'], 
                db_password = config['MYSQL_PASSWORD'])

        #dump_database(release = config['SHOP_PRESTASHOP_RELEASE'], db_user = config['MYSQL_USER'], db_password = config['MYSQL_PASSWORD'])
    else:
        logi( "The instance '{}' ".format(config['SHOP_PRESTASHOP_RELEASE']) + 'already exist ...' )
    #copy_templates(release)



# @deprecated
"""
def _image_exists(image_name):
    r = docker("images", "-q", image_name)
    if r=="":
        return False
    return True
"""



""" @deprecated
def build_image(release):
    image_name = _image_name(release)
    release_dir = _release_dir(release)

    if _image_exists(image_name) == True:
        loge("Image {} already exists".format(image_name))
    else:
        logi("Building docker image {}".format(image_name))
        for line in docker('image', 'build', '-t', image_name, release_dir, _iter=True):
            logi(line)
"""
