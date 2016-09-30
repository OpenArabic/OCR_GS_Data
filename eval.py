#! /usr/bin/env python

from kraken.lib import models
from kraken import rpred
from PIL import Image
from glob import glob
import sys

model = sys.argv[1]
gt = sys.argv[2] if len(sys.argv) > 2 else '.'

rnn = models.load_any(model)
ims = glob(gt + '/*.png')

for f in ims:
    print(f)
    im = Image.open(f)
    it = rpred.rpred(rnn, im, [(0, 0) + im.size])
    with open(f + '.rec.txt', 'wb') as fp:
        fp.write(it.next().prediction.encode('utf-8'))
