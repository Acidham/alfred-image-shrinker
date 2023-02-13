#!/usr/bin/python3

import mimetypes
import sys
from pathlib import Path

image_files = []
for f in sys.argv[1::]:
    mt, n = mimetypes.guess_type(f)
    ext = Path(f).suffix
    if ext.lower() == '.heic' or (mt != None and "image" in mt):
        image_files.append(f)

files = "\t".join(image_files)

sys.stdout.write(files)
