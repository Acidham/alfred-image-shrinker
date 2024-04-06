#!/usr/bin/python3

import os
import shutil
import sys
from pathlib import Path

WHITELIST_EXT = [
    'png',
    'jpeg',
    'jpg',
    'gif',
    'tiff',
    'bmp',
    'psd',
    'heic',
]

image_files = []
for f in sys.argv[1::]:
    ext = Path(f).suffix.replace('.', '').lower()
    if ext in WHITELIST_EXT:
        # create a copy if img_suffix is not empty in WF config
        if os.getenv('img_suffix'):
            path, filename = os.path.split(f)
            basename, extension = os.path.splitext(filename)
            new_file_name = f"{basename}{os.getenv('img_suffix')}.{extension}"
            new_file = os.path.join(path, new_file_name)
            shutil.copyfile(f, new_file)
            f = new_file

        image_files.append(f)

files = "\t".join(image_files)

sys.stdout.write(files)
