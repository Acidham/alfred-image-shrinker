import os
import sys

source_file = sys.argv[1]
source_path = os.path.dirname(source_file)
sys.stdout.write(source_path)
