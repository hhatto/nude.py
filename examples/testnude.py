from __future__ import print_function

import os
from nude import Nude


IMAGE_ROOT = ROOT = os.path.dirname(os.path.abspath(__file__)) + '/images/'
for file_name in os.listdir(IMAGE_ROOT):
    file_path = os.path.join(IMAGE_ROOT, file_name)
    if os.path.isdir(file_path):
        continue
    n = Nude(file_path)
    n.parse()
    print(n.result, n.message)

