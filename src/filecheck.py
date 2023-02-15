#!/usr/bin/python3

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
        image_files.append(f)

files = "\t".join(image_files)

sys.stdout.write(files)
