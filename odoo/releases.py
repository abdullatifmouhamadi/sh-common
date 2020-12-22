REPO     = 'https://github.com/odoo/odoo/archive/'

RELEASES = [
    '14.0',
    '13.0',
    '12.0',
]


def release_filename(release):
    return release + '.zip'

def release_extract_dir(release):
    return release
    