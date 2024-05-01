from .patch_matplotlib import patch_matplotlib
from .patch_requests import reload_requests_and_patch

def setup_pythonlab(matplotlib_img_tag, host, channel_id):
  patch_matplotlib(matplotlib_img_tag)
  reload_requests_and_patch(host, channel_id)
