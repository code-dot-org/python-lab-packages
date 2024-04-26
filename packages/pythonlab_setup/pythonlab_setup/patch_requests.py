import requests
import urllib.parse

def get_proxy_path(host, url, channel_id):
    return f"{host}/xhr?u={urllib.parse.quote(url, safe='/:')}&c={urllib.parse.quote(channel_id, safe='/:')}"


def patch_requests(host, channel_id):
    _old_get = requests.get

    def get(url, params=None, **kwargs):
        print("hello from patch!")
        print(f"host: {host}, url: {url}, channel_id: {channel_id}")
        url = get_proxy_path(host, url, channel_id)
        return _old_get(url, params, **kwargs)

    requests.get = get
