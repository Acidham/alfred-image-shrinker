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
for file_path in sys.argv[1:]:
    file_extension = Path(file_path).suffix[1:].lower()
    if file_extension in WHITELIST_EXT:
        img_suffix = os.getenv('img_suffix')
        target_folder = os.getenv('target_folder')
        path = Path(file_path)

        if not (os.getenv('target_folder')) and not (img_suffix):
            img_suffix = '_shrinked'

        if target_folder:
            path = Path(target_folder) / path.name

        if img_suffix:
            new_file_name = f"{path.stem}{img_suffix}{path.suffix}"
            new_file_path = path.with_name(new_file_name)
            shutil.copyfile(file_path, new_file_path)
            file_path = str(new_file_path)

        image_files.append(file_path)
"""
image_files = []
for f in sys.argv[1::]:
    ext = Path(f).suffix.replace('.', '').lower()
    if ext in WHITELIST_EXT:
        img_suffix = os.getenv('img_suffix')
        path, filename = os.path.split(f)
        if not (os.getenv('target_folder')) and not (img_suffix):
            img_suffix = '_shrinked'
        if os.getenv('target_folder'):
            path = os.getenv('target_folder')
        # create a copy if img_suffix is not empty in WF config
        if img_suffix:
            basename, extension = os.path.splitext(filename)
            new_file_name = f"{basename}{img_suffix}{extension}"
            new_file = os.path.join(path, new_file_name)
            shutil.copyfile(f, new_file)
            f = new_file

        image_files.append(f)
"""

files = "\t".join(image_files)

sys.stdout.write(files)
