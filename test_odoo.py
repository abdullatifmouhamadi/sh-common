 # /usr/bin/python

from odoo.odoo import _pull_release,release_path

_pull_release(release = '13.0')

#print("salut")

print("path =" + release_path(release='13.0'))
