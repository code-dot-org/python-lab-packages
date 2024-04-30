from .patch_matplotlib import patch_matplotlib
from .patch_requests import patch_requests

def setup_pythonlab(matplotlib_img_tag, host, channel_id):
  print("hello from setup!")
  patch_matplotlib(matplotlib_img_tag)
  patch_requests(host, channel_id)
