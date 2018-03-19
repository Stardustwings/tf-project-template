#!/usr/bin/env python3

from PIL import Image
from glob import glob

# from datetime import datetime

# start = datetime.now()

for image_file in glob('valid_encoded/*.jpg'):
    Image.open(image_file).save(image_file[:-3] + 'png')

# end = datetime.now()

# print('Run time: {}'.format((end - start).microseconds))
