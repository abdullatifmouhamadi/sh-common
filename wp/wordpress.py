 # /usr/bin/python

from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php72, chmod, mv, cp
from sh.contrib import git
import sh, contextlib, os
from .releases import RELEASES, release_filename, REPO, release_extract_dir
from .config import CACHE_DIR, TMP_DIR, ADMIN_DIR, APP_OWNER
import sys

from ..common.utils import log, logi

def _pull_release(release):
    if not release in RELEASES:
        raise ValueError('Invalid release')

    filename = release_filename(release)
    if not os.path.isdir( CACHE_DIR ):
        log( "Creating cache dir {} ".format( CACHE_DIR ) )
        mkdir("-p", CACHE_DIR )

    if not os.path.exists( CACHE_DIR + filename ):
        log( "Downloading release {} ".format( filename ) )
        wget( REPO + filename, "-O", CACHE_DIR + filename)



def copy_src(installDir, release):
    _pull_release(release)
    filename    = CACHE_DIR + release_filename(release)
    extract_dir = CACHE_DIR + release_extract_dir(release)
    if not os.path.isdir( extract_dir ):
        log( "Extracting {} ".format( filename ) )
        unzip("-n", "-q", filename, "-d", extract_dir)

    
    log( "Removing old files ... " )
    rm("-rf", installDir)

    log( "Creating install dir {} ... ".format(installDir) )
    mkdir("-p", installDir )

    log( "Copying files ... " )
    #unzip("-n", "-q", extract_dir + '' , "-d", installDir)
    cp("-arf", extract_dir + '/WordPress-' + release + '/.', installDir) # /. content of the directory

    #chown("-R", APP_OWNER, installDir)


def setup(installDir, config):

    if not os.path.isdir( installDir ):


        copy_src(installDir = installDir, release = config['CMS_WORDPRESS_RELEASE'])
        """
        install(installDir      = installDir, 
                domain          = config['SHOP_HOST_DOMAIN'], #TEMPLATE_DOMAIN_NAME, 
                db_server       = config['MYSQL_HOST'],
                db_name         = config['SHOP_DB_NAME'],#database_name, 
                db_user         = config['MYSQL_USER'], 
                db_password     = config['MYSQL_PASSWORD'],
                admin_email     = config['ADMIN_EMAIL'],
                admin_password  = config['ADMIN_PASSWORD'])
        """

    else:
        logi( "The instance '{}' ".format(config['CMS_WORDPRESS_RELEASE']) + 'already exist ...' )
    #copy_templates(release)
