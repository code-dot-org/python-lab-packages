import base64
import os

from io import BytesIO

os.environ['MPLBACKEND'] = 'AGG'

import matplotlib.pyplot

def patch_matplotlib(matplotlib_img_tag):
    _old_show = matplotlib.pyplot.show

    def show():
        buf = BytesIO()
        matplotlib.pyplot.savefig(buf, format='png')
        buf.seek(0)
        # encode to a base64 str
        img = base64.b64encode(buf.read()).decode('utf-8')
        print(f'{matplotlib_img_tag} {img}')
        matplotlib.pyplot.clf()

    matplotlib.pyplot.show = show
