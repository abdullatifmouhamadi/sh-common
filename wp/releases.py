REPO     = 'https://github.com/WordPress/WordPress/archive/'
RELEASES = [
    '5.5.1',
    '5.5',
    '5.4.2',
    '5.3.4'  
]


def release_filename(release):
    return release + '.zip'

def release_extract_dir(release):
    return release



