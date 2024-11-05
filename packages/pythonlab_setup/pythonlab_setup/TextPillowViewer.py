from PIL import ImageShow
import base64
import os
from io import BytesIO

class TextPillowViewer(ImageShow.Viewer):
  
  def show(self, image, **options):
    buffered = BytesIO()
    image.save(buffered, format="png")
    buffered.seek(0)
    img_str = base64.b64encode(buffered.read()).decode('utf-8')
    # todo: parameterize this
    print(f'MATPLOTLIB_SHOW_IMG {img_str}')
    return 1