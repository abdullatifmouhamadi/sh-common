 # /usr/bin/python

from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php72, chmod, mv, cp, sed
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
    else:
        logi(title="release alread exists",msg="")
    
    return release_path(release)


def release_path(release):
    return CACHE_DIR+release + '.zip'