"""
This code is used to download files
"""

import os
import cgi
import requests
import shutil

if __name__ != "__main__":
    __version__ = 0.1


def download_file(url, path, file_name=None):
    """
    Download file from url to path.
    If file_name is not given, it would either look for the filename
    in Content-Disposition header or use the filename in url.
    """
    res = requests.get(url, stream=True)
    if res.status_code != 200:
        raise ValueError(f'Failed to download: {res.status_code}')

    if file_name is None:
        if 'Content-Disposition' in res.headers:
            params = cgi.parse_header(
                res.headers.get('Content-Disposition', ''))[-1]
            if 'filename' not in params:
                raise ValueError('Could not find a filename')
            file_name = params['filename']
        else:
            file_name = os.path.basename(url)

    abs_path = os.path.join(path, os.path.basename(file_name))
    with open(abs_path, 'wb') as target:
        res.raw.decode_content = True
        shutil.copyfileobj(res.raw, target)

    print(f"Download {file_name}")
